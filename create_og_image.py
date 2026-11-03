# -*- coding: utf-8 -*-
"""
Generate a professional 1200x630 OpenGraph social preview banner for RouterIPHub.
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = r"C:\Users\acer\.gemini\antigravity\scratch\routeriphub\public"
ASSETS_DIR = os.path.join(OUTPUT_DIR, "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

WIDTH = 1200
HEIGHT = 630

# Create base image with dark technical gradient
img = Image.new("RGBA", (WIDTH, HEIGHT), (10, 15, 29, 255))
draw = ImageDraw.Draw(img)

# Draw subtle gradient overlay
for y in range(HEIGHT):
    # Gradient from (10, 15, 29) to (15, 23, 42)
    ratio = y / HEIGHT
    r = int(10 + (15 - 10) * ratio)
    g = int(15 + (23 - 15) * ratio)
    b = int(29 + (42 - 29) * ratio)
    draw.line([(0, y), (WIDTH, y)], fill=(r, g, b, 255))

# Draw subtle networking grid dots/lines
grid_color = (30, 41, 59, 120)
for x in range(40, WIDTH, 40):
    for y in range(40, HEIGHT, 40):
        draw.point((x, y), fill=grid_color)

# Draw top accent border line (vibrant blue gradient effect)
for x in range(WIDTH):
    alpha = int(255 * (1 - abs(x - WIDTH/2) / (WIDTH/2)))
    draw.line([(x, 0), (x, 4)], fill=(2, 132, 199, alpha))

# Load standard Windows system fonts or default fallback
try:
    font_bold_huge = ImageFont.truetype("segoeui.ttf", 64)
    font_bold_large = ImageFont.truetype("segoeuib.ttf", 54)
    font_semibold = ImageFont.truetype("segoeuib.ttf", 32)
    font_regular = ImageFont.truetype("segoeui.ttf", 24)
    font_small = ImageFont.truetype("segoeui.ttf", 18)
    font_mono = ImageFont.truetype("consola.ttf", 22)
except Exception:
    try:
        font_bold_huge = ImageFont.truetype("arialbd.ttf", 60)
        font_bold_large = ImageFont.truetype("arialbd.ttf", 50)
        font_semibold = ImageFont.truetype("arialbd.ttf", 30)
        font_regular = ImageFont.truetype("arial.ttf", 24)
        font_small = ImageFont.truetype("arial.ttf", 18)
        font_mono = ImageFont.truetype("cour.ttf", 22)
    except Exception:
        font_bold_huge = ImageFont.load_default()
        font_bold_large = ImageFont.load_default()
        font_semibold = ImageFont.load_default()
        font_regular = ImageFont.load_default()
        font_small = ImageFont.load_default()
        font_mono = ImageFont.load_default()

# 1. Pill Badge at Top Left
badge_x, badge_y = 80, 70
badge_w, badge_h = 440, 38
draw.rounded_rectangle([badge_x, badge_y, badge_x + badge_w, badge_y + badge_h], radius=19, fill=(2, 132, 199, 40), outline=(2, 132, 199, 180), width=1)
draw.text((badge_x + 20, badge_y + 8), "NETWORK HARDWARE & GATEWAY REFERENCE", font=font_small, fill=(56, 189, 248, 255))

# 2. Draw Vector-Style Router Icon beside Brand
icon_x, icon_y = 80, 140
# Stacked Router body 1
draw.rounded_rectangle([icon_x, icon_y + 10, icon_x + 60, icon_y + 36], radius=6, fill=(15, 23, 42, 255), outline=(2, 132, 199, 255), width=2)
draw.ellipse([icon_x + 12, icon_y + 20, icon_x + 18, icon_y + 26], fill=(56, 189, 248, 255))
draw.ellipse([icon_x + 26, icon_y + 20, icon_x + 32, icon_y + 26], fill=(56, 189, 248, 255))
draw.ellipse([icon_x + 40, icon_y + 20, icon_x + 46, icon_y + 26], fill=(56, 189, 248, 255))
# Stacked Router body 2
draw.rounded_rectangle([icon_x, icon_y + 44, icon_x + 60, icon_y + 70], radius=6, fill=(15, 23, 42, 255), outline=(2, 132, 199, 255), width=2)
draw.ellipse([icon_x + 12, icon_y + 54, icon_x + 18, icon_y + 60], fill=(56, 189, 248, 255))
draw.ellipse([icon_x + 26, icon_y + 54, icon_x + 32, icon_y + 60], fill=(56, 189, 248, 255))
draw.ellipse([icon_x + 40, icon_y + 54, icon_x + 46, icon_y + 60], fill=(34, 197, 94, 255)) # Green status
# Antennas
draw.line([(icon_x + 10, icon_y + 10), (icon_x + 10, icon_y - 12)], fill=(2, 132, 199, 255), width=3)
draw.line([(icon_x + 50, icon_y + 10), (icon_x + 50, icon_y - 12)], fill=(2, 132, 199, 255), width=3)

# Brand Title
draw.text((icon_x + 80, icon_y - 2), "RouterIPHub", font=font_bold_huge, fill=(255, 255, 255, 255))
draw.rounded_rectangle([icon_x + 490, icon_y + 14, icon_x + 560, icon_y + 46], radius=6, fill=(2, 132, 199, 50), outline=(2, 132, 199, 200), width=1)
draw.text((icon_x + 502, icon_y + 20), "2026", font=font_small, fill=(56, 189, 248, 255))

# 3. Main Headline & Subtitle
draw.text((80, 240), "The Definitive Default Router IP & Gateway Reference", font=font_semibold, fill=(241, 245, 249, 255))
draw.text((80, 290), "Search default logins, factory reset guides, LED codes & technical specs across 1,500+ models.", font=font_regular, fill=(148, 163, 184, 255))
draw.text((80, 330), "Featuring client-side Subnet Calculators, Wi-Fi QR Code generators, and local gateway diagnostics.", font=font_regular, fill=(148, 163, 184, 255))

# 4. Feature Badges Grid along bottom
card_y = 410
card_h = 100
cards = [
    ("📡 Hardware Models", "200+ Verified Specs", (2, 132, 199)),
    ("🏢 Gateway IP Hubs", "192.168.1.1 & 10.0.0.1", (16, 185, 129)),
    ("🛠️ Subnet Calculator", "CIDR & Host Ranges", (168, 85, 247)),
    ("📱 Wi-Fi QR Generator", "Encrypted WPA3 Signs", (234, 88, 12))
]

card_w = 240
gap = 20
start_x = 80

for i, (head, sub, color) in enumerate(cards):
    cx = start_x + i * (card_w + gap)
    draw.rounded_rectangle([cx, card_y, cx + card_w, card_y + card_h], radius=12, fill=(15, 23, 42, 220), outline=(30, 41, 59, 255), width=1)
    # colored accent bar
    draw.line([(cx + 16, card_y), (cx + 60, card_y)], fill=color, width=3)
    draw.text((cx + 16, card_y + 20), head, font=font_regular, fill=(255, 255, 255, 255))
    draw.text((cx + 16, card_y + 55), sub, font=font_small, fill=(148, 163, 184, 255))

# 5. Bottom Footer Branding
draw.line([(80, 560), (WIDTH - 80, 560)], fill=(30, 41, 59, 180), width=1)
draw.text((80, 580), "routeriphub.com — Open Networking Knowledgebase & Tool Suite", font=font_small, fill=(100, 116, 139, 255))
draw.text((WIDTH - 280, 580), "100% Free • Zero Tracking", font=font_small, fill=(56, 189, 248, 255))

# Save PNG
png_path_1 = os.path.join(OUTPUT_DIR, "og-image.png")
png_path_2 = os.path.join(ASSETS_DIR, "og-image.png")
img.save(png_path_1, "PNG", optimize=True)
img.save(png_path_2, "PNG", optimize=True)

print(f"Successfully generated {png_path_1} ({os.path.getsize(png_path_1)} bytes)")
