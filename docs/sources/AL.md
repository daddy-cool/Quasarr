# AL

Per-source notes for the `AL` integration. For conventions that apply to every source document, see `docs/sources/README.md`; for the rules that govern third-party payload work, see the `Third-Party Source Work` section of `AGENTS.md`.

## Search

- Module: `quasarr/search/sources/al.py`
- Categories: Movies, Shows, Anime Shows
- Style: HTML scrape via BeautifulSoup
- Capabilities: `supports_imdb=True`, `supports_phrase=False`, `supports_absolute_numbering=True`, `requires_login=True`
- Session: `quasarr.providers.sessions.al` (`fetch_via_requests_session`, `invalidate_session`)

## Download

- Module: `quasarr/downloads/sources/al.py`
- Inherits: `AbstractDownloadSource`
- Link protection: handled in `quasarr/downloads/linkcrypters/al.py` (CAPTCHA solving and content decryption); FlareSolverr is required for the download flow.
- CAPTCHA flow: the details page and the initial `/ajax/captcha` (`nocaptcha`) request run on the FlareSolverr browser session to arm the challenge. The CAPTCHA solve (icon fetch + selection submit on `/files/captcha`) and the final `/ajax/captcha` (`captcha`) validation must run on the same `requests.Session`, because AL binds a solved CAPTCHA to the client that solved it — validating from the FlareSolverr browser instead is rejected with `The captcha ID was invalid`. CAPTCHA POST requests include browser-style AJAX headers, and the requests session keeps the current FlareSolverr User-Agent so it stays browser-consistent.

## Notable quirks

- Absolute episode numbering is resolved through `quasarr.providers.xem_metadata.get_season_name`.
- Anime release titles are constructed via `quasarr.downloads.sources.helpers.anime_title.guess_release_title`.
- Search treats a single-hit redirect as an implicit result; redirects are followed before parsing.
- Per-release HTML is cached for a short window via `get_recently_searched` to avoid re-fetching detail pages.
- Multi-episode packs are split per requested episode, with size divided proportionally.
