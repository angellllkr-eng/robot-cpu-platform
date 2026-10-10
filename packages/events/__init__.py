"""Event contract package for the Robot–CPU platform."""

from packages.events.models import (
    PlatformEvent,
    FACT_VERIFIED,
    FACT_REJECTED,
    RISK_DETECTED,
    OPPORTUNITY_FOUND,
    REVENUE_GENERATED,
    JOURNAL_POSTED,
    RECONCILIATION_GAP_DETECTED,
    LEARNING_CAPTURED,
)
from packages.events.consumer import IdempotentConsumer, ProcessedEventsStore

__all__ = [
    "PlatformEvent",
    "IdempotentConsumer",
    "ProcessedEventsStore",
    "FACT_VERIFIED",
    "FACT_REJECTED",
    "RISK_DETECTED",
    "OPPORTUNITY_FOUND",
    "REVENUE_GENERATED",
    "JOURNAL_POSTED",
    "RECONCILIATION_GAP_DETECTED",
    "LEARNING_CAPTURED",
]
