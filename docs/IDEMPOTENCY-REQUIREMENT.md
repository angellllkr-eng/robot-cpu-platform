# Idempotency Requirement — Mandatory for All Consumers

**Status:** Mandatory (v1.1)
**Owner:** A11-K governance
**Related:** ADR-0004 (Event-First), Amendment-0001 (Tiered Approval)

## The Rule

Every event consumer MUST check `idempotency_key` before acting.

Pub/Sub and any at-least-once delivery guarantee means retries are normal.
Without this check:

- Journal entries post twice → trial balance breaks
- Revenue records twice → books lie
- Risk assessments duplicate → false escalation

## Two Fields, Two Jobs

| Field | Job |
|---|---|
| `correlation_id` | Traces one operation across services (one cause, many effects) |
| `idempotency_key` | Deduplication key — same key = same action, skip on retry |

## The Reference Implementation

`packages/events/consumer.py` — `IdempotentConsumer`.

Every service adopts this wrapper. No raw handler calls allowed in production.

## Test Evidence

- Duplicate event with same key: handler runs once, second skipped
- Different key: processed normally
- All 44 vocabulary entries present including accounting and learning events

## Enforcement

Governance-service rejects any service that cannot demonstrate idempotent
consumption. This is a Zero Operational Law gate.
