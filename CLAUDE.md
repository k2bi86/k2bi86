# CLAUDE.md

This file provides guidance for AI assistants working in this repository.

## Repository Overview

This is a **GitHub profile repository** (`k2bi86/k2bi86`). GitHub automatically displays the `README.md` from a repository matching the owner's username as the profile biography on their GitHub profile page.

**Repository contents:**
- `README.md` — the GitHub profile page content (Markdown only)
- `CLAUDE.md` — this file; guidance for AI assistants

There is no application code, build system, or test suite.

### Current State of README.md

The `README.md` currently contains the default GitHub profile template placeholder text and has not yet been customized. When asked to update the profile, replace or build upon this template content with real information about the repository owner.

## Repository Structure

```
k2bi86/k2bi86/
├── README.md     # GitHub profile page (rendered on github.com/k2bi86)
└── CLAUDE.md     # AI assistant guidance (this file)
```

No subdirectories, build artifacts, configuration files, lock files, or source code exist in this repository.

## Development Workflow

### Branching

- The default branch is `main`.
- Feature branches use the naming convention `claude/short-description-{UUID}` (e.g. `claude/add-claude-documentation-FpJZv`).
- Develop all changes on a designated feature branch and push before opening a PR.
- **Never push directly to `main`.**

### Making Changes

Since this is a Markdown-only repository, all meaningful changes are edits to `README.md` (or, when updating AI guidance, to `CLAUDE.md`).

```bash
# Stage and commit changes
git add README.md
git commit -m "Descriptive commit message in imperative mood"

# Push to the feature branch
git push -u origin <branch-name>
```

### Commit Message Conventions

- Use imperative mood: `Update README.md`, `Add skills section`, `Fix broken link`
- Keep messages short and descriptive (no longer than ~72 characters)
- No ticket or issue references are required for this repo

### Typical Workflow for Profile Updates

1. Ensure you are on the correct feature branch (check `git branch`).
2. Read the current `README.md` before making edits.
3. Make targeted edits using the `Edit` tool; prefer editing over full rewrites unless the content is being completely replaced.
4. Stage and commit with a clear message.
5. Push to the remote feature branch.

## Key Conventions

- **Markdown style:** Standard GitHub-Flavored Markdown (GFM). Emoji (e.g. ✨, 🔭) are acceptable and common in profile READMEs.
- **Content tone:** Personal, concise, and up-to-date. This is a public-facing profile — write for a technical audience visiting the owner's GitHub page.
- **No build steps:** There is nothing to install, build, lint, or test. Do not create `package.json`, `Makefile`, CI configs, or similar files.
- **No extra files:** Do not create additional files beyond `README.md` and `CLAUDE.md` unless explicitly requested.
- **Single author:** All commits in this repository have been by `k2bi86`.

## Remote Configuration

The git remote (`origin`) is proxied locally during automated sessions:

```
http://local_proxy@127.0.0.1:39991/git/k2bi86/k2bi86
```

This is normal in the Claude Code web environment — treat it like a standard GitHub remote. Use `git push -u origin <branch-name>` as normal.

## Git History Summary

| Commit | Description |
|--------|-------------|
| Initial commit | Repository created with default template |
| Update README.md | Minor update to README content |
| Add CLAUDE.md | First version of AI assistant guidance |
| Merge PR #1 | Merged `claude/add-claude-documentation-uCX9f` into `main` |

## Notes for AI Assistants

- Always read `README.md` before proposing or making edits to it.
- When updating this `CLAUDE.md`, reflect the actual current state of the repository — do not describe features or files that do not exist.
- The repository owner's GitHub username is `k2bi86`. Refer to them by username when needed.
- Do not add CI/CD pipelines, GitHub Actions workflows, or any automation configuration — this repo intentionally has none.
- Do not speculate about what the profile "should" contain; only make changes explicitly requested by the user.
