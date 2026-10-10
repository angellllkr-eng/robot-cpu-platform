"""MindReply Command Gateway — Founder view of the Body.

ADR-0012: Founder Command Center.

GET /dashboard → revenue, clients, automation rate, growth index
"""

from __future__ import annotations

import httpx
from fastapi import FastAPI

app = FastAPI(title="MindReply Command Gateway", version="1.0.0")

COMMERCE_URL = "http://commerce:8102"
DISCOVERY_URL = "http://discovery:8101"


@app.get("/dashboard")
def dashboard() -> dict:
    """Aggregate Body metrics for the Founder."""
    revenue = {"revenue": 0.0, "offers": 0, "clients": 0}
    opportunities = {"total": 0}

    try:
        with httpx.Client(timeout=2.0) as client:
            r = client.get(f"{COMMERCE_URL}/mr/commerce/revenue").json()
            revenue = r
            o = client.get(f"{DISCOVERY_URL}/mr/discovery/opportunities").json()
            opportunities = {"total": o.get("total", 0)}
    except Exception:
        pass

    return {
        "platform": "mindreply",
        "revenue": revenue.get("revenue", 0.0),
        "offers": revenue.get("offers", 0),
        "clients": revenue.get("clients", 0),
        "opportunities_found": opportunities["total"],
        "automation_rate": 0.0,  # wired in v2
        "growth_index": 0.0,  # wired in v2
    }


@app.get("/health")
def health() -> dict:
    return {"service": "mindreply-gateway", "status": "healthy"}
