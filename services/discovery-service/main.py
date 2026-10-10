"""MindReply Discovery Service — opportunity scan across markets, signals, competitors.

ADR-0003: MindReply Owns Value Creation.

POST /mr/discovery/scan            → scan for opportunities
GET  /mr/discovery/opportunities    → list found opportunities
GET  /mr/discovery/status           → health
"""

from __future__ import annotations

from fastapi import FastAPI

from packages.events.models import PlatformEvent, OPPORTUNITY_FOUND

app = FastAPI(title="MindReply Discovery Service", version="1.0.0")

OPPORTUNITIES: list[dict] = []


@app.post("/mr/discovery/scan")
def scan(data: dict) -> dict:
    """Scan a market/signal for opportunities."""
    opportunity = {
        "title": data.get("title", "untitled"),
        "market": data.get("market", "unknown"),
        "signal": data.get("signal", ""),
        "status": "FOUND",
        "source": data.get("source", "unspecified"),
    }
    OPPORTUNITIES.append(opportunity)

    PlatformEvent.create(event_type=OPPORTUNITY_FOUND, source="mr.discovery", payload=opportunity)
    return opportunity


@app.get("/mr/discovery/opportunities")
def list_opportunities() -> dict:
    return {"opportunities": OPPORTUNITIES, "total": len(OPPORTUNITIES)}


@app.get("/mr/discovery/status")
def status() -> dict:
    return {"service": "discovery-service", "status": "healthy", "domain": "mindreply"}
