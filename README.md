# Robot–CPU Platform

A11-K × MindReply — The executive AI operating system for certainty and value.

## Mission

Robot–CPU Platform is the canonical operating architecture for a disciplined AI enterprise.

- A11-K is the intelligence layer: verify, know, govern, decide, and protect.
- MindReply is the execution layer: discover, build, sell, deliver, and scale.
- Founder is the authority layer: decide, approve, and own outcomes.

This structure creates a system where truth and value are not optional. They are the operating standard.

## Operating principle

Every input becomes one of four categories:

- Knowledge
- Decision
- Action
- Result

If an input does not increase certainty or value, it is rejected.

## The system

```text
Signal → Knowledge → Verification → Decision → Execution → Observation → Learning → Knowledge
```

## Platform architecture

```text
robot-cpu-platform/
├── apps/                       # Founder-facing and operator-facing gateways
│   ├── a11k-gateway/
│   ├── mindreply-gateway/
│   └── ak-precision-robotics/
├── services/                   # Runtime service domains
│   ├── reality-service/        # A11-K: fact verification
│   ├── knowledge-service/      # A11-K: knowledge graph and memory
│   ├── risk-service/           # A11-K: risk and resilience
│   ├── executive-service/      # A11-K: prioritization and decisions
│   ├── discovery-service/      # MindReply: opportunity discovery
│   ├── builder-service/        # MindReply: product creation
│   ├── commerce-service/        # MindReply: revenue and growth
│   ├── delivery-service/       # MindReply: client outcomes
│   └── expansion-service/      # MindReply: scale and reach
├── packages/
│   ├── events/
│   ├── auth/
│   ├── logging/
│   ├── config/
│   └── execution-contracts/
├── docs/                       # Constitution, ADRs, operating principles
├── policies/
├── prompts/
├── tests/
├── docker-compose.yml
├── pyproject.toml
├── README.md
└── LICENSE
```

## Core law

1. Does it increase certainty? → A11-K
2. Does it increase value? → MindReply
3. Does it increase neither? → Reject

## Event contract

Everything communicates through typed events.

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

## Governance and authority

The platform is governed by a simple rule:

- CPUs verify
- Robots execute
- Humans authorize

This means human approval remains sovereign at critical decision points, while the system continuously provides evidence, context, and operational intelligence.

## Brand and design system

This repository is the canonical source for the ecosystem’s premium operating identity.

See: `docs/BRAND-SYSTEM.md`

The system is intentionally:

- executive-grade
- restrained and premium
- calm, precise, and credible
- low-noise and high-signal
- built for trust, clarity, and execution

## Evidence and accountability

The platform is designed to make outcomes auditable.

- evidence trails matter
- decisions are traceable
- risk is monitored continuously
- system health is observable
- operational actions remain reviewable

## Run locally

```bash
docker compose up --build
```

## Key ecosystem links

- A11-K Core: https://github.com/angellllkr-eng/a11k-core
- A11 Sovereign Nowline: legacy reference only
- A11 Evidence Surface: public proof layer
- Solara Brand Identity: premium design system
- MindReply execution contracts: packages/execution-contracts

## Status

This repository is the operating system authority for the current platform architecture.

The system is designed to be clear, scalable, and trustworthy—without gimmicks, unnecessary novelty, or inflated hype.
