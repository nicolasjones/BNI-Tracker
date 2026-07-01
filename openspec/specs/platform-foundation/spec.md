# platform-foundation Specification

## Purpose

Define the base platform, runtime boundaries, and local/deployment conventions for BNI Track.

## Requirements

### Requirement: Base Platform Boundaries

The system MUST define stable boundaries between the web application, AI/service layer, persistence layer, and deployment surfaces.

#### Scenario: Foundation stack is established

- GIVEN the technical foundation is created
- WHEN the platform is defined
- THEN the web product SHALL use a web application runtime
- AND the AI/service layer SHALL remain a separate runtime boundary
- AND persistence SHALL remain a separate managed data boundary

#### Scenario: Future capabilities are added

- GIVEN future releases introduce new behaviors
- WHEN the platform evolves
- THEN the architecture MUST preserve the separation between product UI, AI orchestration, and persistence

### Requirement: Reproducible Local Development

The system MUST support reproducible local development for all required runtimes and services.

#### Scenario: New developer starts the project

- GIVEN a fresh project checkout
- WHEN the developer follows setup conventions
- THEN the local environment MUST be reproducible
- AND required services MUST be identifiable and isolated

#### Scenario: Required configuration is missing

- GIVEN a required environment setting is absent
- WHEN a runtime starts
- THEN the system MUST fail with a clear configuration error

### Requirement: Portable AI Provider Boundary

The system MUST keep model-provider selection outside product-facing application behavior.

#### Scenario: Provider changes in the future

- GIVEN the project adopts a different model provider
- WHEN the AI layer is updated
- THEN product-facing platform contracts MUST remain stable
- AND provider replacement MUST NOT require a full platform rewrite
