# CLAUDE.md

This file provides guidance for AI assistants working in this repository.

## Repository Overview

This is a **GitHub profile repository** (`k2bi86/k2bi86`). GitHub automatically displays the `README.md` from a repository matching the owner's username as the profile biography on their GitHub profile page.

**Repository contents:**
- `README.md` — the GitHub profile page content (Markdown only)

There is no application code, build system, or test suite.

## Development Workflow

### Branching

- The default branch is `main`.
- Feature branches use the naming convention `claude/short-description-{UUID}` (e.g. `claude/add-claude-documentation-uCX9f`).
- Develop all changes on a designated feature branch and push before opening a PR.

### Making Changes

Since this is a Markdown-only repository, all meaningful changes are edits to `README.md`.

```bash
# Stage and commit changes
git add README.md
git commit -m "Descriptive commit message in imperative mood"

# Push to the feature branch
git push -u origin <branch-name>
```

### Commit Message Conventions

- Use imperative mood: `Update README.md`, `Add skills section`, `Fix broken link`
- Keep messages short and descriptive
- No ticket or issue references are required for this repo

## Key Conventions

- **Markdown style:** Standard GitHub-Flavored Markdown (GFM) with emoji support is fine
- **Content:** The README is the profile page — keep it personal, concise, and up-to-date
- **No build steps:** There is nothing to install, build, lint, or test
- **Single author:** All commits have been by `k2bi86`

## Remote Configuration

The git remote (`origin`) is proxied locally during automated sessions:

```
http://local_proxy@127.0.0.1:39991/git/k2bi86/k2bi86
```

This is normal in the Claude Code web environment — treat it like a standard GitHub remote.
