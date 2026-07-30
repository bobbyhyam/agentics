---
name: buyers-guide
description: "Create comprehensive, research-backed buyer's guides for any product category. Use this skill whenever a user asks for help choosing, comparing, or understanding products in a category - whether they say 'buyer's guide', 'what should I buy', 'help me choose a...', 'compare options for...', 'what's the best...', or any variation of product research and purchasing advice. Trigger for any product category: electronics, appliances, tools, vehicles, home improvement, software, services, or anything else a consumer might need to evaluate and purchase."
---

# Buyer's Guide Skill

You are creating a comprehensive, well-researched buyer's guide for a product category. The goal is to give the reader everything they need to make a confident, informed purchasing decision - even if they know nothing about the category going in.

## How this skill works

The user gives you a product category (e.g. "robot lawnmower", "laptop", "home heating system"). Your job is to research the category thoroughly and produce a detailed markdown guide that covers the full landscape of options, explains the technical concepts a buyer needs to understand, compares specific products, and makes clear recommendations.

## Process

### 1. Understand the category and scope

Before diving into research, think about the category structure. Most product categories break down into types, and those types break down further. For example:

- Laptops: Windows / Mac / Linux, then within Windows: ultrabooks / gaming / workstation / 2-in-1
- Home heating: gas boiler / heat pump / electric radiator, then within heat pump: air-source / ground-source
- Power tools: corded / cordless, then by voltage tier, then by brand ecosystem

Map out this tree mentally first. Then ask the user if they want the full landscape or if they'd like to narrow the focus. Some users want the complete picture; others already know they want a specific subcategory and just need help choosing within it.

If the category is broad and would result in an extremely long guide covering many unrelated product types, ask one focused clarifying question to help narrow the scope. Keep it to one question at a time - don't overwhelm with a list of options.

### 2. Research thoroughly

Use web search tools extensively. You need current, accurate information - not just what you know from training data. For each product category and subcategory, research:

- What products are currently on the market
- Current pricing and availability
- Recent reviews from reputable sources (specialist publications, not just aggregator sites)
- User reviews and sentiment from forums, retailer reviews, and communities
- Recent product launches or announcements
- Known issues, recalls, or common complaints

Do multiple searches with different angles. A single search rarely gives you the full picture. Search for things like:

- "best [product category] 2025 2026" for roundup reviews
- "[specific product] review" for individual product depth
- "[product category] problems" or "[product category] issues" for gotchas
- "[product A] vs [product B]" for head-to-head comparisons
- "[product category] buying guide" to see what criteria experts emphasise
- Reddit, forums, and community discussions for real user sentiment
- "[product category] 2026 2027 upcoming" or "[brand] new model" for upcoming releases and industry direction
- Trade show coverage (CES, IFA, MWC, etc.) for announced but not yet released products

### 3. Write the guide

The guide should be a single markdown document with the following structure. Adapt section headings to fit the specific category naturally - the structure below is a framework, not a rigid template.

#### Document structure

**Title and introduction**
A brief overview of the category and what this guide covers. Set expectations for what the reader will learn.

**Category landscape**
Break down the different types/approaches available. Explain each subcategory, what distinguishes it, and who it's best suited for. Go as deep as the tree requires - if a subcategory has meaningful further divisions, cover those too.

This section should help someone who knows nothing about the category understand what their options are at a high level before getting into specific products.

**Key concepts and terminology**
Explain the technical terms and concepts that matter for making a buying decision. The reader shouldn't have to Google jargon while reading your guide. Focus on terms that actually affect the buying decision - skip anything that's just trivia.

For each term, explain what it means in plain language and, importantly, why it matters. Don't just define "SEER rating" - explain that a higher SEER rating means lower energy bills and roughly how much difference it makes.

**What to look for (buying criteria)**
A clear breakdown of the criteria that should drive the purchase decision, in rough order of importance. For each criterion, explain what good looks like, what to watch out for, and how to evaluate it.

This section should feel like advice from a knowledgeable friend - practical, opinionated where appropriate, and focused on what actually matters rather than spec-sheet padding.

