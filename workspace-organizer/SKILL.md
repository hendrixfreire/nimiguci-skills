---
name: workspace-organizer
description: Audit, organize, and maintain the local workspace structure. Use when asked to clean up the workspace, reorganize files/folders, archive old outputs, standardize memory file names, move project files into clearer folders, or enforce the workspace layout rules.
---

Keep the workspace predictable and conservative. Prefer moving and grouping over deleting.

## Default structure
Use `docs/WORKSPACE_STRUCTURE.md` as the source of truth for folder roles and naming rules. Read it before making structural changes.

## Core behavior
- Keep the root minimal
- Group project files under `projects/<name>/`
- Keep reusable scripts under `scripts/`
- Keep current outputs under `output/`
- Move obsolete or versioned material to `archive/`
- Keep memory organized under `memory/daily/`, `memory/notes/`, and `memory/incidents/`
- Prefer renames and moves over content rewrites unless paths must be updated

## Safety rules
- Do not delete user files by default
- When moving project config or tokens, map and update references first
- Validate path-sensitive code after moves when practical
- Do not archive active runtime state blindly
- After running `scripts/maintenance/organize_workspace.py --dry-run`, explicitly check whether any proposed move could break an MCP, skill, script, or local integration that depends on fixed local paths
- Use `config/workspace-organizer-sensitive-paths.json` as the protected-path list for known path-sensitive areas
- If there is MCP/path sensitivity risk, do not apply moves blindly; recommend one of: updating the relevant config/path references, keeping the file in place, or moving it only after a controlled migration plan
- Prefer constant organization with compatibility over perfect folder purity
- Before `--apply`, keep a change manifest / backup record of the planned moves so rollback stays possible

## Specific guidance
### Memory
- Use `YYYY-MM-DD.md` for daily summaries
- Use `YYYY-MM-DD_HHMM.md` for timestamped day entries
- Use kebab-case for topic notes

### Archive
- Put old config backups in `archive/configs/`
- Put superseded outputs in `archive/outputs/`
- Put obsolete artifacts in `archive/legacy/`
- Do not use `archive/` as a blind dump; create subfolders when needed

### Agents
- Keep only agent-specific bundles in `agents/`
- If a file is actually project code or project config, move it to the relevant project instead of leaving it in `agents/`

### Reminders
- Treat `reminders/` as operational only if it contains active reminder assets
- If empty or inactive, leave it empty or archive it after confirmation

## Workflow
1. Inspect the relevant folders first
2. Propose or infer the target structure from `docs/WORKSPACE_STRUCTURE.md`
3. Prefer running `scripts/maintenance/organize_workspace.py --report-only` for recurring reviews; it generates both JSON manifest and Markdown report in `archive/notes/`
4. Review the generated report and manifest for MCP/skill/script/local-tool path sensitivity before applying anything
5. If a move may break an MCP or local integration, recommend the safest path: update config references, migrate in two steps, or keep the file where it is for now
6. Use `scripts/maintenance/organize_workspace.py --apply --from-manifest <manifest.json>` when applying a reviewed plan
7. Use `--apply-risky` only after explicit human approval for high/critical-risk moves
8. Prefer `--smoke-tests` after apply to validate Python/config integrity
9. Move files conservatively for anything the script does not cover
10. Update broken paths when moves affect active scripts/config
11. Summarize what changed and what still needs manual review
