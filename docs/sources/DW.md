# DW

Per-source notes for the `DW` integration. For conventions, see `docs/sources/README.md`; for third-party payload rules, see the `Third-Party Source Work` section of `AGENTS.md`.

## Search

- Module: `quasarr/search/sources/dw.py`
- Categories: Movies, Shows
- Style: HTML scrape via BeautifulSoup
- Capabilities: `supports_imdb=True`, `supports_phrase=False`, `requires_login=False`
- Session: plain `requests`

## Download

- Module: `quasarr/downloads/sources/dw.py`
- Inherits: `AbstractDownloadSource`
- Link protection: none — direct links

## Notable quirks

- German month names are mapped to numeric months for date parsing; new variants must be added to the local mapping.
- The IMDb identifier is read from the article HTML and used to validate that the result still matches the request.
