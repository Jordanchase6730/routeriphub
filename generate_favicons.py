# -*- coding: utf-8 -*-
"""
Generate complete professional Favicon suite for RouterIPHub:
- favicon.ico (16x16, 32x32, 48x48)
- favicon.svg (Vector, theme-adaptive)
- favicon-32x32.png
- favicon-16x16.png
- apple-touch-icon.png (180x180)
- android-chrome-192x192.png
- android-chrome-512x512.png
- site.webmanifest
"""
import os
import json
from PIL import Image, ImageDraw

PUBLIC_DIR = r"C:\Users\acer\.gemini\antigravity\scratch\routeriphub\public"

def draw_router_icon(size):
    """
    Draw a clean, crisp, high-contrast router icon on a rounded squircle.
    Optimized for high visibility across 16px to 512px.
    """
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Scale factor
    s = size / 512.0
    
    # 1. Background Squircle
    margin = int(16 * s)
    radius = int(110 * s)
    bg_box = [margin, margin, size - margin, size - margin]
    
    # Gradient or solid dark modern background
    draw.rounded_rectangle(bg_box, radius=radius, fill=(11, 18, 32, 255), outline=(2, 132, 199, 255), width=max(1, int(10 * s)))
    
    # 2. Upper Wi-Fi Signal Arches (Radio Waves)
    center_x = size // 2
    arc_center_y = int(220 * s)
    
    # Outer Arc
    r1 = int(110 * s)
    draw.arc([center_x - r1, arc_center_y - r1, center_x + r1, arc_center_y + r1], start=215, end=325, fill=(56, 189, 248, 255), width=max(2, int(20 * s)))
    
    # Inner Arc
    r2 = int(65 * s)
    draw.arc([center_x - r2, arc_center_y - r2, center_x + r2, arc_center_y + r2], start=215, end=325, fill=(2, 132, 199, 255), width=max(2, int(18 * s)))

    # Radio emitter center dot
    r_dot = max(2, int(10 * s))
    draw.ellipse([center_x - r_dot, int(210 * s) - r_dot, center_x + r_dot, int(210 * s) + r_dot], fill=(56, 189, 248, 255))
    
    # 3. Stacked Hardware Router Chassis
    # Top Router Box
    r_left = int(80 * s)
    r_right = size - int(80 * s)
    r_width = r_right - r_left
    
    top_y1 = int(250 * s)
    top_y2 = int(330 * s)
    draw.rounded_rectangle([r_left, top_y1, r_right, top_y2], radius=int(20 * s), fill=(20, 31, 51, 255), outline=(2, 132, 199, 255), width=max(1, int(12 * s)))
    
    # LED indicator dots on Top Router
    led_y_top = (top_y1 + top_y2) // 2
    led_r = max(2, int(12 * s))
    
    # LED 1 (Power - Blue)
    x1 = r_left + int(45 * s)
    draw.ellipse([x1 - led_r, led_y_top - led_r, x1 + led_r, led_y_top + led_r], fill=(56, 189, 248, 255))
    # LED 2 (Internet - Cyan)
    x2 = r_left + int(90 * s)
    draw.ellipse([x2 - led_r, led_y_top - led_r, x2 + led_r, led_y_top + led_r], fill=(56, 189, 248, 255))
    # LED 3 (Wireless - Green)
    x3 = r_left + int(135 * s)
    draw.ellipse([x3 - led_r, led_y_top - led_r, x3 + led_r, led_y_top + led_r], fill=(34, 197, 94, 255))
    # Horizontal Ethernet Port Slits on Right
    draw.rounded_rectangle([r_right - int(120 * s), led_y_top - int(6 * s), r_right - int(40 * s), led_y_top + int(6 * s)], radius=int(4 * s), fill=(56, 189, 248, 200))
    
    # Bottom Router Box
    bot_y1 = int(355 * s)
    bot_y2 = int(435 * s)
    draw.rounded_rectangle([r_left, bot_y1, r_right, bot_y2], radius=int(20 * s), fill=(20, 31, 51, 255), outline=(2, 132, 199, 255), width=max(1, int(12 * s)))
    
    # LED indicator dots on Bottom Router
    led_y_bot = (bot_y1 + bot_y2) // 2
    # LED 1 (Power - Blue)
    draw.ellipse([x1 - led_r, led_y_bot - led_r, x1 + led_r, led_y_bot + led_r], fill=(56, 189, 248, 255))
    # LED 2 (WAN - Green)
    draw.ellipse([x2 - led_r, led_y_bot - led_r, x2 + led_r, led_y_bot + led_r], fill=(34, 197, 94, 255))
    # LED 3 (LAN Active - Green)
    draw.ellipse([x3 - led_r, led_y_bot - led_r, x3 + led_r, led_y_bot + led_r], fill=(34, 197, 94, 255))
    # Port Slits on Right
    draw.rounded_rectangle([r_right - int(120 * s), led_y_bot - int(6 * s), r_right - int(40 * s), led_y_bot + int(6 * s)], radius=int(4 * s), fill=(56, 189, 248, 200))
    
    return img

