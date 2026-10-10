"""Canonical event contract for the Robot–CPU platform.

Everything communicates through events only.
ADR-0004: Event-First Communication.

v1.1: idempotency_key added as a mandatory deduplication field.
correlation_id traces one operation across services.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field


class PlatformEvent(BaseModel):
    """Canonical event envelope. Required fields per ADR-0004."""

    event_id: str = Field(default_factory=lambda: str(uuid4()))
    event_type: str
    source: str
    correlation_id: str = Field(default_factory=lambda: str(uuid4()))
    idempotency_key: str = Field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    payload: dict[str, Any] = Field(default_factory=dict)

    @staticmethod
    def create(
        event_type: str,
        source: str,
        payload: dict[str, Any] | None = None,
        correlation_id: str | None = None,
        idempotency_key: str | None = None,
    ) -> PlatformEvent:
        return PlatformEvent(
            event_type=event_type,
            source=source,
            payload=payload or {},
            correlation_id=correlation_id or str(uuid4()),
            idempotency_key=idempotency_key or str(uuid4()),
        )


# ── Canonical event vocabulary ──────────────────────────────────────────────

# A11-K (Brain) events
FACT_SUBMITTED = "fact.submitted"
FACT_VERIFIED = "fact.verified"
FACT_REJECTED = "fact.rejected"
CONTRADICTION_FOUND = "fact.contradiction_found"
KNOWLEDGE_CREATED = "knowledge.created"
KNOWLEDGE_UPDATED = "knowledge.updated"
PATTERN_DISCOVERED = "knowledge.pattern_discovered"
RISK_DETECTED = "risk.detected"
RISK_ESCALATED = "risk.escalated"
RISK_MITIGATED = "risk.mitigated"
RISK_CLOSED = "risk.closed"
DECISION_CREATED = "decision.created"
DECISION_APPROVED = "decision.approved"
MISSION_CREATED = "mission.created"
PRIORITY_ASSIGNED = "priority.assigned"
ORDER_ISSUED = "order.issued"
DIRECTIVE_CREATED = "directive.created"
STANDARD_UPDATED = "standard.updated"

# MindReply (Body) events
OPPORTUNITY_FOUND = "opportunity.found"
OPPORTUNITY_QUALIFIED = "opportunity.qualified"
ASSET_CREATED = "asset.created"
ASSET_DEPLOYED = "asset.deployed"
REVENUE_GENERATED = "revenue.generated"
DELIVERY_STARTED = "delivery.started"
DELIVERY_COMPLETED = "delivery.completed"
SYSTEM_EXPANDED = "system.expanded"
CLIENT_CREATED = "client.created"
CLIENT_UPDATED = "client.updated"

# Accounting events
JOURNAL_POSTED = "journal.posted"
RECONCILIATION_COMPLETED = "reconciliation.completed"
RECONCILIATION_GAP_DETECTED = "reconciliation.gap_detected"

# Observatory / security events
ALERT_CREATED = "alert.created"
SYSTEM_DEGRADED = "system.degraded"
SYSTEM_HEALTHY = "system.healthy"
ACCESS_DENIED = "security.access_denied"
LOGIN_SUCCESS = "security.login_success"
LOGIN_FAILED = "security.login_failed"
SECRET_ROTATED = "security.secret_rotated"
INCIDENT_REPORTED = "security.incident_reported"
DASHBOARD_REFRESHED = "dashboard.refreshed"

# Learning loop
LEARNING_CAPTURED = "learning.captured"
