---
name: declarative-prompt
description: Scaffold a declarative, outcome-based prompt for a task using a structured markdown template (goal, definition of done, constraints, non-goals, forbidden shortcuts), so the agent receiving it plans its own route. Use this skill whenever the user wants to write, structure, draft, or improve a prompt or brief for an AI agent or coding agent - including phrases like "help me write a prompt for", "scaffold a prompt", "build a brief for this task", "spec this out for Claude Code", "turn this into a proper prompt", or when they describe a substantial task and ask how best to instruct an agent to do it. Trigger it even when the user doesn't say the word "prompt" but is clearly preparing to delegate a non-trivial task to an agent and wants it set up properly.
---

# Declarative Prompt Scaffolder

Help the user produce a completed, task-specific prompt built on declarative
prompting principles: state the goal, the verifiable definition of done, the
constraints and the non-goals - then let the receiving agent plan its own
route. Never turn the output into a step-by-step procedure for the agent to
follow; if the user starts dictating steps, capture the underlying intent and
constraints instead, and say why.

The blank template lives at `assets/template.md`. Read it before scaffolding
so section wording stays consistent.

## Workflow

1. **Capture the task.** Restate the user's task in one sentence and confirm
   it if there is any ambiguity. Extract everything already said in the
   conversation - goal, constraints, context, deadlines - before asking
   anything. Never ask for information the user has already provided.

2. **Classify the task type** and select sections using the guide below. Core
   sections are always included. Add an optional section only when it earns
   its place for this task; a bloated prompt buries its own rules.

3. **Fill what you can, mark what you can't.** Populate each selected section
   from conversation context. Where a critical section (Goal, Definition of
   Done, Constraints) has a gap you cannot responsibly infer, ask the user.
   Ask questions one at a time, and only for gaps that would materially
   change the prompt. For non-critical gaps, insert a reasonable draft and
   flag it with `<!-- TODO: confirm -->` rather than interrogating the user.

4. **Sharpen the two highest-leverage sections:**
   - *Definition of Done* must be verifiable. Prefer executable checks
     (tests pass, linter clean, build green, output validates) over
     subjective ones ("looks good"). If the user offers a vague criterion,
     propose a checkable version of it.
   - *Forbidden Shortcuts* must be task-specific. Name the cheats this
     particular task invites (e.g. for code: editing tests to pass,
     stubbing implementations, disabling linters; for research: fabricated
     citations, secondary sources presented as primary). Generic filler
     here is worse than nothing.

5. **Keep it lean.** Repo-level conventions, standard commands and house
   style belong in AGENTS.md / CLAUDE.md, not in a per-task prompt. If the
   user supplies that kind of content, suggest moving it there and leave it
   out of the prompt.

6. **Deliver.** Output the completed prompt as a markdown file the user can
   copy or save, with all guidance comments from the template removed and
   unused sections deleted. Offer one round of tightening: read the result
   back looking for contradictions between sections (a constraint that
   conflicts with the goal, a done-criterion the non-goals rule out) and fix
   them - contradictory instructions measurably degrade agent performance.

## Section selection guide

Core, always included: Goal, Definition of Done, Constraints, Non-Goals,
Context, Forbidden Shortcuts.

| Task type | Add these optional sections |
|-----------|----------------------------|
| Small fix / one-off script | None - core only, trim Context hard |
| Multi-file feature | Plan First, Verification Steps, Inputs & References |
| Long-running / background agent | Plan First, Autonomy & Escalation, Verification Steps |
| Production / infra change | Risk & Rollback, Autonomy & Escalation, Plan First |
| Research / analysis | Output Format, Inputs & References, Open Questions |
| Writing / comms | Audience & Tone, Output Format, Acceptance Examples |

When a task straddles types, union the sections, then cut any that would sit
empty. An empty section teaches the receiving agent to ignore section
headings.

## Example

**Input:** "I need a prompt for Claude Code to add rate limiting to our
public API. FastAPI, Redis is already in the stack, mustn't break the
existing auth middleware."

**Output sketch (abbreviated):**

```markdown
## Goal
Add per-client rate limiting to the public API so no single client can
degrade service for others.

## Definition of Done
- [ ] Requests over the limit receive HTTP 429 with a Retry-After header
- [ ] Existing test suite passes unchanged
- [ ] New tests cover the limit boundary and header behaviour
- [ ] Auth middleware behaviour is unchanged (existing auth tests pass)

## Constraints
- FastAPI; use the existing Redis instance for counters
- No new external dependencies without flagging first

## Non-Goals
- No changes to auth middleware
- No per-endpoint custom limits in this pass

## Forbidden Shortcuts
- No editing existing tests to make them pass
- No in-memory fallback silently replacing Redis

## Plan First
Before making any changes, produce a step-by-step plan and stop for my
approval.
```

Note what the example does not contain: no instructions about which files to
open, which library to pick, or what order to work in. That is the receiving
agent's job.
