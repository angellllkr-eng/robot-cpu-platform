"""Canonical event contract for the Robot–CPU platform.

Everything communicates through events only.
ADR-0004: Event-First Communication.
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
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    payload: dict[str, Any] = Field(default_factory=dict)

    @staticmethod
    def create(event_type: str, source: str, payload: dict[str, Any] | None = None) -> PlatformEvent:
        return PlatformEvent(
            event_type=event_type,
            source=source,
            payload=payload or {},
        )


# ── Canonical event vocabulary ──────────────────────────────────────────────

# A11-K (Brain) events
FACT_SUBMITTED = "FACT_SUBMITTED"
FACT_VERIFIED = "FACT_VERIFIED"
FACT_REJECTED = "FACT_REJECTED"
CONTRADICTION_FOUND = "CONTRADICTION_FOUND"
KNOWLEDGE_CREATED = "KNOWLEDGE_CREATED"
KNOWLEDGE_UPDATED = "KNOWLEDGE_UPDATED"
PATTERN_DISCOVERED = "PATTERN_DISCOVERED"
RISK_DETECTED = "RISK_DETECTED"
RISK_ESCALATED = "RISK_ESCALATED"
RISK_MITIGATED = "RISK_MITIGATED"
RISK_CLOSED = "RISK_CLOSED"
DECISION_CREATED = "DECISION_CREATED"
DECISION_APPROVED = "DECISION_APPROVED"
MISSION_CREATED = "MISSION_CREATED"
PRIORITY_ASSIGNED = "PRIORITY_ASSIGNED"
ORDER_ISSUED = "ORDER_ISSUED"
DIRECTIVE_CREATED = "DIRECTIVE_CREATED"
STANDARD_UPDATED = "PRINCIPLE_CHANGED"

# MindReply (Body) events
OPPORTUNITY_FOUND = "OPPORTUNITY_FOUND"
OPPORTUNITY_QUALIFIED = "OPPORTUNITY_QUALIFIED"
ASSET_CREATED = "ASSET_CREATED"
ASSET_DEPLOYED = "ASSET_DEPLOYED"
REVENUE_GENERATED = "REVENUE_GENERATED"
DELIVERY_STARTED = "DELIVERY_STARTED"
DELIVERY_COMPLETED = "DELIVERY_COMPLETED"
SYSTEM_EXPANDED = "SYSTEM_EXPANDED"
CLIENT_CREATED = "CLIENT_CREATED"
CLIENT_UPDATED = "CLIENT_UPDATED"

# Observatory / security events
ALERT_CREATED = "ALERT_CREATED"
SYSTEM_DEGRADED = "SYSTEM_DEGRADED"
SYSTEM_HEALTHY = "SYSTEM_HEALTHY"
ACCESS_DENIED = "ACCESS_DENIED"
LOGIN_SUCCESS = "LOGIN_SUCCESS"
LOGIN_FAILED = "LOGIN_FAILED"
SECRET_ROTATED = "SECRET_ROTATED"
INCIDENT_REPORTED = "INCIDENT_REPORTED"
DASHBOARD_REFRESHED = "DASHBOARD_REFRESHED"
