#!/usr/bin/env python3
"""
Updates the domain and method keywords in README.md from
domain-keywords.txt and method-keywords.txt.
"""

from pathlib import Path
import re
import sys

def load_keywords(file_path: Path) -> list[str]:
    if not file_path.exists():
        return []
    seen = set()
    keywords = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            kw = line.strip()
            if kw and kw not in seen:
                seen.add(kw)
                keywords.append(kw)
    return keywords

def format_list(keywords: list[str]) -> str:
    return "\n".join(f"- `{kw}`" for kw in keywords)

def update_readme(repo_root: Path) -> bool:
    readme_path = repo_root / "README.md"
    domain_file = repo_root / "domain-keywords.txt"
    method_file = repo_root / "method-keywords.txt"

    if not readme_path.exists():
        print(f"Error: {readme_path} not found.", file=sys.stderr)
        return False

    domain_kws = load_keywords(domain_file)
    method_kws = load_keywords(method_file)

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Pattern for Domain Keywords
    domain_replacement = (
        "#### 1. Domain Keywords\n"
        "Full list is in [`domain-keywords.txt`](domain-keywords.txt):\n"
        + format_list(domain_kws)
        + "\n\n"
    )
    content, count1 = re.subn(
        r"#### 1\. Domain Keywords\s*\nFull list is in \[`domain-keywords\.txt`\]\(domain-keywords\.txt\):[\s\S]*?(?=#### 2\. Method Keywords)",
        domain_replacement,
        content
    )

    # Pattern for Method Keywords
    method_replacement = (
        "#### 2. Method Keywords\n"
        "Full list is in [`method-keywords.txt`](method-keywords.txt):\n"
        + format_list(method_kws)
        + "\n\n"
    )
    content, count2 = re.subn(
        r"#### 2\. Method Keywords\s*\nFull list is in \[`method-keywords\.txt`\]\(method-keywords\.txt\):[\s\S]*?(?=#### How to Format Keywords in YAML)",
        method_replacement,
        content
    )

    if count1 == 0 or count2 == 0:
        print("Warning: Keyword sections could not be matched in README.md", file=sys.stderr)
        return False

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("README.md successfully updated with latest keywords.")
    return True

if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parent.parent
    success = update_readme(repo_root)
    sys.exit(0 if success else 1)
