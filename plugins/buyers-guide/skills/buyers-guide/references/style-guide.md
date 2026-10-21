# Buyer's guide visual style

The guide has one visual identity and every element on the page, including photographs and generated illustrations, has to sit inside it. This file defines that identity. Read it whenever you are adding an image, drawing an SVG, or unsure how a component should look.

## Palette per category

The page structure, type and layout never change. The three accent colours do, so that a guide for a garden tool and a guide for a television read as issues of the same magazine with different cover art. Pick one palette from the table by the feel of the category, set the three hex values once in the template's `:root`, and use the same three values in every illustration prompt and SVG. Never mix palettes within a guide and never invent a fourth colour.

| Palette | Primary | Secondary | Highlight | Reach for it when |
|---|---|---|---|---|
| Circuit (default) | `#1f3fe0` cobalt | `#ff6b1a` tangerine | `#f2e84b` lemon | Tools, computing, general electronics, anything with no obvious character |
| Cinema | `#5b1fd6` violet | `#ff2e6a` magenta | `#39e6c8` mint | TVs, audio, cameras, gaming, home entertainment |
| Field | `#1c6b3a` forest | `#e0521c` rust | `#ffd23f` marigold | Garden, outdoor, agriculture, bikes, camping, anything used outside |
| Hearth | `#b23a1a` brick | `#1a4f7a` steel | `#f5c518` amber | Kitchen, appliances, heating, home improvement, furniture |
| Motion | `#0f2d6b` navy | `#e8262d` racing red | `#f4f4f4` white (use `#c9c9c9` for shapes) | Vehicles, EVs, e-bikes, drones, anything that moves |
| Ledger | `#0f4c5c` teal | `#e07a1f` copper | `#d9e8c4` sage | Software, subscriptions, financial products, services |

Primary carries the cover, score tiles, tile underlines, links and the best-overall step. Secondary carries the heading rule, the top score, the gotcha rule and the cover disc. Highlight carries the cover tag, the award badge, the TL;DR bold and the outlook panel. If a highlight is pale (Motion, Ledger), the outlook panel text stays `--ink` and remains readable; check it.

## Fixed tokens

| Token | Value | Use |
|---|---|---|
| `--bg` | `#f6f6f6` | Page background |
| `--card` | `#ffffff` | Every content block |
| `--ink` | `#111111` | Body text, table header, TL;DR block |
| `--grey` | `#666a70` | Meta text, captions, credits |
| `--line` | `#e2e3e6` | Rules, empty score track |
| `--good` / `--bad` | `#1a7f3c` / `#c0392b` | Owner praise and complaints only |

Type is Archivo, condensed (75% width) and black (900) for every heading, product name and score; normal width for body. Headings are uppercase. Nothing else is. Do not add fonts, gradients, drop shadows, rounded corners or colours beyond the chosen palette. The template already contains all the CSS; do not restyle it per guide.

## Which visual to use

Decide per concept, not per section:

- **Product photo** - every product that gets a card. Real photographs only.
- **AI illustration** - any concept that is easier to grasp when you can see it: how a component works, what a product type looks like next to another, a cutaway, a use-case scene, a scale comparison. This is the default for concept explanation.
- **Inline SVG** - charts (score comparison, price versus performance, run-time curves), simple tree diagrams (the category landscape), labelled schematic parts. Anything that is really data or boxes-and-arrows.
- **No image** - if a paragraph already explains it fully, do not add a picture. Two or three illustrations plus one or two SVGs is typical for a guide; ten is too many.

## Product photos

`image_search` shows pictures to the reader but does not return URLs, and manufacturer and retailer product pages are rendered in the browser, so a plain fetch of the page finds no product image. Two methods work; use them in this order.

