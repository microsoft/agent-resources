#!/usr/bin/env python3
"""Generate the Open Graph social share image (1200x630) for the Microsoft
Agent Resources hub. Regenerates images/og-image.png.

Run: python3 scripts/generate_og_image.py
"""
from __future__ import annotations

import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"
OUT = IMAGES / "og-image-v2.png"

W, H = 1200, 630

# Brand palette (matches assets/css/styles.css :root)
BRAND_MID = (0, 61, 115)
BRAND_ACCENT = (0, 120, 212)
PURPLE = (70, 52, 135)
TEXT = (245, 248, 255)
MUTED = (176, 196, 222)


def vertical_gradient(size, top, bottom):
    img = Image.new("RGB", size, top)
    px = img.load()
    w, h = size
    for y in range(h):
        t = y / (h - 1)
        r = int(top[0] + (bottom[0] - top[0]) * t)
        g = int(top[1] + (bottom[1] - top[1]) * t)
        b = int(top[2] + (bottom[2] - top[2]) * t)
        for x in range(w):
            px[x, y] = (r, g, b)
    return img


def radial_glow(size, center, radius, color, alpha=180):
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    steps = 40
    for i in range(steps, 0, -1):
        r = int(radius * i / steps)
        a = int(alpha * (1 - i / steps) ** 2)
        d.ellipse(
            (center[0] - r, center[1] - r, center[0] + r, center[1] + r),
            fill=(*color, a),
        )
    return layer.filter(ImageFilter.GaussianBlur(radius=40))


def dot_grid(size, spacing=22, color=(255, 255, 255, 18), radius=1):
    w, h = size
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    for y in range(spacing, h, spacing):
        for x in range(spacing, w, spacing):
            d.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color)
    return layer


def load_font(size, bold=False):
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/SFNS.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for c in candidates:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                continue
    return ImageFont.load_default()


def fit_icon(path, box):
    im = Image.open(path).convert("RGBA")
    iw, ih = im.size
    scale = min(box / iw, box / ih)
    nw, nh = max(1, int(iw * scale)), max(1, int(ih * scale))
    return im.resize((nw, nh), Image.LANCZOS)


def rounded_badge(size, radius, fill, border=None, border_width=2):
    w, h = size
    im = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w - 1, h - 1), radius=radius, fill=fill)
    if border:
        d.rounded_rectangle((0, 0, w - 1, h - 1), radius=radius, outline=border, width=border_width)
    return im


