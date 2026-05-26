# SF

Per-source notes for the `SF` integration. For conventions, see `docs/sources/README.md`; for third-party payload rules, see the `Third-Party Source Work` section of `AGENTS.md`.

## Search

- Module: `quasarr/search/sources/sf.py`
- Categories: Shows, Anime Shows
- Style: HTML scrape via BeautifulSoup for the feed; two API calls for search (series lookup, then season HTML)
- Capabilities: `supports_imdb=True`, `supports_phrase=False`, `requires_login=False`
- Session: plain `requests`

## Download

- Module: `quasarr/downloads/sources/sf.py`
- Inherits: `AbstractDownloadSource`
- Link protection: none — direct links

## Notable quirks

- The feed covers a rolling two-day window; older entries are not surfaced.
- Mirrors expose short host codes that the module maps to full hoster names through a local lookup table.
- Season-pack size is divided evenly across episodes when emitting per-episode releases.
- HTML responses for search are cached briefly via `get_recently_searched` to avoid duplicate fetches inside a single query.
