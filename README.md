# agentics

Modular agentics for Claude Code: skills, subagents, hooks, and reusable instructions. Each component is packaged as its own plugin so you can install only what you want.

## Install

Add this marketplace once:

```
/plugin marketplace add <owner>/agentics
```

Then install any single component:

```
/plugin install buyers-guide@agentics
/plugin install declarative-prompt@agentics
```

Choose user, project, or local scope at install time.

## Layout

```
.claude-plugin/marketplace.json   # catalog of all plugins
plugins/<name>/                   # one plugin per component
  .claude-plugin/plugin.json
  skills/<name>/SKILL.md          # skills
  agents/<name>.md                # subagents
  hooks/hooks.json                # hooks
snippets/                         # reusable CLAUDE.md / AGENTS.md blocks to @-import
```

## Snippets

Snippets are always-on instruction blocks for CLAUDE.md / AGENTS.md. They aren't a plugin — adding the marketplace clones this whole repo to `~/.claude/plugins/marketplaces/agentics/`, so once you've run `/plugin marketplace add`, reference any snippet directly from your CLAUDE.md:

```markdown
@~/.claude/plugins/marketplaces/agentics/snippets/writing-style.md
```

No install step, no version in the path. New snippet content arrives with `/plugin marketplace update agentics` (or marketplace auto-update, if enabled). Importing a file from outside the project triggers a one-time approval prompt per project — that's expected.
