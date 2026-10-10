"""Idempotent event consumer — reference implementation.

Pub/Sub delivers at-least-once. Every consumer MUST check
idempotency_key before acting, or retries double-post journal
entries, double-charge revenue, and corrupt the trial balance.

Usage:
    consumer = IdempotentConsumer(store)
    consumer.handle(event, handler)
"""

from __future__ import annotations

from typing import Any, Callable

from packages.events.models import PlatformEvent


class ProcessedEventsStore:
    """Minimal in-memory store. Swap for Redis/Firestore in production."""

    def __init__(self) -> None:
        self._seen: set[str] = set()

    def seen(self, key: str) -> bool:
        return key in self._seen

    def record(self, key: str) -> None:
        self._seen.add(key)


class IdempotentConsumer:
    """Wraps any event handler with deduplication."""

    def __init__(self, store: ProcessedEventsStore | None = None) -> None:
        self.store = store or ProcessedEventsStore()

    def handle(
        self,
        event: PlatformEvent,
        handler: Callable[[PlatformEvent], Any],
    ) -> dict[str, Any]:
        key = event.idempotency_key
        if self.store.seen(key):
            return {
                "status": "skipped_duplicate",
                "idempotency_key": key,
                "event_type": event.event_type,
            }
        result = handler(event)
        self.store.record(key)
        return {
            "status": "processed",
            "idempotency_key": key,
            "event_type": event.event_type,
            "result": result,
        }
