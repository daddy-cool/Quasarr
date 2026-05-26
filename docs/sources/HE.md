# HE

Per-source notes for the `HE` integration. For conventions, see `docs/sources/README.md`; for third-party payload rules, see the `Third-Party Source Work` section of `AGENTS.md`.

## Search

- Module: `quasarr/search/sources/he.py`
- Categories: Movies, Shows, Anime Shows
- Style: HTML scrape via BeautifulSoup; feed and search share the same code path (feed is the empty-query case)
- Capabilities: `supports_imdb=True`, `supports_phrase=False`, `requires_login=False`
- Session: plain `requests`

## Download

- Module: `quasarr/downloads/sources/he.py`
- Inherits: `AbstractDownloadSource`
- Link protection: none — direct links, with a FlareSolverr fallback if the standard fetch is challenged

## Notable quirks

- IMDb-only: non-IMDb input returns an empty result set.
- Relative posting timestamps ("X minutes ago" and German variants) are normalised into RFC dates.
- Mirrors are filtered by normalised hostname against the configured mirror list.
