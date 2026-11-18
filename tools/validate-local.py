"""Validate tracked corpus files without rewriting texts or generated data."""
from pathlib import Path
import json
import subprocess
import sys
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
files = subprocess.check_output(["git", "ls-files", "-z"], cwd=root).decode("utf-8").split("\0")
counts = {"xml": 0, "json": 0, "python": 0}
errors = []
for name in filter(None, files):
    path = root / name
    suffix = path.suffix.lower()
    try:
        if suffix == ".xml":
            for _, element in ET.iterparse(path, events=("end",)):
                element.clear()
            counts["xml"] += 1
        elif suffix == ".json":
            json.loads(path.read_text(encoding="utf-8-sig"))
            counts["json"] += 1
        elif suffix == ".py":
            compile(path.read_bytes(), str(path), "exec")
            counts["python"] += 1
    except (ValueError, SyntaxError, OSError, ET.ParseError) as error:
        errors.append({"file": name, "error": str(error)})
print(json.dumps({"checked": counts, "errors": errors}, ensure_ascii=False, indent=2))
sys.exit(bool(errors))
