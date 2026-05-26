# WX

Per-source notes for the `WX` integration. For conventions, see `docs/sources/README.md`; for third-party payload rules, see the `Third-Party Source Work` section of `AGENTS.md`.

## Search

- Module: `quasarr/search/sources/wx.py`
- Categories: Movies, Shows, Anime Shows
- Style: RSS/Atom hybrid feed; JSON API for search
- Capabilities: `supports_imdb=True`, `supports_phrase=False`, `requires_login=False`
- Session: plain `requests`

## Download

- Module: `quasarr/downloads/sources/wx.py`
- Inherits: `AbstractDownloadSource`
- Link protection: none — direct links; detail and release endpoints are queried for full metadata

## Notable quirks

- The feed parser detects whether the payload is RSS or Atom and adapts; the default password is derived from the configured hostname in upper case.
- Search filters API results by an internal type token (movie / series / anime) to match the requested category.
- Releases are deduplicated by full title; mirrors come from the per-release block.
- IMDb mismatches between the query and the release are dropped; the release's own IMDb identifier is preferred when the query did not supply one.
