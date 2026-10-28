# Minimum Viable Repository Standard

**Status:** Proposed standard — adoption is not implied by the presence of this document.  
**Scope:** Repositories in ZQM Labs and ZQM Computing.  
**Principle:** Improve repositories in place. Do not archive, delete, consolidate, or reduce repository count as part of this program.

This standard defines the minimum evidence and documentation every repository should provide. It is a checklist, not a claim that any repository already complies.

## 1. Required repository landing page

Every maintained repository README should state:

- **Purpose:** one sentence describing what the repository does and who it serves.
- **Maturity:** exactly one evidence-backed status:
  - `Scaffold` — structure exists, but no useful example is yet validated.
  - `Examples Present` — examples are present but have not all been independently verified.
  - `Tested Patterns` — at least one documented example has passed its stated validation.
  - `Production-Ready Patterns` — only when operational, security, compatibility, recovery, and release claims have supporting evidence.
- **Prerequisites:** runtime/tool versions and any required native libraries or external services.
- **Quickstart:** one reproducible example, preferably offline and based on synthetic/public fixtures.
- **Validation:** exact commands, expected outcomes, and known limitations.
- **Non-claims:** what the example/repository does not establish (for example, production deployment, legal permission, complete security, or end-to-end service health).
- **Dependencies:** package manager, manifest, lockfile, and environment recreation command.
- **Contribution and safety:** links to applicable license, contributing, security, and code-of-conduct policies.
- **Related work:** a small number of verified links to relevant repositories and the portfolio index.

Do not set a maturity status based only on repository age, README polish, a successful syntax check, or a green workflow that did not run the relevant example.

## 2. Dependency and environment policy

### Python

- For new Python repositories, prefer `pyproject.toml` with `uv` and a committed `uv.lock`.
- Pin the supported Python version and separate runtime dependencies from development/test dependencies.
- For geospatial stacks with native GDAL/PROJ/GEOS dependencies, evaluate `pixi` where it improves cross-platform reproducibility; do not migrate a working project without evidence that migration is worthwhile.
- Existing Poetry or pip-tools projects may retain their current tooling if lockfile-enforced installs and reproducible tests work.

### JavaScript / TypeScript

- Commit the package manifest and lockfile.
- Use `npm ci` with npm, `pnpm install --frozen-lockfile` with pnpm, or the equivalent frozen install for the selected package manager.
- For new projects, consider pnpm's dependency isolation; existing npm projects do not need a package-manager migration merely for uniformity.
- Document the supported Node version and run tests plus the production build in CI.

### Shared rules

- CI must install from the committed lockfile and fail if it is missing or inconsistent.
- Do not resolve fresh dependency ranges in release/production workflows.
- Automate dependency updates where feasible, with human review for major changes and a documented cooldown/minimum-release-age policy where the ecosystem supports it.
- Do not disable install scripts globally without checking whether required native builds or tooling depend on them; apply least privilege and review package scripts.
- Prefer hashes/integrity metadata, produce an SBOM where appropriate, and record the last successful dependency resolution/validation date.
- A private dependency that cannot be retrieved by a scanner is an **incomplete audit**, not a clean audit. Never embed credentials in repository URLs, expose secrets to untrusted pull-request code, suppress scanner failures, or silently substitute an unaudited artifact.

## 3. Minimum validation by maturity tier

| Tier | Minimum evidence |
|---|---|
| Tier A — core/high visibility | Primary example runs in CI; tests and lint pass; dependency install is lockfile-enforced; release/recovery claims have separate evidence; verification date is updated only after success. |
| Tier B — supporting patterns | At least one example runs in CI; basic lint/tests pass; prerequisites and known limitations are clear. |
| Tier C — early/scaffold | README structure and links are checked; at least one useful manual example is supplied; exact commands and expected results are documented. CI is preferred where affordable. |

Tier indicates effort priority, not a public maturity claim. All tiers retain the minimum README and dependency disclosure.

## 4. Example quality and evidence

A useful example should:

1. Have exact prerequisites and runnable commands.
2. Prefer synthetic or public data that can be redistributed and used offline.
3. State expected output or an objective success criterion.
4. Include a focused test or reproducible validation command.
5. Document provenance, licensing/rights assumptions, and known limitations when relevant.
6. Avoid real credentials, private datasets, participant data, paid answer keys, or production secrets.

Keep static/source validation distinct from runtime validation, integration evidence, and production verification. Record which level actually ran and the exact commit or artifact tested.

## 5. Indexes and cross-repository metadata

The portfolio indexes should progressively track, for each repository:

- repository slug and verified URL;
- one-line purpose and primary language/stack;
- tier and evidence-backed maturity status;
- primary example/quickstart;
- manifest and lockfile names;
- last successful validation date;
- two to four related repositories.

A machine-readable manifest may be introduced in the appropriate index repository. Its validator should check that referenced repositories exist and that status values belong to the approved vocabulary. Do not claim the manifest is complete until it has been reconciled against the actual repository inventory.

## 6. Security and operational boundaries

- Use least-privilege workflow permissions and avoid running untrusted PR code with secrets.
- Never bypass required checks to make a PR green.
- A passing unit test does not prove DNS routing, service health, backup restoration, authorization, payment fulfillment, or production deployment.
- Production changes, DNS/tunnel changes, payment configuration, credential rotations, trust-root changes, and live releases require separate review and explicit authorization.
- Keep ZQM Computing (geospatial engineering/scientific computing) and ZQM Labs (community-centered games) distinct; cross-link where useful without conflating their product identities.
- Do not archive or delete repositories under this improvement program. Improve in place and make the full portfolio easier to navigate.

## 7. Adoption checklist

For each repository, record:

- [ ] README purpose, audience, maturity, prerequisites, quickstart, validation, and non-claims.
- [ ] Manifest and committed lockfile; supported runtime is documented.
- [ ] One-command environment recreation and example execution path.
- [ ] Focused tests/lint or a documented manual validation procedure.
- [ ] Security/community/license references verified.
- [ ] Index entry and related links checked.
- [ ] Evidence records exact commit, command/workflow, result, date, and limitations.
- [ ] Any unmet item is recorded as a blocker or follow-up, not represented as complete.

## 8. What this standard does not claim

Publishing this standard does not mean all repositories comply, all lockfiles are current, all examples run, all dependencies are audited, or any service is production-ready. Adoption must be measured repository by repository using current evidence.
