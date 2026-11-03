# ChatGPT and Codex installation

Pixelcraft skills are plain Markdown skill folders containing `SKILL.md` plus optional `agents/openai.yaml` display metadata. They do not require an SDK, API key, remote service, telemetry, or proprietary runtime.

## Codex

Current Codex local skill discovery supports repository-local `.agents/skills/` and user-wide `$HOME/.agents/skills/`. Install Pixelcraft user-wide from the repository root:

```bash
./scripts/install_codex_skills.sh user
```

For a project-local install, run `./scripts/install_codex_skills.sh project /path/to/target-project`. Existing skill folders are skipped by default; pass `--force` to replace them. In Codex, use `/skills` to inspect available skills or `$skill-name` to invoke one. Codex detects skill changes automatically; restart if an update does not appear.

## ChatGPT

In ChatGPT surfaces with Skills enabled, type `@` and select a skill, or let the skill description match the task. In environments without skill imports, attach the relevant `SKILL.md` or paste it into project instructions. Availability depends on the ChatGPT surface and workspace configuration.

## Selection advice

Use `unslop-ui` for a full-screen makeover. Use `slop-detection` or `slop-audit` for diagnosis only. Use a specialist skill for a narrow fix. A focused skill is usually better than loading the entire library for every request.
