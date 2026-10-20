# ZQM House Template
<!-- ZQM-START -->
<!-- markdownlint-disable MD033 -->
<p align="center">
  <strong>ZQM Labs — Z's Quests & Mischief</strong><br>
  <a href="https://zqmlabs.com">zqmlabs.com</a> •
  <a href="https://github.com/ZQM-Labs">GitHub</a>
</p>
<!-- markdownlint-enable MD033 -->
<!-- ZQM-END -->

The ZQM house template provides reusable repository governance and CI defaults
for ZQM Computing and ZQM Labs.

## Included

- Conditional CI for Python, Node.js, and Go projects; tests run only when
  discoverable tests or configured test scripts exist.
- CodeQL that detects supported source languages and skips content-only repos.
- A single Gitleaks secret scan.
- Native dependency audits for declared Python, npm, and Go dependencies.
- Community standards, issue forms, pull-request guidance, and Dependabot.
- Brand and README conventions in [docs/BRAND-AND-README.md](docs/BRAND-AND-README.md).
- Service, data, release and recovery gates in [docs/CONTINUITY-BASELINE.md](docs/CONTINUITY-BASELINE.md).

This template intentionally does not include a generic GitHub Pages deploy:
production sites must define their own deployment target and workflow.

It also intentionally excludes generic payment or fulfillment automation. A product
repository must implement and review its own payment-provider webhook, verify payment
state server-side, enforce idempotency, and deliver downloads through an authorized
private path. Do not use issue labels or issue comments as proof of payment, and do
not add a fulfillment workflow until its end-to-end path has been tested in the
provider's test mode.

## Quick start

```bash
gh repo create ZQM-Computing/my-new-repo --template ZQM-Labs/zqm-template --public
```

## Related repositories

- [ZQM Computing](https://github.com/ZQM-Computing)
- [ZQM Labs](https://github.com/ZQM-Labs)
- [zqmlabs.com](https://zqmlabs.com)

## Installation

```bash
pip install -e .
```

Requires Python 3.11+.

## License

MIT — see LICENSE.

## Validation

The CI workflow runs `python scripts/check_docs.py` to check the root README,
relative Markdown links, hard-coded repository counts, and workflow badge
identity. Run the same check locally before opening a pull request:

```bash
python scripts/check_docs.py
```

The optional `.zqm-repo.yml` manifest records the canonical GitHub slug, display name, and any intentional aliases; CI checks it against the actual repository and README title. Update that manifest when creating a repository from this template.

The checker uses only the Python standard library. It does not fetch external
URLs or prove that external services are live; review deployment and external
links separately when they are operationally important.
