# BY

Per-source notes for the `BY` integration. For conventions, see `docs/sources/README.md`; for third-party payload rules, see the `Third-Party Source Work` section of `AGENTS.md`.

## Search

- Module: `quasarr/search/sources/by.py`
- Categories: Books, Movies, Shows, Audio
- Style: HTML scrape via BeautifulSoup
- Capabilities: `supports_imdb=True`, `supports_phrase=True`, `requires_login=False`
- Session: plain `requests`

## Download

- Module: `quasarr/downloads/sources/by.py`
- Inherits: `AbstractDownloadSource`
- Link protection: none — the download module fetches direct links from the post and applies its own per-hostname mirror filter

## Notable quirks

- Book/magazine titles run through Magazarr-compatible date and issue normalization before being emitted.
- Search results that lack a valid resolution or codec are dropped; feed results keep their original metadata.
- Per-category fetches use category IDs that are defined as constants inside the search module; treat those constants as the source of truth, not example payloads.
