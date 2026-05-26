# SL

Per-source notes for the `SL` integration. For conventions, see `docs/sources/README.md`; for third-party payload rules, see the `Third-Party Source Work` section of `AGENTS.md`.

## Search

- Module: `quasarr/search/sources/sl.py`
- Categories: Books, Movies, Shows, Anime Shows, Audio
- Style: RSS feed parsed with `xml.etree`; HTML scrape via BeautifulSoup for search, with parallel fetches across category sections
- Capabilities: `supports_imdb=True`, `supports_phrase=True`, `requires_login=False`
- Session: shared `ensure_session_cf_bypassed` wrapper that keeps a Cloudflare-cleared session ready

## Download

- Module: `quasarr/downloads/sources/sl.py`
- Inherits: `AbstractDownloadSource`
- Link protection: none — direct links

## Notable quirks

- Cloudflare clearance is required for every fetch; failures fall back through the bypass helper.
- Results are deduplicated by source link, since shows can surface through more than one category section.
- Size and IMDb identifier are extracted from the RSS description, not from a structured field.
