# SJ

Per-source notes for the `SJ` integration. For conventions, see `docs/sources/README.md`; for third-party payload rules, see the `Third-Party Source Work` section of `AGENTS.md`.

## Search

- Module: `quasarr/search/sources/sj.py`
- Categories: Shows, Anime Shows
- Style: JSON API
- Capabilities: `supports_imdb=True`, `supports_phrase=False`, `requires_login=True`
- Session: plain `requests`, authenticated against the API

## Download

- Module: `quasarr/downloads/sources/sj.py`
- Inherits: `AbstractDownloadSource`
- Link protection: the site itself acts as a protected crypter — the download module checks mirrors via `helpers.junkies._release_matches_requested_mirrors` and returns the URL tagged as `"junkies"`, which routes it through Quasarr's userscript CAPTCHA flow

## Notable quirks

- The feed walks recent date-window pages and stops as soon as one returns results.
- IMDb-only: phrase queries return empty.
- Releases are aggregated per season block from the API response.
- ISO-8601 timestamps are normalised into RFC dates before emission.
