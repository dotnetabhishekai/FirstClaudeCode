import sys
import json
import re

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

command = data.get("tool_input", {}).get("command", "")

DANGEROUS_PATTERNS = [
    r"rm\s+(-[a-zA-Z]*r[a-zA-Z]*f|-[a-zA-Z]*f[a-zA-Z]*r)\s+(/|~)(\s|$)",
    r"rm\s+(-[a-zA-Z]*r[a-zA-Z]*f|-[a-zA-Z]*f[a-zA-Z]*r)\s+\*",
    r":\(\)\s*\{.*\};\s*:",
    r"mkfs(\.\w+)?\s",
    r"dd\s+.*of=/dev/",
    r">\s*/dev/sd[a-z]",
    r"git\s+push\s+.*(--force|-f)(\s|$)",
    r"git\s+reset\s+--hard",
    r"chmod\s+-R\s+777\s+/",
]

for pattern in DANGEROUS_PATTERNS:
    if re.search(pattern, command, re.IGNORECASE):
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": (
                    f'check_safe: blocked command matching pattern "{pattern}": {command}'
                ),
            }
        }))
        sys.exit(0)

sys.exit(0)
