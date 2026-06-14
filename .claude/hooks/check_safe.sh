#!/usr/bin/env bash
# PreToolUse hook for Bash: blocks obviously destructive commands.
# Delegates JSON parsing to check_safe.py since jq isn't available everywhere.

dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python "$dir/check_safe.py"
