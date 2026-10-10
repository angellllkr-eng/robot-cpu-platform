"""MindReply Commerce Service — revenue, offers, pipeline, forecasts.

ADR-0003: MindReply Owns Value Creation.

GET  /mr/commerce/revenue  → current revenue state
POST /mr/commerce/offer    → record an accepted offer
GET  /mr/commerce/status    → health
"""

from __future__ import annotations

from fastapi import FastAPI

from packages.events.models import PlatformEvent, REVENUE_GENERATED

app = FastAPI(title="MindReply Commerce Service", version="1.0.0")

STATE = {"revenue": 0.0, "offers": 0, "clients": 0}


@app.get("/mr/commerce/revenue")
def revenue() -> dict:
    return {**STATE}


@app.post("/mr/commerce/offer")
def offer(data: dict) -> dict:
    amount = float(data.get("amount", 0))
    STATE["revenue"] += amount
    STATE["offers"] += 1
    if data.get("new_client"):
        STATE["clients"] += 1

    event = PlatformEvent.create(
        event_type=REVENUE_GENERATED,
        source="mr.commerce",
        payload={"amount": amount, "total_revenue": STATE["revenue"]},
    )
    return {"status": "accepted", "event_id": event.event_id, "revenue": STATE["revenue"]}


@app.get("/mr/commerce/status")
def status() -> dict:
    return {"service": "commerce-service", "status": "healthy", "domain": "mindreply"}
