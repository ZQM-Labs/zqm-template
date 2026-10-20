# Repository Continuity Baseline

Use this checklist when creating or maintaining a repository from the ZQM house template. Adapt it to the repository's actual technology and data; do not copy irrelevant services or assume every repository needs a deployment pipeline.

## 1. Classify the repository

Record:

- Purpose and maintainers.
- Public/private/internal classification and data owner.
- Runtime, supported versions, dependency manager and lockfile policy.
- Whether it deploys a service, generates artifacts, stores state, or is documentation-only.
- External dependencies, secrets, domains, accounts and failure domains.
- Whether a local machine/network is a production dependency.

Never put credentials, personal data, paid content, answer keys, customer/participant data, or restricted internal datasets in public repositories, workflows, artifacts or Pages output.

## 2. Reproducible local operation

- Document a clean setup from a fresh clone.
- Pin application dependencies or commit the appropriate lockfile.
- Provide one local command for lint/test/build where practical.
- Make checks fail on missing required inputs; do not report a skipped/no-op check as a pass.
- Keep local validation possible when hosted CI is unavailable or minutes are constrained.
- State exactly which tests need external services, credentials, GPUs, or special hardware.

## 3. Workflow and supply-chain safety

- Set least-privilege workflow permissions explicitly.
- Add job timeouts and concurrency where appropriate.
- Avoid broad write tokens, secret exposure to untrusted pull requests, and unnecessary scheduled jobs.
- Pin third-party actions to reviewed immutable revisions where policy/tooling supports it.
- Keep dependency updates reviewable; assess major-version compatibility rather than merging solely because a bot opened a PR.
- Use secret scanning and rotate any credential that was exposed; deleting it from the latest commit is not sufficient.
- Do not put payment, release, deployment, or destructive system operations into generic workflows without explicit opt-in and repository-specific validation.

## 4. Service continuity (only if the repository deploys a service)

Document:

- Production origin, hosting model and canonical source/release branch.
- Health/readiness checks and external smoke tests.
- Configuration and secret names/owners (never secret values).
- Last-known-good release identifier and rollback command.
- Database/schema compatibility and separate data restore procedure.
- Provider outage behavior and manual fallback.
- Monitoring/alerting owner and incident contact path.

Do not treat multiple connectors to one host as host availability. A local origin still fails with local power, router, ISP, host or disk.

## 5. Data backup and recovery (if the repository owns state or important artifacts)

- Define RTO/RPO based on actual business impact; mark targets as proposed until measured.
- Back up data and associated uploaded/object files together.
- Keep encrypted backups in an independent failure domain with separate credentials.
- Retain an immutable/offline copy where practical.
- Monitor missing/failed backups and retention.
- Test restore into a clean environment; a successful backup job alone is not proof of recovery.
- Document data export and provider-exit path.

## 6. Release and rollback

- Build from immutable commit/release identifiers, not a moving branch.
- Validate a preview or staging target before production.
- Record source SHA, artifact/version, deploy ID, test evidence and rollback target.
- Keep production deploy separate from merge where failure impact warrants it.
- Treat database migrations, external services and paid fulfilment as separate rollback/recovery concerns.
- Do not claim production readiness from a static check or preview build alone.

## 7. Public repository release gate

Before publishing:

- Scan tracked files, generated site output, fixtures and artifacts for secrets/private data.
- Verify links and examples without including proprietary customer data.
- Confirm license and attribution.
- Review internal hostnames and service endpoints.
- Confirm Project Volusia and other restricted internal material are excluded.
- For game/content repositories, confirm private answer keys and paid kit content are excluded from public artifacts.
- Record any known limitations and unrun tests.

## 8. Minimum evidence in a pull request

Every operational change should state:

1. What changed and why.
2. What was tested, with exact commands/results.
3. What was not tested and why.
4. Whether hosted CI was run.
5. Whether production configuration changed (default: no).
6. Rollback/recovery implications.
7. Remaining risks and the next gate.

A repository is only marked upgraded after its actual contents are inspected, the checks are appropriate to its technology, and unresolved risks are tracked. Archived repositories stay inventory-only unless explicitly selected for maintenance.
