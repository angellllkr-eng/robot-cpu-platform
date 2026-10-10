"""A11-K Risk Service — threat detection, exposure analysis, recovery planning.

ADR-0007: Risk Is A First-Class Domain.

POST /a11k/risk/assess  → assess a target
GET  /a11k/risk/open    → open risks
GET  /a11k/risk/status  → health
"""

from __future__ import annotations

from fastapi import FastAPI

from packages.events.models import PlatformEvent, RISK_DETECTED, RISK_CLOSED

app = FastAPI(title="A11-K Risk Service", version="1.0.0")

RISKS: list[dict] = []


@app.post("/a11k/risk/assess")
def assess(item: dict) -> dict:
    """Assess risk for a target. v1: placeholder scoring."""
    target = item.get("target", "unknown")
    impact = float(item.get("impact", 5))
    likelihood = float(item.get("likelihood", 5))
    score = round(impact * likelihood, 1)

    if score >= 50:
        severity = "CRITICAL"
    elif score >= 25:
        severity = "HIGH"
    elif score >= 10:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    risk = {
        "target": target,
        "score": score,
        "severity": severity,
        "impact": impact,
        "likelihood": likelihood,
        "status": "OPEN",
        "owner": item.get("owner", "unassigned"),
    }
    RISKS.append(risk)

    PlatformEvent.create(event_type=RISK_DETECTED, source="a11k.risk", payload=risk)
    return risk


@app.get("/a11k/risk/open")
def open_risks() -> dict:
    open_ = [r for r in RISKS if r["status"] == "OPEN"]
    return {"risks": open_, "total_open": len(open_), "total": len(RISKS)}


@app.get("/a11k/risk/status")
def status() -> dict:
    return {"service": "risk-service", "status": "healthy", "domain": "a11k"}
