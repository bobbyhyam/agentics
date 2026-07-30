# Declarative Prompt Template

Fill in the core sections for every task. Add optional sections only when they earn their place - a bloated prompt is an anti-pattern (rules get lost in the noise). Delete guidance comments (in *italics*) before sending.

---

## CORE SECTIONS (always included)

## Goal

*One or two sentences: the outcome you want and why it matters. State the destination, not the route. If you can't state the goal without describing steps, you haven't finished thinking about it yet.*

>

## Definition of Done

*Verifiable success criteria. Prefer executable checks (tests pass, linter clean, build green, doc renders) over vibes ("looks good"). This is the single highest-leverage section - under-specified "done" is what agents reward-hack.*

- [ ]
- [ ]
- [ ]

## Constraints

*Hard boundaries the solution must respect: tech stack, versions, APIs, style conventions, performance limits, security requirements, budget/time. These are the "must not violate" rules, distinct from preferences.*

-

## Non-Goals

*Explicitly out of scope. Prevents scope creep and stops the agent "helpfully" refactoring things you didn't ask about. Often the cheapest section to write and the most effective.*

-

## Context

*Minimal, high-signal only: relevant files/paths, prior decisions, links, domain facts the agent can't discover itself. Don't paste what the agent can read or fetch - point to it. If it's a repo convention, it belongs in AGENTS.md/CLAUDE.md, not here.*

>

## Forbidden Shortcuts

*The cheats you refuse: no disabling linters or tests, no stubbed implementations, no editing test files to pass, no hardcoded outputs, no declaring success without running the verification. Name the specific shortcuts this task invites.*

-

---

## OPTIONAL SECTIONS (situation dependent)

## Plan First

*Use for anything non-trivial or multi-file. "Produce a plan and wait for my approval before implementing." The single most recommended gate across vendor guidance.*

> Before making any changes, produce a step-by-step plan and stop for my approval.

## Autonomy & Escalation

*Calibrate eagerness. When should the agent proceed on its own judgement vs stop and ask? Name the decision types that need a human (irreversible actions, external side-effects, ambiguous requirements).*

- Proceed without asking when:
- Stop and ask when:

## Verification Steps

*How the agent should check its own work before declaring done - the commands to run, the order, and what output counts as a pass. Distinct from Definition of Done: that's the target, this is the checking procedure.*

1.

## Inputs & References

*Files, URLs, tickets, designs, prior art, examples of good output. Label each so it's clear what role it plays (spec vs example vs background).*

-

## Output Format

*Deliverable shape: file(s) and paths, language, doc structure, length, naming. Only needed when the format isn't obvious from the goal.*

>

## Acceptance Examples

*Concrete input -> expected output pairs, or a worked example of "good". Few-shot examples remain one of the most reliable steering tools.*

| Input | Expected output |
|-------|-----------------|
|       |                 |

## Risk & Rollback

*For changes touching production, data, or anything irreversible: blast radius, backout plan, what to snapshot first.*

-

## Open Questions

*Known unknowns you want the agent to resolve or flag rather than silently assume. "If any of these change your approach, say so before implementing."*

-

## Audience & Tone

*Writing/comms tasks only: who reads this, register, UK/US English, terminology to use or avoid.*

>

---

## Quick selection guide

| Task type | Add these optional sections |
|-----------|----------------------------|
| Small fix / one-off script | None - core only, and consider trimming Context |
| Multi-file feature | Plan First, Verification Steps, Inputs & References |
| Long-running / background agent | Plan First, Autonomy & Escalation, Verification Steps |
| Production / infra change | Risk & Rollback, Autonomy & Escalation, Plan First |
| Research / analysis | Output Format, Inputs & References, Open Questions |
| Writing / comms | Audience & Tone, Output Format, Acceptance Examples |
