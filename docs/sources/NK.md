# NK

Per-source notes for the `NK` integration. For conventions, see `docs/sources/README.md`; for third-party payload rules, see the `Third-Party Source Work` section of `AGENTS.md`.

## Search

- Module: `quasarr/search/sources/nk.py`
- Categories: Movies, Shows
- Style: HTML scrape via BeautifulSoup; search uses a POST with form-encoded body
- Capabilities: `supports_imdb=True`, `supports_phrase=False`, `requires_login=False`
- Session: plain `requests`

## Download

- Module: `quasarr/downloads/sources/nk.py`
- Inherits: `AbstractDownloadSource`
- Link protection: none — direct links

## Notable quirks

- IMDb input is first converted to a localised German title via `imdb_metadata.get_localized_title` before being submitted as the search term.
- Default passwords are read from a labelled element in the mirrors paragraph when present.
- Season-pack size is unknown and is reported as zero so consumers can compute per-episode estimates upstream.
- Multiple date and time formats are accepted; new ones must be added to the local parser.
