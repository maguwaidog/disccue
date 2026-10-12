#!/usr/bin/env python3
"""Static contract checks for prepared Umami website analytics. Read-only."""
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_HOST = "https://cloud.umami.is/script.js"
WEBSITE_ID = "3a92a319-0024-4673-bcca-f7feea1a78dc"
EXPECTED = {
    "index.html": {"download_hero_click", "download_pricing_click", "checkout_hero_click",
                   "checkout_pricing_click", "demo_hero_click", "demo_section_click", "guide_intro_click"},
    "en/index.html": {"download_hero_click", "download_pricing_click", "checkout_hero_click",
                      "checkout_pricing_click", "demo_hero_click", "demo_section_click", "guide_intro_click"},
    "guides/blu-ray-external-subtitles/index.html": {"trial_guide_click"},
    "en/guides/blu-ray-external-subtitles/index.html": {"trial_guide_click"},
}

class ContractParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.scripts = []
        self.events = []
        self.in_head = False
        self.scripts_in_head = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "head": self.in_head = True
        if tag == "script":
            self.scripts.append(a)
            self.scripts_in_head.append(self.in_head)
        if a.get("data-umami-event"):
            assert tag == "a" and a.get("href"), "event must be on an anchor with a destination"
            self.events.append(a["data-umami-event"])
    def handle_endtag(self, tag):
        if tag == "head": self.in_head = False

def run():
    n = 0
    for path, expected in EXPECTED.items():
        parsed = ContractParser()
        parsed.feed((ROOT / path).read_text(encoding="utf-8"))
        assert len(parsed.scripts) == 1, (path, "script count")
        a = parsed.scripts[0]
        assert parsed.scripts_in_head == [True], path
        for k, v in {
            "src": SCRIPT_HOST,
            "data-website-id": WEBSITE_ID,
            "defer": None,
            "data-exclude-search": "true",
            "data-exclude-hash": "true",
            "data-do-not-track": "true",
            "data-domains": "maguwaidog.github.io",
        }.items():
            assert k in a and a[k] == v, (path, k)
        assert len(parsed.events) == len(expected), (path, parsed.events)
        assert set(parsed.events) == expected, (path, parsed.events)
        n += len(parsed.events)
    for path in ("privacy.html", "en/privacy.html"):
        parsed = ContractParser()
        content = (ROOT / path).read_text(encoding="utf-8")
        parsed.feed(content)
        assert not parsed.scripts, path
        assert "umami.is/privacy" in content, path
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "Umami Cloud" in readme
    print(f"ANALYTICS_STATIC_PASS: 4 pages, {n} events, 2 privacy notices")

if __name__ == "__main__":
    run()
