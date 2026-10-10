# ADR → Service → Event Map

Constitutional traceability: every ADR maps to services, every service maps to events.

## ADR-0002 · A11-K Owns Certainty

| Service | Events Produced |
|---------|----------------|
| reality-service | FACT_VERIFIED, FACT_REJECTED, CONTRADICTION_FOUND |
| knowledge-service | KNOWLEDGE_CREATED, KNOWLEDGE_UPDATED, PATTERN_DISCOVERED |
| risk-service | RISK_DETECTED, RISK_ESCALATED, RISK_MITIGATED, RISK_CLOSED |
| executive-service | DECISION_CREATED, DECISION_APPROVED, MISSION_CREATED |
| founder-service | DIRECTIVE_CREATED, STANDARD_UPDATED, PRINCIPLE_CHANGED |
| command-service | MISSION_CREATED, PRIORITY_ASSIGNED, ORDER_ISSUED |

## ADR-0003 · MindReply Owns Value

| Service | Events Produced |
|---------|----------------|
| discovery-service | OPPORTUNITY_FOUND, OPPORTUNITY_QUALIFIED |
| builder-service | ASSET_CREATED, ASSET_DEPLOYED |
| commerce-service | REVENUE_GENERATED |
| delivery-service | DELIVERY_STARTED, DELIVERY_COMPLETED |
| expansion-service | SYSTEM_EXPANDED |

## ADR-0011 · Security Default

| Service | Events Produced |
|---------|----------------|
| security-service | ACCESS_DENIED, LOGIN_SUCCESS, LOGIN_FAILED, SECRET_ROTATED, INCIDENT_REPORTED |

## ADR-0013 · Observatory

| Service | Events Produced |
|---------|----------------|
| observatory-service | ALERT_CREATED, SYSTEM_DEGRADED, SYSTEM_HEALTHY (consumes ALL) |

## ADR-0014 · Human Authority

| Service | Events Produced |
|---------|----------------|
| approval-service | APPROVAL_REQUESTED, APPROVAL_GRANTED, APPROVAL_REJECTED |

## ADR-0015 · Constitutional Loop

```
CLAIM_SUBMITTED → FACT_VERIFIED → KNOWLEDGE_CREATED → RISK_ASSESSED
→ MISSION_CREATED → OPPORTUNITY_FOUND → ASSET_CREATED
→ REVENUE_GENERATED → RESULT_OBSERVED → LEARNING_CAPTURED → KNOWLEDGE_UPDATED
```
