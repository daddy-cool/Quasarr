# Contributing

Keep commits focused and easy to review.

## Commit Messages

The dominant pattern in this repository is a **single-line, imperative subject with no body**. Match that style.

### Subject

- Start with a capitalized imperative verb: `Add`, `Fix`, `Use`, `Remove`, `Replace`, `Handle`, `Document`, `Demote`, `Filter`, `Refine`.
- Keep it short enough to scan but broad enough to summarize the actual change. Do not undersell a large or multi-file change with a subject that only names one small part of it.
- When a commit touches several related areas, use a subject that captures the shared theme rather than the most prominent file. Use `and` to join two themes when they truly belong together.
- No trailing period. No emoji from contributors (automated tooling may add `🤖`).
- A trailing `(#123)` reference is fine when the commit closes or follows up a specific PR or issue.

Optional conventional prefixes seen in history:

- `chore:` for maintenance work such as dependency bumps, version bumps, or pre-commit tweaks. Still describe the main maintenance work after the prefix.
- `chore(deps):` for dependency-only updates (often dependabot).
- `fix:` for some bug fixes. Many bug fixes omit the prefix and just start with `Fix`; either is fine, but pick one and keep the subject specific.
- `refactor:` only when the change is genuinely a refactor with no behavior change.

Representative subjects from recent history:

- `Use flaresolverr-go in docs and setup UI`
- `Remove remaining LazyLibrarian mentions`
- `Replace magazine client user agent with Magazarr`
- `Document Magazarr setup`
- `Handle empty season and episode values in release matching`
- `Filter SponsorsHelper packages by advertised URL support (#350)`
- `Add timeout slow-mode controls and harden JDownloader retries`
- `Demote NK redirect resolution noise to debug`
- `fix: harden sqlite locking and maintenance (#365)`
- `fix: support icon-only BY mirror labels`
- `chore: 🤖 upgraded dependencies and increased version to 4.3.8`

### Body

Skip the body unless the subject genuinely cannot carry the change. When you do include one:

- List only the main changes that define the commit. Do not pad the message with supporting details such as follow-up links, ignore-rule tweaks, log handling, or other incidental edits unless those details are the actual point of the commit.
- Keep bullets short and concrete; explain *why* only when it would not be obvious from the diff.
- The PR description, not the commit body, is where you write the user-visible summary and test plan.

## Pull Requests

Pull requests should describe the user-visible change, call out any config or hostname impact, and avoid mixing unrelated cleanup with functional work. For UI or integration changes, include proof of behavior such as screenshots, logs, or a brief reproduction example.

The project README asks contributors to coordinate on Discord before starting large new features to avoid duplicate work. For development environment details, also see the root `CONTRIBUTING.md` and `docs/Development.md`.
