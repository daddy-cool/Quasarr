# DL

Per-source notes for the `DL` integration. For conventions, see `docs/sources/README.md`; for third-party payload rules, see the `Third-Party Source Work` section of `AGENTS.md`.

## Search

- Module: `quasarr/search/sources/dl.py`
- Categories: Movies, Shows, Music, Books
- Style: HTML scrape via BeautifulSoup over a forum-style layout, with per-category forums
- Capabilities: `supports_imdb=True`, `supports_phrase=True`, `requires_login=True`
- Session: `quasarr.providers.sessions.dl` (login plus session-validation logic; umlauts are normalised when constructing queries)

## Download

- Module: `quasarr/downloads/sources/dl.py`
- Inherits: `AbstractDownloadSource`
- Link protection: none — links are read directly from forum posts

## Notable quirks

- Paginated search is sequential and bounded by a wall-clock budget; pagination stops as soon as a page yields no results.
- Yearly magazine threads ("Jahresthema") are expanded into per-issue entries; this requires the current year to be present in the thread.
- Magazine titles use a token-normalised matcher so that month/issue variants align across feed and search.
