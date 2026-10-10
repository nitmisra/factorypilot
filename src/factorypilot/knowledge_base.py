"""Minimal keyword-based retrieval; replace with vector retrieval in a later phase."""
from pathlib import Path
import re

MANUAL_PATH = Path(__file__).resolve().parents[2] / "data" / "manuals" / "conveyor_troubleshooting.md"


def retrieve_guidance(query, manual_path=MANUAL_PATH, max_sections=3):
    """Retrieve simple manual sections by keyword overlap."""
    path = Path(manual_path)
    if not path.exists():
        return []

    text = path.read_text(encoding="utf-8")
    sections = re.split(r"(?m)(?=^## )", text)
    terms = {t.lower() for t in re.findall(r"[a-zA-Z0-9_]+", query) if len(t) > 2}
    scored = []
    for section in sections:
        if not section.strip():
            continue
        haystack = section.lower()
        score = sum(1 for term in terms if term in haystack)
        if score:
            scored.append((score, section.strip()))
    scored.sort(key=lambda item: item[0], reverse=True)
    return [section for _, section in scored[:max_sections]]
