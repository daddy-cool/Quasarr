# DD

Per-source notes for the `DD` integration. For conventions, see `docs/sources/README.md`; for third-party payload rules, see the `Third-Party Source Work` section of `AGENTS.md`.

## Search

- Module: `quasarr/search/sources/dd.py`
- Categories: Movies, Shows, Anime Shows
- Style: JSON API with paginated result sets
- Capabilities: `supports_imdb=True`, `supports_phrase=False`, `requires_login=True`
- Session: `quasarr.providers.sessions.dd` — login plus a quality-profile filter applied to API responses

## Download

- Module: `quasarr/downloads/sources/dd.py`
- Inherits: `AbstractDownloadSource`
- Link protection: none — the download module queries the DD API and applies its own hostname-based mirror filter

## Notable quirks

- The search module enforces an IMDb-ID match between the request and the API response and discards mismatches.
- Suspected fake releases cause the cached session to be invalidated so the next request re-authenticates.
- Quality filtering is driven by a fixed list of profiles inside the session module; new resolutions must be added there.
