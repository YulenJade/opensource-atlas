#!/usr/bin/env python3
"""Refresh GitHub category rankings with partial-failure cache fallback."""
import datetime
import json
import os
from pathlib import Path
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs" / "data.json"
CATEGORIES = json.loads((ROOT / "categories.json").read_text(encoding="utf-8"))
old = json.loads(DATA.read_text(encoding="utf-8")) if DATA.exists() else {}
cached = {c["id"]: c for c in old.get("categories", [])}
headers = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "OpenSource-Atlas",
    "X-GitHub-Api-Version": "2022-11-28",
}
if os.getenv("GITHUB_TOKEN"):
    headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]

now = datetime.datetime.now(datetime.timezone.utc).isoformat()
output = {"updated_at": now, "categories": [], "failed_categories": []}
success = 0

def get_json(url):
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=45) as response:
                return json.load(response)
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
            if attempt == 3:
                raise
            wait = 90 if isinstance(exc, urllib.error.HTTPError) and exc.code in (403, 429) else 8 * (attempt + 1)
            print(f"Retrying in {wait}s: {exc}", flush=True)
            time.sleep(wait)

for cat in CATEGORIES:
    try:
        query = cat["query"] + " fork:false archived:false"
        url = "https://api.github.com/search/repositories?" + urllib.parse.urlencode({
            "q": query, "sort": "stars", "order": "desc", "per_page": 50
        })
        payload = get_json(url)
        rows = [{
            "rank": rank,
            "name": r["full_name"],
            "url": r["html_url"],
            "description": r.get("description") or "",
            "stars": r["stargazers_count"],
            "language": r.get("language") or "",
            "license": (r.get("license") or {}).get("spdx_id") or "Unknown",
            "updated_at": r.get("pushed_at") or "",
            "topics": r.get("topics") or [],
        } for rank, r in enumerate(payload["items"], 1)]
        record = {k: cat[k] for k in ("id", "name", "name_en", "group", "group_name", "group_name_en")}
        record.update(repositories=rows, total_count=payload.get("total_count", 0), fetched_at=now)
        output["categories"].append(record)
        success += 1
        print(f"OK {cat['id']}: {len(rows)}", flush=True)
    except Exception as exc:
        print(f"FAILED {cat['id']}: {exc}", flush=True)
        output["failed_categories"].append(cat["id"])
        if cat["id"] in cached:
            record = dict(cached[cat["id"]])
            record.update({k: cat[k] for k in ("name", "name_en", "group", "group_name", "group_name_en")})
            output["categories"].append(record)
    time.sleep(7)

if success == 0:
    raise SystemExit("All category queries failed: existing data preserved.")
output["categories"].sort(key=lambda c: next(i for i, item in enumerate(CATEGORIES) if item["id"] == c["id"]))
DATA.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Updated {success}/{len(CATEGORIES)} categories; stale cached: {len(output['failed_categories'])}", flush=True)
