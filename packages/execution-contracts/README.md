# MindReply Execution Contracts

This package contains the shared machine-readable contracts used by all MindReply departments.

## Schemas

- `schema/execution-record.schema.json` — execution lifecycle, owner, approvals, tool calls, tests and evidence.
- `schema/prompt-contract.schema.json` — required fields for versioned production prompts.

## Compatibility rules

- Additive optional fields may be introduced in a minor contract release.
- Renaming/removing required fields or changing their meaning requires a major version.
- Producers must not emit fields outside the schema.
- Consumers must reject malformed records and fail closed when approval or environment details are ambiguous.
- Store schema version and producer revision with persisted records.

## Evidence rules

A `VERIFIED` record must include direct evidence from the correct environment. Plans, screenshots, documentation and local-only checks cannot independently establish production runtime state.

## Development

Fixtures under `tests/fixtures/` are synthetic. Add positive and negative fixtures for every schema change, including missing required fields, invalid statuses, malformed approvals and prohibited environment/action combinations.
