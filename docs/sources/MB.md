# MB

Per-source notes for the `MB` integration. For conventions, see `docs/sources/README.md`; for third-party payload rules, see the `Third-Party Source Work` section of `AGENTS.md`.

## Search

- Module: `quasarr/search/sources/mb.py`
- Categories: Movies, Shows
- Style: HTML scrape via BeautifulSoup over forum-style posts
- Capabilities: `supports_imdb=True`, `supports_phrase=False`, `requires_login=False`
- Session: plain `requests`

## Download

- Module: `quasarr/downloads/sources/mb.py`
- Inherits: `AbstractDownloadSource`
- Link protection: none — direct links

## Notable quirks

- IMDb-only: a phrase query is converted to an IMDb ID lookup first.
- German month-name parsing is driven by a local `MONTHS_MAP`; new variants must be added there.
- Search drops candidates that do not match the requested resolution and codec; feed entries are kept as posted.
