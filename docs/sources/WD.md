# WD

Per-source notes for the `WD` integration. For conventions, see `docs/sources/README.md`; for third-party payload rules, see the `Third-Party Source Work` section of `AGENTS.md`.

## Search

- Module: `quasarr/search/sources/wd.py`
- Categories: Books, Movies, Shows, Audio
- Style: HTML scrape via BeautifulSoup over a table-based layout
- Capabilities: `supports_imdb=True`, `supports_phrase=True`, `requires_login=False`
- Session: plain `requests`, with a FlareSolverr fallback triggered by `is_cloudflare_challenge` detection

## Download

- Module: `quasarr/downloads/sources/wd.py`
- Inherits: `AbstractDownloadSource`
- Link protection: none — direct links

## Notable quirks

- Adult-tagged entries are excluded unless the requesting query explicitly targets them.
- Video categories enforce a resolution and codec check on search results; the feed accepts whatever the listing exposes.
- Special characters in queries are percent-encoded before being submitted.
