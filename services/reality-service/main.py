"""A11-K Reality Service — fact verification, evidence intake, source scoring.

ADR-0005: Reality Is The Source Of Truth.
ADR-0002: A11-K Owns Certainty.

POST /a11k/reality/verify   → verify a claim
GET  /a11k/reality/truth    → truth ledger
GET  /a11k/reality/status   → health
"""

from __future__ import annotations

from fastapi import FastAPI

from packages.events.models import PlatformEvent, FACT_VERIFIED, FACT_REJECTED, CONTRADICTION_FOUND

app = FastAPI(title="A11-K Reality Service", version="1.0.0")

FACTS: list[dict] = []


@app.post("/a11k/reality/verify")
def verify_fact(claim: dict) -> dict:
    """Verify a claim. Returns VERIFIED or REJECTED with confidence."""
    text = str(claim.get("claim", "")).strip()
    source = str(claim.get("source", "")).strip()

    if not text or not source:
        fact = {
            "claim": claim,
            "status": "REJECTED",
            "confidence": 0,
            "reason": "missing claim or source",
        }
        FACTS.append(fact)
        return fact

    # v1: deterministic placeholder scoring — replaced by evidence engine in v2
    confidence = 95 if source else 40
    status = "VERIFIED" if confidence >= 80 else "REJECTED"

    fact = {
        "claim": claim,
        "status": status,
        "confidence": confidence,
        "source": source,
    }
    FACTS.append(fact)

    event_type = FACT_VERIFIED if status == "VERIFIED" else FACT_REJECTED
    PlatformEvent.create(event_type=event_type, source="a11k.reality", payload=fact)

    return fact


@app.get("/a11k/reality/truth")
def truth() -> dict:
    verified = [f for f in FACTS if f["status"] == "VERIFIED"]
    return {
        "facts": FACTS,
        "total": len(FACTS),
        "verified": len(verified),
        "truth_score": round(len(verified) / len(FACTS) * 100, 1) if FACTS else 0.0,
    }


@app.get("/a11k/reality/status")
def status() -> dict:
    return {"service": "reality-service", "status": "healthy", "domain": "a11k"}