def generate_all_favicons():
    print("Generating comprehensive Favicon suite...")
    
    # 1. Master 512x512 icon
    img_512 = draw_router_icon(512)
    path_512 = os.path.join(PUBLIC_DIR, "android-chrome-512x512.png")
    img_512.save(path_512, "PNG", optimize=True)
    print(f"Created: {path_512}")
    
    # 2. 192x192 Android icon
    img_192 = draw_router_icon(192)
    path_192 = os.path.join(PUBLIC_DIR, "android-chrome-192x192.png")
    img_192.save(path_192, "PNG", optimize=True)
    print(f"Created: {path_192}")
    
    # 3. 180x180 Apple Touch Icon
    img_180 = draw_router_icon(180)
    path_180 = os.path.join(PUBLIC_DIR, "apple-touch-icon.png")
    img_180.save(path_180, "PNG", optimize=True)
    print(f"Created: {path_180}")
    
    # 4. 32x32 PNG Favicon
    img_32 = draw_router_icon(32)
    path_32 = os.path.join(PUBLIC_DIR, "favicon-32x32.png")
    img_32.save(path_32, "PNG", optimize=True)
    print(f"Created: {path_32}")
    
    # 5. 16x16 PNG Favicon
    img_16 = draw_router_icon(16)
    path_16 = os.path.join(PUBLIC_DIR, "favicon-16x16.png")
    img_16.save(path_16, "PNG", optimize=True)
    print(f"Created: {path_16}")
    
    # 6. Multi-resolution favicon.ico (16, 32, 48)
    img_48 = draw_router_icon(48)
    ico_path = os.path.join(PUBLIC_DIR, "favicon.ico")
    img_48.save(ico_path, format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
    print(f"Created: {ico_path}")
    
    # 7. Scalable Vector favicon.svg (crisp on 4K / Retina / theme-aware)
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <linearGradient id="favBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b1220"/>
      <stop offset="100%" stop-color="#141f33"/>
    </linearGradient>
    <linearGradient id="favBlue" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#38bdf8"/>
    </linearGradient>
  </defs>

  <!-- Background Squircle -->
  <rect x="2" y="2" width="60" height="60" rx="14" fill="url(#favBg)" stroke="#0284c7" stroke-width="1.8"/>

  <!-- Wi-Fi Waves -->
  <path d="M 22 24 A 14 14 0 0 1 42 24" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 26 28 A 8 8 0 0 1 38 28" fill="none" stroke="#0284c7" stroke-width="2" stroke-linecap="round"/>
  <circle cx="32" cy="30" r="1.5" fill="#38bdf8"/>

  <!-- Top Router Chassis -->
  <rect x="10" y="34" width="44" height="10" rx="2.5" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
  <circle cx="16" cy="39" r="1.5" fill="#38bdf8"/>
  <circle cx="21" cy="39" r="1.5" fill="#38bdf8"/>
  <circle cx="26" cy="39" r="1.5" fill="#22c55e"/>
  <line x1="42" y1="39" x2="50" y2="39" stroke="#38bdf8" stroke-width="1.2" stroke-linecap="round"/>

  <!-- Bottom Router Chassis -->
  <rect x="10" y="47" width="44" height="10" rx="2.5" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
  <circle cx="16" cy="52" r="1.5" fill="#38bdf8"/>
  <circle cx="21" cy="52" r="1.5" fill="#22c55e"/>
  <circle cx="26" cy="52" r="1.5" fill="#22c55e"/>
  <line x1="42" y1="52" x2="50" y2="52" stroke="#38bdf8" stroke-width="1.2" stroke-linecap="round"/>
</svg>
"""
    svg_path = os.path.join(PUBLIC_DIR, "favicon.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Created: {svg_path}")

    # 8. Web App Manifest (site.webmanifest)
    manifest = {
        "name": "RouterIPHub",
        "short_name": "RouterIPHub",
        "description": "The Definitive Default Router IP & Gateway Reference",
        "icons": [
            {
                "src": "/android-chrome-192x192.png",
                "sizes": "192x192",
                "type": "image/png"
            },
            {
                "src": "/android-chrome-512x512.png",
                "sizes": "512x512",
                "type": "image/png"
            }
        ],
        "theme_color": "#0284c7",
        "background_color": "#0b1220",
        "display": "standalone",
        "start_url": "/"
    }
    manifest_path = os.path.join(PUBLIC_DIR, "site.webmanifest")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print(f"Created: {manifest_path}")

if __name__ == "__main__":
    generate_all_favicons()
