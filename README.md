# Robot–CPU Platform

**A11-K (Brain) × MindReply (Body)** — bi-platform operating architecture.

- **A11-K** = Operating Intelligence: verify, know, risk, decide, govern, secure, observe.
- **MindReply** = Operating Presence: discover, build, sell, deliver, scale.
- **Founder** = The Will: authorize, direct, own outcomes.

## Core Principle

Every input becomes one of four things: **Knowledge · Decision · Action · Result**. Nothing else.

## Native Flow

```
Signal → Knowledge → Verification → Decision → Execution → Observation → Learning → Knowledge
```

## Structure

```
robot-cpu-platform/
├── apps/                  # Founder gateways
│   ├── a11k-gateway/
│   └── mindreply-gateway/
├── services/              # CPU + Robot runtime services
│   ├── reality-service/   # A11-K: fact verification
│   ├── knowledge-service/ # A11-K: knowledge graph
│   ├── risk-service/      # A11-K: threat detection
│   ├── executive-service/ # A11-K: prioritization
│   ├── discovery-service/ # MindReply: opportunity scan
│   ├── builder-service/   # MindReply: asset creation
│   ├── commerce-service/  # MindReply: revenue
│   ├── delivery-service/  # MindReply: client outcomes
│   └── expansion-service/ # MindReply: scale
├── packages/
│   ├── events/            # Canonical event contracts
│   ├── auth/
│   ├── logging/
│   └── config/
├── docs/                  # ADRs, constitutions
├── infrastructure/
├── tests/
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

## Event Contract

Everything communicates through events only:

```json
{
  "eventId": "uuid",
  "eventType": "FACT_VERIFIED",
  "source": "a11k.reality",
  "correlationId": "uuid",
  "timestamp": "iso8601",
  "payload": {}
}
```

## Zero Operational Law

1. Does it increase certainty? → A11-K
2. Does it increase value? → MindReply
3. Does it increase neither? → Reject

## Run

```bash
docker compose up --build
```

- A11-K gateway: http://localhost:9001/dashboard
- MindReply gateway: http://localhost:9101/dashboard
- Reality service: http://localhost:8001
- Risk service: http://localhost:8003
- Discovery service: http://localhost:8101
- Commerce service: http://localhost:8102
