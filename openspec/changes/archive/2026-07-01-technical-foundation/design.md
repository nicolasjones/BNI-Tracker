# Design: Technical Foundation

## Technical Approach

Build BNI Track as a split platform: a Next.js web app for product UX, a Python FastAPI service for AI orchestration, and Supabase as the managed persistence/auth/storage boundary. Keep the current HTML prototypes as reference-only assets while introducing a new application structure beside them.

## Architecture Decisions

### Decision: Runtime split

**Choice**: Next.js for web UI/BFF, FastAPI for AI/service runtime, Supabase for data services.  
**Alternatives considered**: Monolithic Python app; Next.js-only full stack.  
**Rationale**: Matches the chosen stack, keeps AI workflows isolated, and avoids coupling product UI to provider-specific AI logic.

### Decision: Provider-agnostic AI boundary

**Choice**: Put model selection behind a Python service abstraction instead of inside the web app.  
**Alternatives considered**: OpenAI-first SDK in product runtime.  
**Rationale**: Preserves portability across OpenAI, Chinese, or future providers without rewriting product-facing flows.

### Decision: Foundation-first rollout

**Choice**: Introduce engineering guardrails with the first scaffolding slice.  
**Alternatives considered**: Add CI/tests/observability later.  
**Rationale**: The repo currently has no runtime app, no tests, and no CI; delaying guardrails would make future slices harder to stabilize.

## Data Flow

```text
Browser
  │
  ▼
Next.js App ─────→ Supabase Auth / Postgres / Storage
  │
  └────→ FastAPI AI Service ─────→ Model Provider Gateway
                    │
                    └────→ Supabase Storage / Postgres artifacts
```

- Next.js owns routing, UI composition, and user-facing requests.
- FastAPI owns AI orchestration, background-friendly workflows, and provider abstraction.
- Supabase remains the shared system of record and storage boundary.

## File Changes

| File | Action | Description |
|------|--------|-------------|
| `apps/web/` | Create | Next.js application root for the product UI. |
| `services/ai/` | Create | FastAPI service root for AI orchestration and provider abstraction. |
| `packages/config/` | Create | Shared lint/type/config conventions where useful. |
| `infra/docker/` | Create | Docker assets for Python service and local multi-service development. |
| `.github/workflows/ci.yml` | Create | Baseline CI for checks and tests. |
| `.env.example` | Create | Required environment variable contract. |
| `openspec/config.yaml` | Modify | Keep SDD/testing/runtime assumptions aligned with real scaffolding. |

## Interfaces / Contracts

```ts
// web → ai service
type AgentRequest = {
  actorId: string;
  context: { surface: string; entityId?: string };
  input: string;
};
```

```py
# ai provider boundary
class ModelGateway(Protocol):
    async def generate(self, request: AgentRequest) -> dict: ...
```

- The web app talks to the AI service through a stable request/response contract.
- The AI service talks to providers only through the gateway abstraction.

## Testing Strategy

| Layer | What to Test | Approach |
|-------|-------------|----------|
| Unit | Python domain logic, gateway adapters, parsing, validation; TS utilities and schemas | Fast isolated tests in both runtimes |
| Integration | Next.js ↔ Supabase, FastAPI ↔ gateway, storage/auth/config wiring | Service integration tests with test env config |
| E2E | Boot, login, base routing, and basic AI-service reachability | Browser-level smoke tests first |

- TDD is **strict** for Python domain logic, provider adapters, parsing, and API contracts.
- TDD is **lighter** for early Next.js scaffolding and layout work; behavior tests matter more than pixel-first tests.
- CI starts with install, lint, format-check, typecheck, unit tests, web build, and Python smoke checks.
- CI expands later with integration coverage, E2E smoke runs, and coverage gates.

## Migration / Rollout

No product-data migration required. Roll out by introducing scaffolding in parallel with existing prototype assets, then move future slices onto the new runtime. Use environment-based toggles for incomplete AI/runtime features if needed.

- CD begins with preview deployments and non-production validation.
- Staging may be added before production if the first hosted slice needs environment separation.
- Production release remains manual-first until the MVP core is stable.

## Open Questions

- [ ] Which job mechanism will back long-running AI workflows first: lightweight in-process jobs or external queue?
- [ ] Will the first release require staging and production from day one, or only local plus one hosted environment?
