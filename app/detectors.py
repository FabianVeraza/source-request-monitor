import re
from app.schemas import LogEntry

SQLI_PATTERNS = [
    r"(\bor\b\s+1=1\b)",
    r"(--)",
    r"(' OR ')",
    r"(UNION SELECT)"
]

XSS_PATTERNS = [
    r"(<script>)",
    r"(alert\()",
    r"(onerror=)"
]

def analyze_request(entry: LogEntry):
    issues = []
    score = 0

    combined = f"{entry.path} {entry.user_agent}"

    for pattern in SQLI_PATTERNS:
        if re.search(pattern, combined, re.IGNORECASE):
            issues.append("Possible SQL Injection")
            score += 40

    for pattern in XSS_PATTERNS:
        if re.search(pattern, combined, re.IGNORECASE):
            issues.append("Possible XSS")
            score += 30

    if entry.path.startswith("/login") and entry.method == "POST":
        score += 10

    return min(score, 100), issues
