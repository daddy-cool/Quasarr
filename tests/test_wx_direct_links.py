import unittest
from unittest.mock import patch

from quasarr.downloads.sources.wx import Source


class SharedState:
    def __init__(self):
        self.values = {"user_agent": "UA/1.0", "config": self.config}

    def config(self, section):
        if section == "Hostnames":
            return {"wx": "source.invalid"}
        return {}


class FakeResponse:
    def __init__(self, json_data=None, status_code=200):
        self._json = json_data or {}
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise AssertionError(f"HTTP {self.status_code}")

    def json(self):
        return self._json


def _api_payload(releases):
    return {"item": {"releases": releases}}


def _release(fulltitle, links, crypted):
    return {
        "fulltitle": fulltitle,
        "links": links,
        "crypted_links": crypted,
        "options": {"check": {}},
    }


class WxDirectLinksTests(unittest.TestCase):
    URL = "https://www.source.invalid/detail/ABC123/Some-Movie"
    TITLE = "Some.Movie.2024.German.1080p.WEB.H264-GRP"

    def _run(self, releases, head_status_by_url=None, mirrors=None):
        head_status_by_url = head_status_by_url or {}

        def fake_session_get(url, **kwargs):
            if "/start/d/" in url:
                return FakeResponse(_api_payload(releases))
            return FakeResponse({})  # initial page load

        def fake_head(url, **kwargs):
            return FakeResponse(status_code=head_status_by_url.get(url, 200))

        with (
            patch("quasarr.downloads.sources.wx.requests.Session") as session_cls,
            patch("quasarr.downloads.sources.wx.requests.head", fake_head),
        ):
            session = session_cls.return_value
            session.get.side_effect = fake_session_get
            return Source().get_download_links(
                SharedState(), self.URL, mirrors or [], self.TITLE, ""
            )

    def test_prefers_direct_links_over_filecrypt(self):
        releases = [
            _release(
                self.TITLE,
                {
                    "ddownload.com": [
                        "https://ddownload.com/a",
                        "https://ddownload.com/b",
                    ],
                    "rapidgator.net": ["https://rapidgator.net/file/c"],
                },
                {
                    "ddownload.com": "https://filecrypt.cc/Container/AAA.html",
                    "rapidgator.net": "https://filecrypt.cc/Container/BBB.html",
                },
            )
        ]
        result = self._run(releases)
        urls = [link[0] for link in result["links"]]
        # All direct hoster links returned; no filecrypt container leaks through.
        self.assertEqual(
            urls,
            [
                "https://ddownload.com/a",
                "https://ddownload.com/b",
                "https://rapidgator.net/file/c",
            ],
        )
        self.assertFalse(any("filecrypt" in u for u in urls))

    def test_filecrypt_only_release_still_yields_direct_links(self):
        # No hide.cx mirror anywhere; crypted is filecrypt-only. Direct links
        # must still be used instead of failing into the CAPTCHA path.
        releases = [
            _release(
                self.TITLE,
                {"rapidgator.net": ["https://rapidgator.net/file/x"]},
                {"rapidgator.net": "https://filecrypt.cc/Container/ZZZ.html"},
            )
        ]
        result = self._run(releases)
        self.assertEqual(
            [link[0] for link in result["links"]],
            ["https://rapidgator.net/file/x"],
        )

    def test_offline_hoster_is_dropped_but_online_kept(self):
        releases = [
            _release(
                self.TITLE,
                {
                    "ddownload.com": ["https://ddownload.com/live"],
                    "nitroflare.com": ["https://nitroflare.com/dead"],
                },
                {},
            )
        ]
        result = self._run(
            releases, head_status_by_url={"https://nitroflare.com/dead": 404}
        )
        urls = [link[0] for link in result["links"]]
        self.assertIn("https://ddownload.com/live", urls)
        self.assertNotIn("https://nitroflare.com/dead", urls)

    def test_best_mirror_with_most_online_hosters_wins(self):
        releases = [
            _release(
                self.TITLE,
                {"ddownload.com": ["https://ddownload.com/m1"]},
                {},
            ),
            _release(
                self.TITLE,
                {
                    "ddownload.com": ["https://ddownload.com/m2"],
                    "rapidgator.net": ["https://rapidgator.net/file/m2"],
                },
                {},
            ),
        ]
        result = self._run(releases)
        urls = [link[0] for link in result["links"]]
        self.assertEqual(
            sorted(urls),
            ["https://ddownload.com/m2", "https://rapidgator.net/file/m2"],
        )

    def test_falls_back_to_crypted_when_no_direct_links(self):
        # Empty 'links' field → must fall back to the filecrypt container.
        releases = [
            _release(
                self.TITLE,
                {},
                {"ddownload.com": "https://filecrypt.cc/Container/CCC.html"},
            )
        ]
        result = self._run(releases)
        urls = [link[0] for link in result["links"]]
        self.assertEqual(urls, ["https://filecrypt.cc/Container/CCC.html"])


if __name__ == "__main__":
    unittest.main()