1. **One Firecrawl agent job for the whole set.** Load `firecrawl_agent` and `firecrawl_agent_status` with `tool_search`, then run a single job listing every product with its exact model code and asking for (a) a direct URL to a clean front-view product photograph on white from the manufacturer's UK product page or a major UK retailer, ending in .jpg, .png or .webp or on a manufacturer image CDN, and (b) the current UK price with retailer name and page URL. Seed it with the manufacturer and retailer home pages. Give it a schema with `model`, `image_url`, `image_source`, `price_gbp`, `retailer`, `retailer_url`. Tell it to leave fields empty rather than guess. It takes one to three minutes; poll `firecrawl_agent_status` every 20 seconds and do the illustrations in the meantime. This also gives you the price line for every card in one go.
2. **og:image fallback for any product the job missed.** Fetch the manufacturer product page with a browser User-Agent and read the `og:image` meta tag. It is often a real product shot, and manufacturer CDN URLs usually accept a `wid=1200` or similar size parameter to get a larger version.

Download every photo, then look at them together on a contact sheet before using any. Reject: watermarked, under 600px on the long side after trimming, a lifestyle scene where the product is small, a dimension or line diagram, a photo of the wrong variant, or a screen showing a large brand slogan rather than content. Manufacturer CDN images often ship with a wide transparent canvas; `embed_images.py` trims transparent and white borders automatically, so judge the image after that trim, not before. A product-on-white cutout is ideal.

Put the URL or the local path in the card's `<img src>` and the source name (manufacturer or retailer) in the `.credit` line. If no usable photo exists after both methods, use the `.photo.missing` placeholder block rather than a poor image.

## AI illustrations

Generate through the `generate-image` skill (gpt-image-2 on Replicate). Every prompt must start with the house-style prefix below with the three palette placeholders filled from the palette you chose for the guide (name and hex, for example "violet #5b1fd6"), then describe the subject. The prefix is what makes the illustration look like it belongs on the page; do not shorten it.

```
Flat vector editorial illustration for a technology magazine buyer's guide. Pure white background, no gradients, no shadows, no texture, no photorealism. Strictly limited palette: {PRIMARY_NAME} {PRIMARY_HEX}, {SECONDARY_NAME} {SECONDARY_HEX}, {HIGHLIGHT_NAME} {HIGHLIGHT_HEX}, near-black #111111 for outlines and small labels, light grey #e2e3e6 for secondary shapes. Bold geometric shapes, thick uniform outlines, clean and diagrammatic, the style of a Stuff or T3 magazine explainer. Any labels in a condensed bold sans-serif, sentence case, minimal. No brand logos, no real product names, no people's faces.
```

Then add the subject, for example: `Subject: a cutaway of a brushless motor beside a brushed motor, showing the absence of carbon brushes, with two short labels.`

Parameters: `aspect_ratio` `3:2` for figures (matches the template width), `quality` `auto`, `output_format` `webp`, `number_of_images` 1. Download to `/home/claude/guide/img/` with a descriptive filename, reference it by relative path in the `<figure>`, and let `embed_images.py` inline it.

Check the result before using it. Regenerate once if the palette drifted (any colour that is not one of the three palette values, black, grey or white, or any gradient, means it drifted) or if the illustration is decorative rather than explanatory. If the second attempt still does not explain the concept, draw it as SVG instead or drop the figure.

Do not generate images of specific real products. The illustration explains the concept; the photograph shows the product.

## Inline SVG

Use `viewBox="0 0 700 260"` for a wide figure or `0 0 700 400` for a tree. Fill and stroke only with the token hex values. Text uses `font-family="Archivo, Arial, sans-serif"`, `font-weight="700"`, size 14 to 18, `fill="#111111"`. Strokes 3px. No filters, no gradients, no `<style>` blocks inside the SVG (they collide with the page CSS). Give every SVG a `role="img"` and `aria-label`.

A score bar chart is better done with the `.bars` component than with SVG. Use SVG when the chart has two axes or the shape is a diagram.

## Copy inside visuals

Captions are one sentence and say what the reader should take from the figure, not what the figure depicts. `<b>` at the start of the caption is a two or three word label ("Brushless explained", "Platform map"), not "Figure 1".
