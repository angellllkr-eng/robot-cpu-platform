"""A11-K Command Gateway — Founder view of the Brain.

ADR-0012: Founder Command Center.

GET /dashboard → truth score, verification coverage, risk exposure, decision velocity
"""

from __future__ import annotations

import httpx
from fastapi import FastAPI

app = FastAPI(title="A11-K Command Gateway", version="1.0.0")

REALITY_URL = "http://reality:8001"
RISK_URL = "http://risk:8003"


@app.get("/dashboard")
def dashboard() -> dict:
    """Aggregate Brain metrics for the Founder."""
    truth = {"truth_score": 0.0, "verified": 0, "total": 0}
    risks = {"total_open": 0}

    try:
        with httpx.Client(timeout=2.0) as client:
            t = client.get(f"{REALITY_URL}/a11k/reality/truth").json()
            truth = {"truth_score": t.get("truth_score", 0), "verified": t.get("verified", 0), "total": t.get("total", 0)}
            r = client.get(f"{RISK_URL}/a11k/risk/open").json()
            risks = {"total_open": r.get("total_open", 0)}
    except Exception:
        pass  # services may be down during boot

    return {
        "platform": "a11k",
        "truth_score": truth["truth_score"],
        "verification_coverage": truth["truth_score"],
        "verified_facts": truth["verified"],
        "total_claims": truth["total"],
        "risk_exposure": risks["total_open"],
        "decision_velocity": 0.0,  # wired in v2
    }


@app.get("/health")
def health() -> dict:
    return {"service": "a11k-gateway", "status": "healthy"}
