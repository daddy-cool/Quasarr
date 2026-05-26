# AT

Per-source notes for the `AT` integration. For conventions, see `docs/sources/README.md`; for third-party payload rules, see the `Third-Party Source Work` section of `AGENTS.md`.

## Search

- Module: `quasarr/search/sources/at.py`
- Categories: Movies, Shows, Anime Shows
- Style: HTML scrape via BeautifulSoup, with parallel fetches of listing and attachment pages
- Capabilities: `supports_imdb=True`, `supports_phrase=True`, `supports_absolute_numbering=True`, `requires_login=False`
- Session: plain `requests.Session`; concurrent page fetches use `concurrent.futures.ThreadPoolExecutor`

## Download

- Module: `quasarr/downloads/sources/at.py`
- Inherits: `AbstractDownloadSource`
- Link protection: none — direct links resolved against requested mirrors

## Notable quirks

- Listing and attachments pages are fetched in parallel to keep latency low on multi-page series.
- Anime release titles use `helpers.anime_title.guess_release_title`; subtitle language tokens are injected when detected in attachment names.
- German season name resolution runs through `xem_metadata.get_season_name`.
