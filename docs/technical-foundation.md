# Technical Foundation

BNI Track now uses a split foundation:

- `apps/web`: Next.js + TypeScript product runtime.
- `services/ai`: FastAPI AI/service runtime with provider-agnostic gateway contracts.
- `packages/config`: shared TypeScript and lint configuration.
- `infra/docker`: local Docker assets for the AI service.

## Local setup

1. Copy `.env.example` to `.env` and fill secrets outside source control.
2. Install JavaScript dependencies with `npm install`.
3. Install Python dependencies from `services/ai/pyproject.toml` in a virtual environment.
4. Run web with `npm run dev:web`.
5. Run AI service with `uvicorn app.main:app --app-dir services/ai --reload` or Docker Compose from `infra/docker`.

## Quality commands

- `npm run lint`
- `npm run format:check`
- `npm run typecheck`
- `npm run test:ts`
- `npm run test:py`
- `npm run build:web`
- `npm run smoke:ai` (requires the AI service running)

## Secrets and rollout

Tracked files must never contain real credentials. Use `.env.example` for the contract and keep `.env` local or provider-managed. Incomplete runtime behavior should be guarded by feature flags such as `FEATURE_AI_AGENT`.
