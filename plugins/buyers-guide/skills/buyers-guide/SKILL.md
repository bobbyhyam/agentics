---
name: buyers-guide
description: "Create comprehensive, research-backed buyer's guides for any product category, delivered as a single self-contained full-colour HTML page in a tech-magazine style with real product photos, AI-generated concept illustrations and inline SVG charts. Use this skill whenever a user asks for help choosing, comparing, or understanding products in a category - whether they say 'buyer's guide', 'what should I buy', 'help me choose a...', 'compare options for...', 'what's the best...', 'is now a good time to buy...', or any variation of product research and purchasing advice. Trigger for any product category: electronics, appliances, tools, vehicles, home improvement, outdoor and garden kit, software, services, or anything else a consumer might need to evaluate and purchase. Trigger even for a casual one-liner like 'need a new drill, thoughts?'."
---

# Buyer's Guide Skill

Produce a buyer's guide that gives the reader everything they need to make a confident purchase even if they know nothing about the category, and deliver it as one HTML file that looks like a spread from a glossy technology magazine. The research is the substance; the page is how the reader gets through it without giving up.

## Bundled files

- `assets/template.html` - the page. Copy it, fill it, do not restyle it. Every component the guide needs is already in there with a comment saying what goes in it.
- `references/style-guide.md` - brand tokens, when to use a photo versus an illustration versus an SVG, how to source photos, the mandatory prompt prefix for generated illustrations, and SVG rules. Read it before adding any visual.
- `scripts/embed_images.py` - inlines every image as base64 so the finished file is self-contained. Run it last.

## Process

### 1. Scope the category

Most categories are a tree: laptops split into Windows, Mac and Linux, then Windows into ultrabook, gaming, workstation and 2-in-1. Map the tree mentally first. If the category is broad enough that the full landscape would be a very long guide, ask one clarifying question to narrow it. One question, then proceed; the user can widen the scope after seeing the guide.

### 2. Research

Use web search extensively. Expect model naming to be regional and messy (the same TV can carry different names in the UK and the US, and a name can be reused for a different product), so pin each contender to its exact model code before scoring it. Search and treat training knowledge as a starting hypothesis only, because pricing, availability and model line-ups change monthly. Search from several angles:

- "best [category]" plus the current year and next year, for expert roundups
- "[specific model] review" for depth on each contender
- "[category] problems" and "[category] issues" for gotchas
- "[model A] vs [model B]" for head to heads
- "[category] buying guide" to see which criteria experts weight
- Reddit and specialist forums for owner sentiment, including how the manufacturer handles complaints
- "[brand] new model", "[category] upcoming" and trade show coverage (CES, IFA, MWC, Eurobike, Spoga, and the shows relevant to the category) for the outlook section

Fetch the full article for anything that shapes a recommendation; snippets are not enough to score a product. Keep a running list of sources with URL, publisher and date, because the page ends with a numbered source list and every score needs to be defensible.

### 3. Choose the palette and decide the visuals

Pick one of the six palettes in `references/style-guide.md` by the character of the category (Cinema for TVs and audio, Field for garden kit, and so on; Circuit when nothing fits). Set its three hex values in the template's `:root` and use the same three values in every illustration prompt and SVG, so the photographs, drawings and page chrome all belong to one issue. The structure, type and layout never change between guides; only these three colours do.

Before writing, list the concepts that are easier to see than to read, and decide for each whether it is an AI illustration (how something works, what types look like, a scene), an inline SVG (charts, trees, labelled schematics) or nothing. Two or three illustrations and one or two SVGs is typical. Then, for every product that will get a card, find a photograph and a current UK price. One Firecrawl agent job does both for the whole set; the method, the fallback and the rejection rules are in `references/style-guide.md`. Start that job before generating illustrations so it runs while you work.

Generate illustrations through the `generate-image` skill using the house-style prompt prefix from the style guide, verbatim, so every picture shares the page's palette. Check each result: any colour outside the palette, or a picture that decorates rather than explains, gets one regeneration and then falls back to SVG or nothing.

### 4. Build the page

Copy `assets/template.html` to `/home/claude/guide/index.html` and save images to `/home/claude/guide/img/`. Fill the sections in this order; the template's comments say what each expects.

- **Cover** - category tag, an uppercase title of six words or fewer, a one-sentence standfirst that states the decision the reader faces.
- **Meta** - research date, source count, price basis (country, currency, whether bare-tool or bundle).
- **TL;DR** - two or three sentences with the decisive nouns in bold. The reader should be able to stop here.
- **Landscape** - one tile per subcategory; `warn` tiles for options most readers should skip. An illustration here if the category structure is not obvious.
- **Decode the spec sheet** - only terms that change the decision, each with what it means and why it matters in plain language. Skip trivia.
- **What actually matters** - the buying criteria in order of importance, each saying what good looks like and how to check it in a shop or a spec sheet.
- **Watch out** - hidden costs, misleading claims, common regrets.
- **Scores and product cards** - score bars for every contender, then a card per product with photo, score, price line, spec chips, a short assessment, what owners praise, what owners complain about, and an award badge for the winner. Include mainstream picks and anything new and gaining momentum.
- **Head to head** - a spec table, one row per product, columns limited to the specs that differ meaningfully.
- **The podium** - exactly three picks: best overall, best balanced (say what it gives up against the winner), best value. Each with the reasoning so the reader can judge whether it applies to them.
- **Buy now or wait** - confirmed upcoming releases, technology shifts, price trends, then a stamped three-to-five-word verdict. Be honest about uncertainty but still give a verdict.
- **Sources** - numbered, linked, with publisher and date.

Scores are out of 10 to one decimal place and are your synthesis of expert reviews and owner reports. Keep them consistent: a product two points behind another should be visibly worse in the assessment text. Bar width is the score times ten.

### 5. Embed and deliver

Run `python3 scripts/embed_images.py /home/claude/guide/index.html`. It trims transparent and white borders, resizes, inlines every `<img>` as base64 and reports any that failed; swap failed photos for another source or the placeholder block and run it again. Copy the result to `/mnt/user-data/outputs/<category>-buyers-guide.html` and present it with `present_files`.

In the conversation, give a three or four sentence summary: the three picks, the buy-or-wait verdict, and anything surprising the research turned up. Do not repeat the guide.

## Why the page is built this way

The reader is usually on a phone, in the Claude mobile viewer, which forces its own dark background onto pages that do not declare one. The template sets `color-scheme: light only` and paints every surface explicitly so the page renders identically everywhere. Images are embedded rather than linked because retailer image URLs rotate and the guide should still work in a year. The structure and type are fixed and only the three accent colours change per category, so guides for a lawnmower and a laptop look like issues of the same magazine with different cover art, and a generated illustration sits next to a product photograph without jarring.

## Writing style

- Write for an intelligent reader who is new to the category. Short sentences. Verbs over nouns.
- Be direct and opinionated where the evidence supports it: "the Halden is the one to buy because" beats "both have their merits".
- UK English. Never use em dashes; use a hyphen with a space either side.
- No marketing language. If a product is called revolutionary, say whether it is.
- When the evidence is mixed, say so in one sentence and move on.
- Every sentence should tell the reader something that changes what they buy or when.
