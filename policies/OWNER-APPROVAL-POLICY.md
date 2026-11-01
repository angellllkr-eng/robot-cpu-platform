# MindReply Owner Approval Policy

**Version:** 1.0.0  
**Status:** Development policy proposal

## Governing rule

System proposes. Owner commands. Automation executes only after approval.

## Always owner-controlled

The following actions require explicit approval for the exact action, target and environment:

- production deployments and releases;
- financial transactions, refunds, transfers or changes to payment behaviour;
- customer or third-party communications;
- credential, secret, identity or permission changes;
- destructive repository actions, including deletion, archival, force-push or merge where owner policy requires review;
- external publication;
- live infrastructure or production configuration changes;
- production database schema or data mutations.

## Approval record

An approval must capture:
1. unique approval ID;
2. authenticated approver identity;
3. action and intended outcome;
4. exact target resource/repository;
5. environment;
6. bounded scope and expiry where supported;
7. decision and timestamp.

A general statement of enthusiasm or approval for a different task is not transferable authorisation. If the action, target or environment changes, request fresh approval.

## Default permissions

- Read-only discovery: permitted within connected account access and privacy boundaries.
- Local/synthetic development work: permitted when reversible and non-destructive.
- Development branch commits: permitted for the explicitly requested implementation, provided the default branch is untouched.
- Production and external side effects: owner approval required.
- Ambiguous permission or missing evidence: fail closed.

## Separation of duties

The component proposing a change should not be the sole source of its production verification. Verification must use direct evidence from the target environment.

## Evidence handling

Record tool results, commit/build identifiers, test output and runtime references. Redact tokens, credentials, personal data and sensitive payloads. Do not claim VERIFIED from documentation, a plan or a screenshot alone.
