# GitHub publication

Target repository: `voyager67/pixelcraft`

Suggested description: A focused AI-slop recognition and remediation skill library for ChatGPT and Codex.

Suggested topics: `agent-skills`, `ai-slop`, `ui-design`, `ux-design`, `codex`, `chatgpt`, `frontend`, `design-systems`, `accessibility`, `design-quality`.

Publication helper: `scripts/publish.sh`. It uses the GitHub CLI's existing authenticated session, confirms the account, runs validation and security checks, and refuses to overwrite an existing remote repository or reuse an existing `.git` history. It does not contain credentials. Before creating the initial commit, it obtains the public account ID from `gh api user` and configures a repository-local GitHub `noreply` email (GitHub's account-ID-based `noreply` address). It does not read or publish your global Git email.

Do not publish until both local checks pass and a human has reviewed the full file list. Commit author metadata becomes public on GitHub; this helper uses the account-specific `noreply` address to avoid exposing the private email in Git commit history.
