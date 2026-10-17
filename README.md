# ZQM House Template

The ZQM house template provides reusable repository governance and CI defaults
for ZQM Computing and ZQM Labs.

## Included

- Conditional CI for Python, Node.js, and Go projects; tests run only when
  discoverable tests or configured test scripts exist.
- CodeQL that detects supported source languages and skips content-only repos.
- A single Gitleaks secret scan.
- Native dependency audits for declared Python, npm, and Go dependencies.
- Community standards, issue forms, pull-request guidance, and Dependabot.

This template intentionally does not include a generic GitHub Pages deploy:
production sites must define their own deployment target and workflow.

## Quick start

```bash
gh repo create ZQM-Computing/my-new-repo --template ZQM-Labs/zqm-template --public
```

## Related repositories

- [ZQM Computing](https://github.com/ZQM-Computing)
- [ZQM Labs](https://github.com/ZQM-Labs)
- [zqmlabs.com](https://zqmlabs.com)

## License

MIT — see LICENSE.
