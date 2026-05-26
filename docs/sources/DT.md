# DT

Per-source notes for the `DT` integration. For conventions, see `docs/sources/README.md`; for third-party payload rules, see the `Third-Party Source Work` section of `AGENTS.md`.

## Search

- Module: `quasarr/search/sources/dt.py`
- Categories: Movies, Shows, Music, Books
- Style: HTML scrape via BeautifulSoup over article pages
- Capabilities: `supports_imdb=True`, `supports_phrase=True`, `requires_login=False`
- Session: plain `requests`

## Download

- Module: `quasarr/downloads/sources/dt.py`
- Inherits: `AbstractDownloadSource`
- Link protection: none — direct links

## Notable quirks

- Article date parsing assumes a fixed timezone offset; non-matching timezones may produce slightly off timestamps.
- Article HTML is parsed for the IMDb identifier, which is propagated onto search results when present.
- Search drops candidates that do not match the requested resolution and codec; the feed accepts whatever the article exposes.
