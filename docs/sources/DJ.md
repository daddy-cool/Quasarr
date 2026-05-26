# DJ

Per-source notes for the `DJ` integration. For conventions, see `docs/sources/README.md`; for third-party payload rules, see the `Third-Party Source Work` section of `AGENTS.md`.

## Search

- Module: `quasarr/search/sources/dj.py`
- Categories: Shows
- Style: JSON API for the feed; HTML scrape plus a JSON release endpoint for search
- Capabilities: `supports_imdb=True`, `supports_phrase=False`, `requires_login=True`
- Session: plain `requests`

## Download

- Module: `quasarr/downloads/sources/dj.py`
- Inherits: `AbstractDownloadSource`
- Link protection: the site itself acts as a protected crypter — the download module checks mirrors via `helpers.junkies._release_matches_requested_mirrors` and returns the URL tagged as `"junkies"`, which routes it through Quasarr's userscript CAPTCHA flow

## Notable quirks

- Search requires an IMDb ID; phrase searches return empty.
- Series discovery is HTML-scraped to locate a media identifier, then releases are fetched via JSON.
- Releases are aggregated per season block from the JSON response.
