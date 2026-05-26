# RM

Per-source notes for the `RM` integration. For conventions, see `docs/sources/README.md`; for third-party payload rules, see the `Third-Party Source Work` section of `AGENTS.md`.

## Search

- Module: `quasarr/search/sources/rm.py`
- Categories: Movies, Shows
- Style: HTML scrape via BeautifulSoup, plus an API call to enumerate releases for a production
- Capabilities: `supports_imdb=True`, `supports_phrase=True`, `requires_login=False`
- Session: `quasarr.providers.sessions.rm` (a bootstrapped session is required before requests succeed)

## Download

- Module: `quasarr/downloads/sources/rm.py`
- Inherits: `AbstractDownloadSource`
- Link protection: none — direct links

## Notable quirks

- The data model is production-centred: the feed and search find productions first, then fetch each production's releases.
- Search performs multiple match variants on the requested title (full name, leading words, trailing words, year-stripped) to absorb minor naming differences.
- Title normalisation strips leading tags and replaces spaces with dots before emitting results.
- Feed walks up to a fixed number of production pages so cold-start fetches do not run unbounded.
