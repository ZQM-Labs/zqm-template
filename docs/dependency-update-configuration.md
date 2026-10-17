# Dependency update configuration

Dependabot configuration must match manifests that actually exist in this repository. The template intentionally contains no application dependency manifest, so its default `.github/dependabot.yml` enables GitHub Actions updates only. Do not add package ecosystems before the matching manifest exists; Dependabot can report configuration errors for missing manifests.

When a project adds a dependency manifest, add the matching entry to `.github/dependabot.yml` and use the directory containing that manifest:

```yaml
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
  - package-ecosystem: "gomod"
    directory: "/"
    schedule:
      interval: "weekly"
  - package-ecosystem: "nuget"
    directory: "/"
    schedule:
      interval: "weekly"
```

Only include ecosystems that match files committed to the repository (for example, `requirements.txt` or `pyproject.toml` for pip, `package.json` for npm, `go.mod` for Go modules, and a supported .NET project or solution for NuGet). For monorepos, configure each actual manifest directory separately. Keep the schedule aligned with the team's review capacity.