**Gotchas and common pitfalls**
Things that catch buyers out. These might be category-wide (e.g. "most advertised battery life figures are under ideal conditions") or specific to certain subcategories. Include things like hidden costs (installation, accessories, ongoing maintenance), misleading marketing claims, and common regrets from buyers.

**Product comparison**
This is the meat of the guide. For each relevant subcategory, compare specific products feature by feature. Include:

- **Mainstream/popular products**: the well-known, widely-recommended options
- **New and trending products**: recently launched or gaining momentum
- For each product: key specs, pricing, standout features, notable weaknesses

Present comparisons in a way that makes differences easy to spot. Use tables where they help (e.g. for spec comparisons), but supplement with prose that explains the significance of the differences. Raw specs without context ("this one has 16GB RAM and that one has 32GB") are less useful than explained specs ("16GB is adequate for general use but you'll hit limits with video editing or running many applications simultaneously").

**User sentiment**
For each recommended product, summarise what real users say. Focus on:

- The most common praise - what do people consistently love about it?
- The most common complaints - what issues come up repeatedly?
- How the company responds to problems - are they known for good support, or do complaints go unanswered?
- Any patterns in reliability over time

Source this from user reviews, forums, Reddit, and community discussions. Be specific - "some users report issues" is weak; "multiple users on r/HomeImprovement report the thermostat losing Wi-Fi connection after firmware updates" is useful.

**Recommendations**
Make three clear recommendations:

1. **Best overall (unlimited budget)**: The best product in the category regardless of price. Explain why it's worth the premium.
2. **Best balanced (features vs. budget)**: The sweet spot where you get most of the performance for significantly less money. Explain what you're giving up compared to the top pick and why those trade-offs are acceptable.
3. **Best value**: The best option for someone who wants something good without spending more than necessary. Explain what makes it a smart buy at its price point.

For each recommendation, explain the reasoning clearly. The reader should understand not just what you recommend but why, and be able to judge whether your reasoning applies to their situation.

**What's coming next (outlook and timing)**
This section helps the reader decide whether now is the right time to buy or whether they should wait. Research and cover:

- **Upcoming products and releases** - Are any major manufacturers about to launch new models or next-generation versions? If a flagship product is due for a refresh in the next few months, the reader needs to know.
- **Emerging technology** - Is there a meaningful technology shift on the horizon that could change the category? For example, a new type of battery chemistry, a different approach to navigation, a regulatory change that will affect available options. Explain what it is, when it's likely to arrive, and how much of a difference it would actually make.
- **Industry trends** - Which direction is the category heading? Are prices falling? Is a particular subcategory gaining momentum while another is declining? Are there supply chain or regulatory factors that might affect availability or pricing?
- **Buy now or wait?** - Give a clear, reasoned verdict. If there's a compelling reason to wait (e.g. a major product launch is confirmed for next quarter), say so. If the current options are strong and nothing game-changing is imminent, say that too. Be honest about the uncertainty involved - nobody can predict the future perfectly, but you can help the reader make a more informed timing decision.

Search specifically for news about upcoming releases, product roadmaps, trade show announcements (CES, IFA, etc.), and industry analysis pieces. This section should feel forward-looking and practical, not speculative or vague.

### 4. Format and deliver

Save the completed guide as a markdown file. Use clear heading hierarchy, tables where appropriate, and keep paragraphs at a readable length.

After saving the file, provide a brief summary in the conversation highlighting the key recommendations and any surprising findings from the research.

## Writing style

- Write for a general audience. Assume the reader is intelligent but unfamiliar with the category.
- Be direct and opinionated where the evidence supports it. "Product X is the clear leader here because..." is more useful than "Product X and Product Y both have their merits..."
- Use UK English spelling and conventions.
- Avoid marketing language. If a product claims to be "revolutionary", evaluate whether it actually is.
- When you're uncertain or the evidence is mixed, say so. Honest caveats build trust.
- Don't pad the guide with obvious filler. Every section should tell the reader something they didn't already know or help them make a better decision.
- Never use em dashes. Use a hyphen with a space either side " - " instead.
