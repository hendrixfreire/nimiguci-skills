# Workspace Skill

List and explore the workspace directory contents.

## Usage

When the user asks to "list workspace", "show workspace contents", or similar:

1. Run: `ls -la /root/.openclaw/workspace`
2. Optionally run `find /root/.openclaw/workspace -maxdepth 2 -type f` for deeper view
3. Organize the output into categories:
   - Core files (AGENTS.md, SOUL.md, MEMORY.md, etc.)
   - Skills (skills/ folder)
   - Project-specific files
   - Config/logs/cache

## Quick Command

```bash
ls -la /root/.openclaw/workspace && echo "--- Subdirs ---" && find /root/.openclaw/workspace -maxdepth 2 -type d
```
