# core/utils.py
import re
import json
from collections import Counter

def extract_version_info(banner):
    try:
        banner = banner.lower()
        words = banner.split()
        for word in words:
            if '/' in word:
                parts = word.split('/')
                service = parts[0]
                version = parts[1] if len(parts) > 1 else None
                return service, version
        return None, None
    except:
        return None, None

def is_vulnerable(service, version, db_path="version_db.json"):
    try:
        with open(db_path, 'r') as f:
            db = json.load(f)
        if service in db and version in db[service]:
            return db[service][version]  # returns severity
    except Exception as e:
        print(f"[Error] Version check failed: {e}")
    return None

def severity_rank(item):
    levels = {"high": 3, "medium": 2, "low": 1, None: 0}
    return levels.get(item.get("severity"), 0)

def count_severity_levels(results):
    counter = Counter()
    for item in results:
        if item["severity"]:
            counter[item["severity"]] += 1
    return counter

def get_emoji_for_severity(severity):
    emoji_map = {"high": "🔴", "medium": "🟠", "low": "🟡"}
    return emoji_map.get(severity, "⚠️")
