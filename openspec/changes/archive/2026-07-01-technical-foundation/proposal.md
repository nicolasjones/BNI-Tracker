# Proposal: Technical Foundation

## Intent

Prepare a durable engineering base for BNI Track so the MVP can grow without rewrites: reproducible local setup, deployable web app, AI service boundary, data foundation, and project conventions.

## Scope

### In Scope
- Define the base stack: Next.js + TypeScript, Python + FastAPI, Supabase, Vercel, Docker.
- Establish repository and environment conventions: local dev, secrets, configs, and SDD/OpenSpec workflow.
- Add minimum engineering guardrails: CI/tests, lint/format, logging, security baseline, rollback/feature flags.

### Out of Scope
- Product features from Release 1.
- Matching, chapter, power teams, region, and advanced AI behaviors.
- Vendor-specific AI coupling.

## Capabilities

### New Capabilities
- `platform-foundation`: base stack, deployment, local development, and architecture conventions.
- `engineering-foundations`: CI, testing, observability, security, rollback, and feature flags.

### Modified Capabilities
- None

## Approach

Use Next.js for the web product, Supabase for persistence/auth/storage/realtime, Python for the AI/service layer, Vercel for web deployment, and Docker for Python/workers and reproducible local development. Keep the AI layer provider-agnostic.

## Affected Areas

| Area | Impact | Description |
|------|--------|-------------|
| `openspec/config.yaml` | Modified | Keep SDD/hybrid config aligned with the chosen foundation. |
| `.atl/sdd-launcher.md` | Modified | Preserve repo-local SDD entrypoint conventions. |
| `.atl/skill-registry.md` | Modified | Keep the delegator index current. |
| `openspec/changes/technical-foundation/` | New | Proposal/specs for the foundation slice. |

## Risks

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| Overbuilding infrastructure before product validation | Medium | Keep the scope limited to foundations only. |
| Coupling IA to one vendor | High | Introduce a provider-agnostic model gateway from day one. |
| Weak quality gates at launch | Medium | Add minimal CI/testing/linting early. |

## Rollback Plan

Revert foundation changes by restoring the repo to the current prototype state and removing only the new foundation scaffolding. No product data migrations are expected in this slice.

## Dependencies

- Agreement on the final foundation stack.
- Access to Supabase and Vercel accounts.
- Initial AI provider abstraction decision.

## Success Criteria

- [ ] The repo has a reproducible base for local development and deployment.
- [ ] The web app and AI service are separated cleanly.
- [ ] The project has minimum engineering guardrails for future slices.