def main():
    # 1) Base gradient background
    bg = vertical_gradient((W, H), (3, 10, 28), (10, 24, 58)).convert("RGBA")

    # 2) Aurora glows (soft color washes)
    bg.alpha_composite(radial_glow((W, H), (int(W * 0.85), int(H * 0.85)), 560, PURPLE, alpha=160))
    bg.alpha_composite(radial_glow((W, H), (int(W * 0.15), int(H * 0.20)), 520, BRAND_ACCENT, alpha=140))
    bg.alpha_composite(radial_glow((W, H), (int(W * 0.50), int(H * 0.55)), 420, BRAND_MID, alpha=90))

    # 3) Dot grid overlay
    bg.alpha_composite(dot_grid((W, H), spacing=22, color=(255, 255, 255, 20), radius=1))

    # 4) Subtle inner frame
    frame = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    fd = ImageDraw.Draw(frame)
    fd.rounded_rectangle((18, 18, W - 19, H - 19), radius=24, outline=(255, 255, 255, 30), width=2)
    bg.alpha_composite(frame)

    draw = ImageDraw.Draw(bg)

    # 5) Eyebrow pill
    eyebrow_font = load_font(20, bold=True)
    eyebrow = "MICROSOFT  ·  AGENTIC TRANSFORMATION"
    bb = draw.textbbox((0, 0), eyebrow, font=eyebrow_font)
    ew, eh = bb[2] - bb[0], bb[3] - bb[1]
    ex = (W - ew) / 2
    ey = 82
    pad_x, pad_y = 22, 10
    pill = rounded_badge((int(ew + pad_x * 2), int(eh + pad_y * 2)), 99,
                         fill=(255, 255, 255, 20), border=(255, 255, 255, 60), border_width=1)
    bg.alpha_composite(pill, (int(ex - pad_x), int(ey - pad_y)))
    draw.text((ex, ey - 4), eyebrow, font=eyebrow_font, fill=(215, 230, 255))

    # 6) Title with soft shadow
    title_font = load_font(82, bold=True)
    full_title = "Microsoft Agent Resources"
    tb = draw.textbbox((0, 0), full_title, font=title_font)
    tw, th = tb[2] - tb[0], tb[3] - tb[1]
    tx = (W - tw) / 2
    ty = 150
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.text((tx + 2, ty + 4), full_title, font=title_font, fill=(0, 0, 0, 150))
    shadow = shadow.filter(ImageFilter.GaussianBlur(6))
    bg.alpha_composite(shadow)
    draw.text((tx, ty), full_title, font=title_font, fill=TEXT)

    # 7) Subtitle
    subtitle_font = load_font(30)
    subtitle = "Build, deploy & manage AI agents across the Microsoft platform"
    sb = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    sw = sb[2] - sb[0]
    draw.text(((W - sw) / 2, ty + th + 28), subtitle, font=subtitle_font, fill=MUTED)

    # 8) Product row — five icon badges with labels
    products = [
        ("Microsoft 365 Copilot", IMAGES / "copilot-icon.png"),
        ("Copilot Studio", IMAGES / "copilot-studio-icon.png"),
        ("Microsoft Foundry", IMAGES / "foundry-icon.png"),
        ("Agent Framework", IMAGES / "agent-framework-icon.png"),
        ("Agent 365", IMAGES / "agent365-icon.png"),
    ]

    n = len(products)
    badge_size = 104
    icon_box = 68
    row_y = 410
    # Equal-width slots so long labels don't collide with neighbors.
    side_padding = 70
    slot_w = (W - 2 * side_padding) // n

    label_font = load_font(17, bold=True)

    for i, (label, icon_path) in enumerate(products):
        slot_cx = side_padding + slot_w * i + slot_w // 2
        bx = slot_cx - badge_size // 2
        by = row_y

        # soft blue glow behind badge
        glow = Image.new("RGBA", (badge_size + 80, badge_size + 80), (0, 0, 0, 0))
        gd = ImageDraw.Draw(glow)
        gd.rounded_rectangle((0, 0, badge_size + 79, badge_size + 79), radius=50,
                             fill=(0, 120, 212, 70))
        glow = glow.filter(ImageFilter.GaussianBlur(22))
        bg.alpha_composite(glow, (bx - 40, by - 40))

        badge = rounded_badge((badge_size, badge_size), 22,
                              fill=(255, 255, 255, 32),
                              border=(255, 255, 255, 95), border_width=1)
        bg.alpha_composite(badge, (bx, by))

        icon = fit_icon(icon_path, icon_box)
        ix = bx + (badge_size - icon.width) // 2
        iy = by + (badge_size - icon.height) // 2
        bg.alpha_composite(icon, (ix, iy))

        lb = draw.textbbox((0, 0), label, font=label_font)
        lw = lb[2] - lb[0]
        draw.text((slot_cx - lw / 2, by + badge_size + 16), label,
                  font=label_font, fill=(222, 234, 252))

    # 9) Footer
    foot_font = load_font(20)
    footer = "Microsoft Copilot Acceleration Team"
    fb = draw.textbbox((0, 0), footer, font=foot_font)
    fw = fb[2] - fb[0]
    draw.text(((W - fw) / 2, H - 52), footer, font=foot_font, fill=(150, 175, 210))

    out = bg.convert("RGB")
    out.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT} ({out.size})")


if __name__ == "__main__":
    main()
