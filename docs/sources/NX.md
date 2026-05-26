# NX

Per-source notes for the `NX` integration. For conventions, see `docs/sources/README.md`; for third-party payload rules, see the `Third-Party Source Work` section of `AGENTS.md`.

## Search

- Module: `quasarr/search/sources/nx.py`
- Categories: Books, Movies, Shows, Audio
- Style: JSON API with paginated category listings
- Capabilities: `supports_imdb=True`, `supports_phrase=True`, `requires_login=True`
- Session: plain `requests`, authenticated against the API

## Download

- Module: `quasarr/downloads/sources/nx.py`
- Inherits: `AbstractDownloadSource`
- Link protection: none — API-backed flow

## Notable quirks

- Internal type tokens map to Quasarr categories (e.g. ebook, movie, episode, audio); changes to that mapping must stay in lockstep with the API.
- Book entries are normalised through the Magazarr title helper.
- A mismatched IMDb ID on the API response causes the result to be dropped.
