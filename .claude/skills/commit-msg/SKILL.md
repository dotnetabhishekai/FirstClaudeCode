---
name: commit-msg
description: Draft a commit message for the currently staged changes, following this repo's conventions. Use when the user asks to write, draft, or suggest a commit message without actually creating the commit.
---

# Commit Message Drafting

Draft a commit message for the staged changes in this repo. Do not run `git commit` — only output the drafted message for the user to review.

## Steps

1. Run `git diff --staged` to see what will be committed. If nothing is staged, say so and stop (don't draft a message for unstaged changes without asking).
2. Run `git log --oneline -10` to check for an existing commit message style/convention in this repo. If history is empty, fall back to the default style below.
3. Draft the message:
   - **Subject line**: imperative mood, concise (≈50 chars, hard limit ~70), no trailing period (e.g. "Add CSV export to invoice generator").
   - **Body** (only if the change needs explaining): blank line after subject, then 1-3 sentences focused on *why* the change was made, not a restatement of the diff.
4. Present the drafted message in a fenced code block so the user can copy it or ask for adjustments.

## Notes

- Match the tone/style of recent commits if the repo has history.
- Don't invent scope/ticket prefixes (e.g. `feat:`, `JIRA-123:`) unless that convention already appears in `git log`.
- If the diff spans unrelated changes, mention this to the user and suggest splitting the commit instead of writing one message that covers everything.
