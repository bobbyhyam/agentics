#!/usr/bin/env python3
"""
Inline every remote or local image referenced in a buyer's guide HTML file
as a base64 data URI, so the finished guide is a single self-contained file
that does not break when a retailer moves or removes a photo.

Why this exists: the guide is read inside the Claude mobile viewer, which
cannot be relied on to fetch external images, and product photo URLs on
retailer sites are routinely rotated. Embedding at build time is the only
way to guarantee the page looks the same in a year.

Usage:
    python3 embed_images.py guide.html [--max-dim 1200] [--out guide.html]

Behaviour:
  - Finds every <img src="..."> in the file.
  - Skips anything that is already a data: URI or an inline <svg>.
  - Downloads http(s) sources with a browser-like User-Agent; reads local
    paths directly.
  - Trims transparent or near-white borders (manufacturer CDN images often
    sit on a huge empty canvas), then downscales so the longest side is --max-dim pixels (default 1200; this
    keeps a ten-image guide comfortably under 2MB) and re-encodes as WebP
    where Pillow supports it, else keeps the original format.
  - Replaces the src attribute in place and writes the result to --out
    (defaults to overwriting the input).
  - Any image that fails to download is left as-is and reported on stderr
    with the URL, so you can swap it for another source or the placeholder
    card described in references/style-guide.md.
"""
import argparse
import base64
import io
import os
import re
import sys
import urllib.request

try:
    from PIL import Image
except ImportError:
    Image = None

IMG_RE = re.compile(r'(<img\b[^>]*?\bsrc=")([^"]+)(")', re.IGNORECASE)
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")


def fetch(src, base_dir):
    if src.startswith(("http://", "https://")):
        req = urllib.request.Request(src, headers={"User-Agent": UA, "Accept": "image/*,*/*"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read()
    path = src if os.path.isabs(src) else os.path.join(base_dir, src)
    with open(path, "rb") as f:
        return f.read()


def trim_borders(im, pad=12):
    """Crop transparent or near-white borders so CDN product shots with a wide
    empty canvas fill the card instead of shrinking to a thumbnail."""
    from PIL import ImageChops
    work = im.convert("RGBA")
    if work.getchannel("A").getextrema()[0] < 255:
        box = work.getbbox()
    else:
        rgb = work.convert("RGB")
        bg = Image.new("RGB", rgb.size, (255, 255, 255))
        diff = ImageChops.difference(rgb, bg).convert("L").point(lambda v: 255 if v > 12 else 0)
        box = diff.getbbox()
    if not box:
        return im
    l, t, r, b = box
    box = (max(l - pad, 0), max(t - pad, 0), min(r + pad, im.width), min(b + pad, im.height))
    if (box[2] - box[0]) * (box[3] - box[1]) < 0.9 * im.width * im.height:
        return im.crop(box)
    return im


def to_data_uri(raw, max_dim):
    if Image is None:
        mime = "image/png"
        return f"data:{mime};base64,{base64.b64encode(raw).decode()}"
    im = Image.open(io.BytesIO(raw))
    fmt = (im.format or "PNG").upper()
    im = trim_borders(im)
    if max_dim and max(im.size) > max_dim:
        im.thumbnail((max_dim, max_dim), Image.LANCZOS)
    buf = io.BytesIO()
    if fmt == "GIF":
        im.save(buf, format="GIF")
        mime = "image/gif"
    else:
        try:
            if im.mode not in ("RGB", "RGBA"):
                im = im.convert("RGBA" if "A" in im.mode else "RGB")
            im.save(buf, format="WEBP", quality=82, method=6)
            mime = "image/webp"
        except Exception:
            buf = io.BytesIO()
            im.convert("RGB").save(buf, format="JPEG", quality=85)
            mime = "image/jpeg"
    return f"data:{mime};base64,{base64.b64encode(buf.getvalue()).decode()}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--max-dim", type=int, default=1200)
    ap.add_argument("--out")
    args = ap.parse_args()

    base_dir = os.path.dirname(os.path.abspath(args.html))
    with open(args.html, encoding="utf-8") as f:
        html = f.read()

    done, failed = 0, []

    def repl(m):
        nonlocal done
        src = m.group(2)
        if src.startswith("data:"):
            return m.group(0)
        try:
            raw = fetch(src, base_dir)
            uri = to_data_uri(raw, args.max_dim)
            done += 1
            return f"{m.group(1)}{uri}{m.group(3)}"
        except Exception as e:
            failed.append((src, str(e)))
            return m.group(0)

    html = IMG_RE.sub(repl, html)
    out = args.out or args.html
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Embedded {done} image(s) into {out} ({os.path.getsize(out) // 1024} KB)")
    for src, err in failed:
        print(f"FAILED: {src} -> {err}", file=sys.stderr)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
