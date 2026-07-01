# Tasks: Technical Foundation

## Review Workload Forecast

| Field | Value |
|-------|-------|
| Estimated changed lines | 700-1200 |
| 400-line budget risk | High |
| Chained PRs recommended | Yes |
| Suggested split | PR 1 foundation scaffolding → PR 2 AI service + Docker → PR 3 CI/tests/ops |
| Delivery strategy | apply foundation scaffold directly in current workspace |
| Chain strategy | feature-branch-chain selected; local workspace has no git repository metadata |

Decision needed before apply: Yes
Chained PRs recommended: Yes
Chain strategy: feature-branch-chain
400-line budget risk: High

### Suggested Work Units

| Unit | Goal | Likely PR | Notes |
|------|------|-----------|-------|
| 1 | Create web/app foundation and shared config | PR 1 | Base repo structure and env contract |
| 2 | Create AI service and provider gateway skeleton | PR 2 | Depends on PR 1 paths and contracts |
| 3 | Add CI, tests, Docker, rollout guardrails | PR 3 | Can target PR 2 branch or merge after PR 2 |

## Phase 1: Foundation

- [x] 1.1 Create `apps/web/` with Next.js + TypeScript scaffold, base routing, and minimal app shell.
- [x] 1.2 Create `packages/config/` for shared lint/format/type config and wire root package scripts.
- [x] 1.3 Add `.env.example` with web, AI service, Supabase, and provider-gateway variables.
- [x] 1.4 Update `openspec/config.yaml` to reflect real test/build/tooling commands once scaffold exists.

## Phase 2: AI / Runtime Boundaries

- [x] 2.1 Create `services/ai/` FastAPI scaffold with health endpoint and request validation.
- [x] 2.2 Add provider-agnostic gateway contract and one stub adapter path under `services/ai/`.
- [x] 2.3 Define web → AI request/response contract in shared types or mirrored schemas.
- [x] 2.4 Add local service wiring so web and AI runtimes can run together without product features.

## Phase 3: Local Ops / Delivery

- [x] 3.1 Create `infra/docker/` assets for AI service and local multi-service development.
- [x] 3.2 Add local run scripts/docs for web, AI service, and required support services.
- [x] 3.3 Add secret-handling conventions so no credentials are stored in tracked source files.
- [x] 3.4 Add feature-flag/rollback placeholders for incomplete runtime features.

## Phase 4: Testing / CI

- [x] 4.1 RED: add failing Python unit tests for gateway contract, config parsing, and validation behavior.
- [x] 4.2 GREEN: implement enough AI service code to satisfy the new Python unit tests.
- [x] 4.3 Add TS unit tests for config/schema helpers and smoke checks for web boot.
- [x] 4.4 Create `.github/workflows/ci.yml` to run install, lint, format-check, typecheck, unit tests, and web build.
- [x] 4.5 Add integration or smoke verification for web ↔ AI reachability and config error handling.

## Phase 5: Cleanup / Verification

- [x] 5.1 Document local setup, expected commands, and service boundaries in repo-facing docs.
- [x] 5.2 Verify proposal/spec/design artifacts still match the implemented scaffolding and update only if drift appears.
