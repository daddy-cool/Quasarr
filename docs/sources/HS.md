# HS

Per-source notes for the `HS` integration. For conventions, see `docs/sources/README.md`; for third-party payload rules, see the `Third-Party Source Work` section of `AGENTS.md`.

## Search

- Module: `quasarr/search/sources/hs.py`
- Categories: Movies, Shows
- Style: RSS feed parsed with BeautifulSoup's `html.parser` (lxml is intentionally avoided); search resolves by IMDb ID
- Capabilities: `supports_imdb=True`, `supports_phrase=False`, `requires_login=False`
- Session: plain `requests`

## Download

- Module: `quasarr/downloads/sources/hs.py`
- Inherits: `AbstractDownloadSource`
- Link protection: none — direct links

## Notable quirks

- IMDb-only: phrase queries return empty.
- Per-episode size is derived from the season-pack bitrate multiplied by parsed episode duration; if no figure can be computed the season-pack size is used as a fallback.
- Episode metadata is extracted from article text using a regex constant inside the module.
