# ZQM House Template

The ZQM house template — .github boilerplate, CI, gitleaks, and community standards every new ZQM repo starts from.

## Who this is for

ZQM Computing and ZQM Labs maintainers creating new repositories. This template ensures every repo starts with consistent governance, CI, and security scanning.

## What's inside

```
.github/
  workflows/
    ci.yml              # Python lint + test
    security-scan.yml   # CodeQL analysis
  ISSUE_TEMPLATE/
    bug_report.yml
    feature_request.yml
  PULL_REQUEST_TEMPLATE.md
  CODE_OF_CONDUCT.md
  SECURITY.md
  dependabot.yml
```

## Quick start

```bash
# Create a new repo from this template
gh repo create ZQM-Computing/my-new-repo --template ZQM-Computing/zqm-template --public

# Or clone and customize
gh repo clone ZQM-Computing/zqm-template my-new-repo
```

## What you get

| Feature | Status |
|---|---|
| CI workflow | Automated |
| Security scanning | Automated |
| Dependabot | Enabled |
| Issue templates | Bug + Feature |
| PR template | Standard |
| Code of conduct | Contributor Covenant |
| Security policy | Vulnerability reporting |

## Related repositories

- [ZQM Computing](https://github.com/ZQM-Computing) — geospatial arm of ZQM Labs
- [ZQM Labs](https://github.com/ZQM-Labs) — games studio
- [geospatial-patterns](https://github.com/ZQM-Computing/geospatial-patterns) — umbrella index

## License

MIT — see LICENSE file.

*Part of [ZQM Labs](https://github.com/ZQM-Labs) — games, gear & a little mischief.*
