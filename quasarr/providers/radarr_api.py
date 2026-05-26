# -*- coding: utf-8 -*-
# Quasarr
# Project by https://github.com/rix1337

import requests

from quasarr.providers.log import error, trace, warn

_SHARED_STATE_KEY = "radarr_client"


def get_client(shared_state):
    """Return the cached Radarr client, or None when Radarr is not configured."""
    return shared_state.values.get(_SHARED_STATE_KEY)


def set_client(shared_state, client):
    """Store the Radarr client in shared state (pass None to clear)."""
    shared_state.update(_SHARED_STATE_KEY, client)


class RadarrAPIClient:
    """Minimal client for the Radarr v3 HTTP API.

    See https://radarr.video/docs/api/ for the full specification.
    """

    def __init__(self, base_url, api_key, timeout=10):
        if not base_url:
            raise ValueError("base_url is required")
        if not api_key:
            raise ValueError("api_key is required")
        self._base_url = base_url.rstrip("/")
        self._api_key = api_key
        self._timeout = timeout

    def _get(self, path, params=None):
        url = f"{self._base_url}/api/v3{path}"
        headers = {
            "X-Api-Key": self._api_key,
            "Accept": "application/json",
        }
        try:
            response = requests.get(
                url, headers=headers, params=params, timeout=self._timeout
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            warn(f"Radarr API request to {url} failed: {e}")
            return None

    def movie_lookup_imdb(self, imdb_id):
        """Look up a movie on Radarr by its IMDb ID.

        Returns the parsed JSON movie object, or None when the request fails
        or Radarr cannot resolve the IMDb ID.
        """
        if not imdb_id:
            return None
        return self._get("/movie/lookup/imdb", params={"imdbId": imdb_id})


def get_tmdb_id(shared_state, imdb_id):
    """Return the tmdbId Radarr resolves for the given IMDb ID, or None."""
    client = get_client(shared_state)
    if client is None:
        error("Radarr metadata lookup skipped: Radarr is not configured")
        return None

    movie = client.movie_lookup_imdb(imdb_id)
    if not movie:
        return None

    tmdb_id = movie.get("tmdbId")
    if not tmdb_id:
        warn(f"Radarr response for {imdb_id} did not include a TMDB ID")
        return None

    trace(f"Resolved IMDb ID '{imdb_id}' to TMDB ID '{tmdb_id}'")

    return tmdb_id
