# FX

Per-source notes for the `FX` integration. For conventions, see `docs/sources/README.md`; for third-party payload rules, see the `Third-Party Source Work` section of `AGENTS.md`.

## Search

- Module: `quasarr/search/sources/fx.py`
- Categories: Movies, Shows
- Style: HTML scrape via BeautifulSoup over articles that expose multiple protected links per release
- Capabilities: `supports_imdb=True`, `supports_phrase=False`, `requires_login=False`
- Session: plain `requests`

## Download

- Module: none — FX has no per-source download module; the search emits filecrypt links and downloads flow through Quasarr's central link processor (`quasarr/downloads/__init__.py`) plus the shared filecrypt linkcrypter (`quasarr/downloads/linkcrypters/filecrypt.py`).
- Link protection: filecrypt-style links, resolved by the shared linkcrypter pipeline

## Notable quirks

- The default password is derived from a fixed portion of the configured hostname.
- Each article emits multiple download blocks; they are iterated by index, not by container.
- Size is read from a tagged inline element near the article body.
