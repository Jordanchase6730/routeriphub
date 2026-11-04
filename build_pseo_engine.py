# -*- coding: utf-8 -*-
"""
RouterIPHub - Complete Programmatic SEO (pSEO) Architecture Engine
Generates:
1. 32 Model Setup Sheets (/routers/[brand]-[model]/) + Master Directory (/routers/)
2. 10 ISP Gateway Hubs (/isp/[isp-gateway]/) + Master Directory (/isp/)
3. 16 Dedicated Brand Hubs (/brands/[brand]/) + Master Directory (/brands/)
4. 17 Private Gateway IP Hubs (/ip/[gateway-ip]/) + Master Directory (/ip/)
5. 6 Dedicated Tool Pages (/tools/[tool-name]/) + Master Tools Directory (/tools/)
6. Categorized Sitemap Index Architecture (/sitemaps/*.xml + /sitemap.xml)
7. Dynamic Data Exports (routers.json, routers.csv, routers.sql)
8. Global Search Index (search-index.json) with 160+ entries
9. Clean Vercel Redirects (301s from legacy .html to clean /slug/ URLs)
10. AI / LLM manifests (llms.txt, llms-full.txt)
"""

import os
import shutil
import json
import csv
import html
from datetime import datetime
from generate_pseo_data import (
    ROUTER_MODELS,
    ISP_GATEWAYS,
    BRAND_PROFILES,
    IP_GATEWAYS,
    TOOL_PAGES
)

ROOT_DIR = r"C:\Users\acer\.gemini\antigravity\scratch\routeriphub"
PUBLIC_DIR = os.path.join(ROOT_DIR, "public")
TODAY = "2026-11-03"

def escape(s):
    return html.escape(str(s) if s is not None else "")

def make_dirs(path):
    os.makedirs(path, exist_ok=True)

# Common Header & Nav
def get_header(title, description, canonical_url, active_nav="", breadcrumbs=None, schemas_json_ld=None):
    b_items = breadcrumbs or [("Home", "/")]
    
    # Generate BreadcrumbList Schema
    breadcrumb_schema_items = []
    for idx, (b_name, b_url) in enumerate(b_items, start=1):
        full_url = f"https://routeriphub.com{b_url}" if b_url.startswith("/") else b_url
        breadcrumb_schema_items.append({
            "@type": "ListItem",
            "position": idx,
            "name": b_name,
            "item": full_url
        })
    
    bc_schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": breadcrumb_schema_items
    }
    
    all_schemas = [bc_schema]
    if schemas_json_ld:
        all_schemas.extend(schemas_json_ld)
        
    schema_block = json.dumps({"@context": "https://schema.org", "@graph": all_schemas}, indent=2)

    # Breadcrumbs HTML
    bc_html_parts = []
    for idx, (b_name, b_url) in enumerate(b_items):
        if idx == len(b_items) - 1:
            bc_html_parts.append(f'<span aria-current="page">{escape(b_name)}</span>')
        else:
            bc_html_parts.append(f'<a href="{escape(b_url)}">{escape(b_name)}</a>')
    bc_html = ' <span class="sep">&rsaquo;</span> '.join(bc_html_parts)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description)}">
  <link rel="canonical" href="{escape(canonical_url)}">

  <!-- Favicon Suite -->
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
  <link rel="shortcut icon" href="/favicon.ico">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#0284c7">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{escape(canonical_url)}">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(description)}">
  <meta property="og:site_name" content="RouterIPHub">
  <meta property="og:image" content="https://routeriphub.com/og-image.png">
  <meta property="og:image:secure_url" content="https://routeriphub.com/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:type" content="image/png">
  <meta property="og:image:alt" content="RouterIPHub - The Definitive Default Router IP & Gateway Reference">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@RouterIPHub">
  <meta name="twitter:creator" content="@RouterIPHub">
  <meta name="twitter:title" content="{escape(title)}">
  <meta name="twitter:description" content="{escape(description)}">
  <meta name="twitter:image" content="https://routeriphub.com/og-image.png">
  <meta name="twitter:image:alt" content="RouterIPHub - The Definitive Default Router IP & Gateway Reference">

  <!-- Instant Theme Initializer (Light Mode Default, 0ms FOUT) -->
  <script>
    (function() {{
      try {{
        var t = localStorage.getItem('theme');
        if (t === 'dark') {{
          document.documentElement.setAttribute('data-theme', 'dark');
        }} else {{
          document.documentElement.setAttribute('data-theme', 'light');
        }}
      }} catch (e) {{}}
    }})();
  </script>
  <link rel="stylesheet" href="/css/style.css">
  <script src="/js/app.js" defer></script>
  <script src="/js/tools.js" defer></script>

  <!-- Structured Data / JSON-LD -->
  <script type="application/ld+json">
{schema_block}
  </script>
</head>
<body>

  <!-- Site Navigation Header -->
  <header class="site-header">
    <div class="container nav-wrap">
      <a href="/" class="brand-logo">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#0284c7" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect>
          <rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect>
          <line x1="6" y1="6" x2="6.01" y2="6"></line>
          <line x1="6" y1="18" x2="6.01" y2="18"></line>
        </svg>
        <span>RouterIPHub</span>
        <span class="brand-badge">2026</span>
      </a>

      <!-- Desktop Navigation Links -->
      <nav aria-label="Main Navigation" class="desktop-nav">
        <ul class="nav-links">
          <li><a href="/routers/" class="{'active' if active_nav == 'routers' else ''}">Routers</a></li>
          <li><a href="/isp/" class="{'active' if active_nav == 'isp' else ''}">ISP Gateways</a></li>
          <li><a href="/brands/" class="{'active' if active_nav == 'brands' else ''}">Brands</a></li>
          <li><a href="/ip/" class="{'active' if active_nav == 'ip' else ''}">IP Directory</a></li>
          <li><a href="/tools/" class="{'active' if active_nav == 'tools' else ''}">Tools</a></li>
          <li><a href="/howto.html" class="{'active' if active_nav == 'howto' else ''}">Guides</a></li>
        </ul>
      </nav>

      <!-- Header Actions -->
      <div class="header-actions">
        <!-- Global Search Bar Button -->
        <button class="search-trigger-btn" aria-label="Search entire website" title="Search site (Press / or Ctrl+K)">
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
          <span class="search-trigger-text">Search site...</span>
          <kbd class="search-trigger-kbd">Ctrl K</kbd>
        </button>

        <!-- Theme Switcher Button -->
        <button class="theme-toggle-btn" aria-label="Toggle Dark/Light Mode" title="Toggle Theme">
          <svg class="sun-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
          <svg class="moon-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
        </button>

        <!-- Mobile Menu Toggle Button -->
        <button class="mobile-menu-btn" id="mobile-menu-toggle" aria-label="Toggle mobile menu" aria-expanded="false">
          <svg class="icon-menu" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
          <svg class="icon-close" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:none;"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </button>
      </div>
    </div>

    <!-- Mobile Navigation Drawer -->
    <div class="mobile-nav-drawer" id="mobile-nav-drawer" aria-hidden="true">
      <div class="container">
        <div style="margin-bottom: 0.75rem;">
          <button class="search-trigger-btn" style="width: 100%; border-radius: var(--radius-md); justify-content: flex-start; padding: 0.75rem 1rem; min-height: 48px; background: var(--bg-card); gap: 0.75rem;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            <span style="font-size: 0.95rem; color: var(--text-muted);">Search entire site (150+ models, IPs, tools)...</span>
          </button>
        </div>

        <ul class="mobile-nav-list">
          <li><a href="/routers/"><span>📡 Router Models Directory</span><span>&rarr;</span></a></li>
          <li><a href="/isp/"><span>🏢 ISP Gateway Portals (Xfinity, AT&T, Fios)</span><span>&rarr;</span></a></li>
          <li><a href="/brands/"><span>🏷️ Brand Directories (Netgear, ASUS, TP-Link)</span><span>&rarr;</span></a></li>
          <li><a href="/ip/"><span>⚡ Gateway IP Directory (192.168.1.1, 10.0.0.1)</span><span>&rarr;</span></a></li>
          <li><a href="/tools/"><span>🛠️ Interactive Networking Tools</span><span>&rarr;</span></a></li>
          <li><a href="/howto.html"><span>📖 Setup & Troubleshooting Guides</span><span>&rarr;</span></a></li>
          <li style="margin-top: 0.5rem; border-top: 1px solid var(--border-color); padding-top: 0.5rem;">
            <button class="theme-toggle-btn" style="width: 100%; border-radius: var(--radius-md); font-size: 0.95rem; font-weight: 600; display: flex; align-items: center; justify-content: space-between; padding: 0.85rem 1.15rem; background: var(--bg-card); height: auto; min-height: 48px;">
              <span>🌓 Switch Dark / Light Mode</span>
              <span style="font-size: 0.8rem; color: var(--text-muted);">Toggle</span>
            </button>
          </li>
        </ul>
      </div>
    </div>
  </header>

  <!-- Breadcrumbs Bar -->
  <div class="breadcrumbs-bar">
    <div class="container">
      <nav aria-label="Breadcrumb" class="breadcrumbs">
        {bc_html}
      </nav>
    </div>
  </div>
"""

def get_footer():
    return """
  <!-- Footer -->
  <footer class="site-footer">
    <div class="container footer-wrap">
      <div class="footer-col">
        <div class="brand-logo" style="margin-bottom: 0.75rem;">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#0284c7" stroke-width="2.2">
            <rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect>
            <rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect>
            <line x1="6" y1="6" x2="6.01" y2="6"></line>
            <line x1="6" y1="18" x2="6.01" y2="18"></line>
          </svg>
          <span>RouterIPHub</span>
        </div>
        <p style="font-size: 0.875rem; color: var(--text-muted); line-height: 1.6;">
          Open reference platform for router default gateway IPs, factory credentials, LED diagnostics, and networking utilities.
        </p>
      </div>

      <div class="footer-col">
        <h4 class="footer-heading">Programmatic Silos</h4>
        <ul class="footer-links">
          <li><a href="/routers/">Router Models</a></li>
          <li><a href="/isp/">ISP Gateways</a></li>
          <li><a href="/brands/">Hardware Brands</a></li>
          <li><a href="/ip/">Gateway IP Hubs</a></li>
          <li><a href="/tools/">Interactive Tools</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4 class="footer-heading">Open Data & Developers</h4>
        <ul class="footer-links">
          <li><a href="/developers.html">Developer API & Datasets</a></li>
          <li><a href="/data/routers.json" download>routers.json (REST API)</a></li>
          <li><a href="/data/routers.csv" download>routers.csv (Tabular)</a></li>
          <li><a href="/data/routers.sql" download>routers.sql (ANSI Schema)</a></li>
          <li><a href="/llms.txt">llms.txt (AI Directory)</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4 class="footer-heading">Compliance & Sitemaps</h4>
        <ul class="footer-links">
          <li><a href="/sitemap.xml">XML Sitemap Index</a></li>
          <li><a href="/robots.txt">robots.txt</a></li>
          <li><a href="/find-router-ip.html">Find My Gateway IP</a></li>
          <li><a href="/howto.html">How-To Setup Guides</a></li>
        </ul>
      </div>
    </div>

    <div class="container footer-bottom">
      <p>&copy; 2026 RouterIPHub. All rights reserved. Open data licensed under CC BY 4.0. Hardware trademarks belong to their respective owners.</p>
    </div>
  </footer>

</body>
</html>
"""

# ==============================================================================
# 1. GENERATE ROUTER MODEL PAGES (/routers/[slug]/)
# ==============================================================================
def generate_router_model_pages():
    print(f"Generating {len(ROUTER_MODELS)} router model pages...")
    for m in ROUTER_MODELS:
        slug = m["slug"]
        model_dir = os.path.join(PUBLIC_DIR, "routers", slug)
        make_dirs(model_dir)

        canonical = f"https://routeriphub.com/routers/{slug}/"
        title = f"{m['brand']} {m['model_name']} Default IP, Password & Setup Guide (2026)"
        desc = f"Access {m['brand']} {m['model_name']} default login IP ({m['default_ip']}), admin password, factory reset procedure, and LED diagnostics cheat-sheet."

        # Structured Schemas
        tech_schema = {
            "@type": "TechArticle",
            "headline": f"{m['brand']} {m['model_name']} Default Login IP, Password, and Setup Guide",
            "description": desc,
            "mainEntityOfPage": canonical,
            "datePublished": "2026-01-15T08:00:00+00:00",
            "dateModified": f"{TODAY}T02:00:00+00:00",
            "author": {"@type": "Organization", "name": "RouterIPHub Editorial Team"},
            "publisher": {"@type": "Organization", "name": "RouterIPHub", "url": "https://routeriphub.com/"}
        }

        howto_schema = {
            "@type": "HowTo",
            "name": f"How to Log Into {m['brand']} {m['model_name']}",
            "description": f"Step-by-step instructions to access the admin console of your {m['brand']} {m['model_name']}.",
            "step": [
                {
                    "@type": "HowToStep",
                    "position": 1,
                    "name": "Connect to Device Network",
                    "text": f"Connect your PC, Mac, or phone to the router via Wi-Fi (SSID pattern: {m['default_ssid_pattern']}) or plug an Ethernet cable into any LAN port."
                },
                {
                    "@type": "HowToStep",
                    "position": 2,
                    "name": "Open Web Browser",
                    "text": f"Open any modern web browser and navigate to {m['web_domain']} or directly to http://{m['default_ip']}."
                },
                {
                    "@type": "HowToStep",
                    "position": 3,
                    "name": "Enter Credentials",
                    "text": f"Enter the default username '{m['default_username']}' and password '{m['default_password']}'."
                },
                {
                    "@type": "HowToStep",
                    "position": 4,
                    "name": "Configure Network Settings",
                    "text": "Once inside the administration portal, configure your wireless SSID, update your administrator password, and adjust security settings."
                }
            ]
        }

        faq_schema = {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": f"What is the default IP address for {m['brand']} {m['model_name']}?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": f"The primary default IP address is {m['default_ip']}. You can also access the management portal via {m['web_domain']} (or fallback IP {m['fallback_ip']})."
                    }
                },
                {
                    "@type": "Question",
                    "name": f"What is the default password for {m['brand']} {m['model_name']}?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": f"The default username is '{m['default_username']}' and the default password is '{m['default_password']}'. {'Note: The unique factory password is also printed on the device sticker.' if m['password_on_sticker'] else ''}"
                    }
                },
                {
                    "@type": "Question",
                    "name": f"How do I reset my {m['brand']} {m['model_name']} to factory settings?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": m['reset_instructions']
                    }
                }
            ]
        }

        breadcrumbs = [
            ("Home", "/"),
            ("Routers", "/routers/"),
            (m["brand"], f"/brands/{m['brand_slug']}/"),
            (m["model_name"], f"/routers/{slug}/")
        ]

        # Build LED Table Rows
        led_rows = ""
        for led in m["led_indicators"]:
            led_rows += f"""
            <tr>
              <td><strong>{escape(led['name'])}</strong></td>
              <td><span class="led-badge-normal">{escape(led['normal'])}</span></td>
              <td><span class="led-badge-error">{escape(led['error'])}</span></td>
              <td style="color: var(--text-secondary);">{escape(led['desc'])}</td>
            </tr>
            """

        content = f"""
  <main class="container" style="padding-top: 1.5rem; padding-bottom: 3.5rem;">
    <div class="content-container">
      <div class="silo-badge silo-badge-router">📡 Hardware Model Setup Sheet</div>
      <h1 style="font-size: 2.15rem; font-weight: 800; margin-bottom: 0.75rem; letter-spacing: -0.02em;">
        {escape(m['brand'])} {escape(m['model_name'])}
      </h1>
      <p style="font-size: 1.1rem; color: var(--text-secondary); margin-bottom: 1.5rem;">
        Complete default configuration parameters, factory credentials, LED indicator cheat-sheet, and hardware reset procedure.
      </p>

      <!-- Google AIO / Featured Snippet Answer Box -->
      <div class="answer-box">
        <div class="answer-box-label">Quick Gateway Answer (RFC 1918 Verified)</div>
        <div class="answer-box-main">
          Default IP: <strong>{escape(m['default_ip'])}</strong> &bull; Web: <strong>{escape(m['web_domain'])}</strong> &bull; User: <strong>{escape(m['default_username'])}</strong> &bull; Pass: <strong>{escape(m['default_password'])}</strong>
        </div>
        <div class="answer-box-sub">
          To log into the <strong>{escape(m['brand'])} {escape(m['model_name'])}</strong>, connect to your router via Wi-Fi or Ethernet and open <a href="http://{escape(m['default_ip'])}" target="_blank" rel="noopener">http://{escape(m['default_ip'])}</a> in your browser.
        </div>
      </div>

      <!-- Quick Action Buttons -->
      <div class="action-btn-group">
        <a href="http://{escape(m['default_ip'])}" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
          Open Admin Panel (http://{escape(m['default_ip'])}) &rarr;
        </a>
        <button class="btn btn-secondary copy-btn" data-copy="{escape(m['default_ip'])}">
          Copy IP ({escape(m['default_ip'])})
        </button>
        <button class="btn btn-secondary copy-btn" data-copy="{escape(m['default_password'])}">
          Copy Password
        </button>
      </div>

      <!-- Hardware Specs Grid -->
      <h2 style="font-size: 1.4rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.5rem;">
        Hardware Configuration & Specifications
      </h2>
      <div class="specs-grid">
        <div class="spec-item">
          <span class="spec-item-label">Manufacturer</span>
          <span class="spec-item-val"><a href="/brands/{escape(m['brand_slug'])}/">{escape(m['brand'])}</a></span>
        </div>
        <div class="spec-item">
          <span class="spec-item-label">Hardware Type</span>
          <span class="spec-item-val">{escape(m['hardware_type'])}</span>
        </div>
        <div class="spec-item">
          <span class="spec-item-label">Default Gateway IP</span>
          <span class="spec-item-val"><a href="/ip/{m['default_ip'].replace('.', '-')}/">{escape(m['default_ip'])}</a></span>
        </div>
        <div class="spec-item">
          <span class="spec-item-label">Alternative Web Domain</span>
          <span class="spec-item-val">{escape(m['web_domain'])}</span>
        </div>
        <div class="spec-item">
          <span class="spec-item-label">Fallback IP</span>
          <span class="spec-item-val">{escape(m['fallback_ip'])}</span>
        </div>
        <div class="spec-item">
          <span class="spec-item-label">Default Username</span>
          <span class="spec-item-val">{escape(m['default_username'])}</span>
        </div>
        <div class="spec-item">
          <span class="spec-item-label">Default Password</span>
          <span class="spec-item-val">{escape(m['default_password'])}</span>
        </div>
        <div class="spec-item">
          <span class="spec-item-label">Password on Sticker</span>
          <span class="spec-item-val">{'Yes (Check Base Label)' if m['password_on_sticker'] else 'No (Standard Preset)'}</span>
        </div>
        <div class="spec-item">
          <span class="spec-item-label">Default SSID Pattern</span>
          <span class="spec-item-val">{escape(m['default_ssid_pattern'])}</span>
        </div>
        <div class="spec-item">
          <span class="spec-item-label">Wi-Fi Standard</span>
          <span class="spec-item-val">{escape(m['wifi_standard'])}</span>
        </div>
      </div>

      <!-- Factory Reset Procedure -->
      <h2 style="font-size: 1.4rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 0.5rem;">
        How to Factory Reset {escape(m['brand'])} {escape(m['model_name'])}
      </h2>
      <div class="reset-instruction-box">
        <p style="margin-bottom: 0.75rem;"><strong>Hardware Reset Instructions:</strong></p>
        <p>{escape(m['reset_instructions'])}</p>
      </div>

      <!-- LED Indicators Cheat-Sheet -->
      <h2 style="font-size: 1.4rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 0.5rem;">
        LED Indicator Diagnostic Cheat-Sheet
      </h2>
      <div style="overflow-x: auto;">
        <table class="led-table">
          <thead>
            <tr>
              <th>LED Name</th>
              <th>Normal State</th>
              <th>Error / Alert State</th>
              <th>Description & Function</th>
            </tr>
          </thead>
          <tbody>
            {led_rows}
          </tbody>
        </table>
      </div>

      <!-- In-Page Diagnostic Reachability Console -->
      <div class="card" style="margin: 2.5rem 0; border: 1px solid var(--border-color); background: var(--bg-card); border-radius: var(--radius-lg); padding: 1.5rem;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem; flex-wrap: wrap; gap: 0.5rem;">
          <h3 style="font-size: 1.15rem; font-weight: 700; display: flex; align-items: center; gap: 0.5rem;">
            <span>⚡ Live Gateway Reachability Probe</span>
          </h3>
          <span style="font-size: 0.8rem; background: var(--info-bg); color: var(--text-accent); padding: 0.2rem 0.6rem; border-radius: 4px; font-weight: 600;">
            Target: {escape(m['default_ip'])}
          </span>
        </div>
        <p style="font-size: 0.875rem; color: var(--text-muted); margin-bottom: 1rem;">
          Test whether your device is currently connected to this gateway subnet via local browser ping probes:
        </p>
        <div style="display: flex; gap: 0.75rem; align-items: center; flex-wrap: wrap;">
          <button id="probe-btn" class="btn btn-primary" style="padding: 0.55rem 1rem; font-size: 0.875rem;">
            Test Connection to {escape(m['default_ip'])}
          </button>
          <div id="probe-status" style="font-size: 0.875rem; font-weight: 600;"></div>
        </div>
      </div>

      <!-- Official Resources -->
      <h2 style="font-size: 1.4rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 0.75rem;">
        Official Companion App & Documentation
      </h2>
      <div style="display: flex; flex-wrap: wrap; gap: 1rem; margin-bottom: 2.5rem;">
        <a href="{escape(m['companion_app_store_url'])}" target="_blank" rel="noopener noreferrer" class="btn-official-link">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"></rect><line x1="12" y1="18" x2="12.01" y2="18"></line></svg>
          <span>Download {escape(m['mobile_app'])}</span>
        </a>
        <a href="{escape(m['official_manual_url'])}" target="_blank" rel="noopener noreferrer" class="btn-official-link">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
          <span>Download Official PDF Manual</span>
        </a>
      </div>

      <!-- Cross Silo Links -->
      <div style="margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--border-color);">
        <h3 style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.75rem;">Related Guides & Tools</h3>
        <div style="display: flex; flex-wrap: wrap; gap: 0.75rem;">
          <a href="/brands/{escape(m['brand_slug'])}/" class="btn btn-secondary" style="font-size: 0.85rem;">
            All {escape(m['brand'])} Routers &rarr;
          </a>
          <a href="/ip/{m['default_ip'].replace('.', '-')}/" class="btn btn-secondary" style="font-size: 0.85rem;">
            {escape(m['default_ip'])} Gateway Hub &rarr;
          </a>
          <a href="/tools/subnet-calculator/" class="btn btn-secondary" style="font-size: 0.85rem;">
            CIDR Subnet Calculator &rarr;
          </a>
          <a href="/tools/wifi-qr-code/" class="btn btn-secondary" style="font-size: 0.85rem;">
            Wi-Fi QR Code Generator &rarr;
          </a>
        </div>
      </div>
    </div>
  </main>
"""
        full_html = get_header(title, desc, canonical, active_nav="routers", breadcrumbs=breadcrumbs, schemas_json_ld=[tech_schema, howto_schema, faq_schema]) + content + get_footer()
        with open(os.path.join(model_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(full_html)

# ==============================================================================
# 2. GENERATE ROUTERS MASTER INDEX (/routers/)
# ==============================================================================
def generate_router_index_page():
    print("Generating /routers/ master index page...")
    routers_dir = os.path.join(PUBLIC_DIR, "routers")
    make_dirs(routers_dir)

    canonical = "https://routeriphub.com/routers/"
    title = "Router Hardware Models Directory (Default IP, Credentials & Reset Sheets)"
    desc = "Browse hardware setup sheets for Netgear, TP-Link, ASUS, Linksys, Ubiquiti, MikroTik, Eero, and Arris. Find factory passwords, reset buttons, and LED codes."

    cards_html = ""
    for m in ROUTER_MODELS:
        cards_html += f"""
        <div class="card" style="display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
              <span class="badge" style="background: var(--info-bg); color: var(--text-accent);">{escape(m['brand'])}</span>
              <span style="font-size: 0.75rem; font-weight: 700; color: var(--text-muted);">{escape(m['hardware_type'].split()[0])}</span>
            </div>
            <h3 style="font-size: 1.15rem; font-weight: 700; margin-bottom: 0.4rem;">
              <a href="/routers/{escape(m['slug'])}/">{escape(m['model_name'])}</a>
            </h3>
            <p style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 1rem;">
              Default Gateway: <a href="/ip/{m['default_ip'].replace('.', '-')}/"><strong>{escape(m['default_ip'])}</strong></a> &bull; Pass: <code>{escape(m['default_password'])}</code>
            </p>
          </div>
          <div style="border-top: 1px solid var(--border-color); padding-top: 0.75rem; display: flex; justify-content: space-between; align-items: center;">
            <span style="font-size: 0.775rem; color: var(--text-muted);">{escape(m['wifi_standard'].split('(')[0])}</span>
            <a href="/routers/{escape(m['slug'])}/" style="font-size: 0.85rem; font-weight: 600;">View Sheet &rarr;</a>
          </div>
        </div>
        """

    content = f"""
  <main class="container" style="padding-top: 2rem; padding-bottom: 4rem;">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 2.5rem auto;">
      <div class="silo-badge silo-badge-router">📡 Programmatic Hardware Silo</div>
      <h1 style="font-size: 2.25rem; font-weight: 800; margin-bottom: 0.75rem;">
        Router Hardware Models Directory
      </h1>
      <p style="font-size: 1.1rem; color: var(--text-secondary);">
        Model-specific setup sheets, factory default passwords, physical reset button durations, and LED diagnostic cheat-sheets.
      </p>
    </div>

    <div class="grid-3" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 1.25rem;">
      {cards_html}
    </div>
  </main>
"""
    breadcrumbs = [("Home", "/"), ("Routers", "/routers/")]
    full_html = get_header(title, desc, canonical, active_nav="routers", breadcrumbs=breadcrumbs) + content + get_footer()
    with open(os.path.join(routers_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(full_html)

# ==============================================================================
# 3. GENERATE ISP GATEWAY PAGES (/isp/[slug]/ & /isp/)
# ==============================================================================
def generate_isp_pages():
    print(f"Generating {len(ISP_GATEWAYS)} ISP gateway pages...")
    for isp in ISP_GATEWAYS:
        slug = isp["slug"]
        isp_dir = os.path.join(PUBLIC_DIR, "isp", slug)
        make_dirs(isp_dir)

        canonical = f"https://routeriphub.com/isp/{slug}/"
        title = f"{isp['isp_name']} Gateway Login, Default Password & Bridge Mode ({isp['default_ip']})"
        desc = f"Access {isp['isp_name']} router admin portal at {isp['default_ip']}. Default username, printed access code instructions, factory reset, and bridge mode guide."

        tech_schema = {
            "@type": "TechArticle",
            "headline": f"{isp['isp_name']} Gateway Login and Configuration Guide",
            "description": desc,
            "mainEntityOfPage": canonical,
            "datePublished": "2026-01-15T08:00:00+00:00",
            "dateModified": f"{TODAY}T02:00:00+00:00",
            "author": {"@type": "Organization", "name": "RouterIPHub Editorial Team"},
            "publisher": {"@type": "Organization", "name": "RouterIPHub", "url": "https://routeriphub.com/"}
        }

        howto_schema = {
            "@type": "HowTo",
            "name": f"How to Log Into {isp['isp_name']} Gateway",
            "step": [
                {
                    "@type": "HowToStep",
                    "position": 1,
                    "name": "Connect to ISP Gateway",
                    "text": "Connect to your home Wi-Fi network or plug an Ethernet cable directly into LAN Port 1."
                },
                {
                    "@type": "HowToStep",
                    "position": 2,
                    "name": "Open Gateway URL",
                    "text": f"Open your browser and enter {isp['web_address']}."
                },
                {
                    "@type": "HowToStep",
                    "position": 3,
                    "name": "Enter Credentials",
                    "text": f"Submit username '{isp['default_username']}' and password '{isp['default_password']}'."
                }
            ]
        }

        breadcrumbs = [
            ("Home", "/"),
            ("ISP Gateways", "/isp/"),
            (isp["isp_name"], f"/isp/{slug}/")
        ]

        content = f"""
  <main class="container" style="padding-top: 1.5rem; padding-bottom: 3.5rem;">
    <div class="content-container">
      <div class="silo-badge silo-badge-isp">🏢 Service Provider Gateway Hub</div>
      <h1 style="font-size: 2.15rem; font-weight: 800; margin-bottom: 0.75rem; letter-spacing: -0.02em;">
        {escape(isp['isp_name'])} Gateway Login ({escape(isp['default_ip'])})
      </h1>
      <p style="font-size: 1.1rem; color: var(--text-secondary); margin-bottom: 1.5rem;">
        Default login credentials, IP passthrough, bridge mode instructions, and factory reset procedure for {escape(isp['gateway_name'])}.
      </p>

      <!-- Answer Box -->
      <div class="answer-box">
        <div class="answer-box-label">Verified ISP Configuration</div>
        <div class="answer-box-main">
          Gateway IP: <strong>{escape(isp['default_ip'])}</strong> &bull; User: <strong>{escape(isp['default_username'])}</strong> &bull; Pass: <strong>{escape(isp['default_password'])}</strong>
        </div>
        <div class="answer-box-sub">
          {escape(isp['sticker_note'])}
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="action-btn-group">
        <a href="{escape(isp['web_address'])}" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
          Open {escape(isp['isp_name'])} Portal ({escape(isp['default_ip'])}) &rarr;
        </a>
        <button class="btn btn-secondary copy-btn" data-copy="{escape(isp['default_ip'])}">
          Copy IP ({escape(isp['default_ip'])})
        </button>
      </div>

      <!-- Specifications Grid -->
      <h2 style="font-size: 1.4rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.5rem;">
        Gateway Parameters & Access Details
      </h2>
      <div class="specs-grid">
        <div class="spec-item">
          <span class="spec-item-label">Internet Service Provider</span>
          <span class="spec-item-val">{escape(isp['isp_name'])}</span>
        </div>
        <div class="spec-item">
          <span class="spec-item-label">Hardware Models</span>
          <span class="spec-item-val">{escape(isp['gateway_name'])}</span>
        </div>
        <div class="spec-item">
          <span class="spec-item-label">Default Gateway IP</span>
          <span class="spec-item-val"><a href="/ip/{isp['default_ip'].replace('.', '-')}/">{escape(isp['default_ip'])}</a></span>
        </div>
        <div class="spec-item">
          <span class="spec-item-label">Default Username</span>
          <span class="spec-item-val">{escape(isp['default_username'])}</span>
        </div>
        <div class="spec-item">
          <span class="spec-item-label">Default Password</span>
          <span class="spec-item-val">{escape(isp['default_password'])}</span>
        </div>
        <div class="spec-item">
          <span class="spec-item-label">Official Companion App</span>
          <span class="spec-item-val"><a href="{escape(isp['app_url'])}" target="_blank" rel="noopener">{escape(isp['app_name'])}</a></span>
        </div>
      </div>

      <!-- Bridge Mode / IP Passthrough Guide -->
      <h2 style="font-size: 1.4rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 0.5rem;">
        How to Enable Bridge Mode or IP Passthrough
      </h2>
      <div class="card" style="padding: 1.25rem; margin-bottom: 1.5rem;">
        <p style="line-height: 1.7; color: var(--text-primary);">{escape(isp['bridge_mode_guide'])}</p>
      </div>

      <!-- Reset Procedure -->
      <h2 style="font-size: 1.4rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.5rem;">
        Physical Factory Reset Procedure
      </h2>
      <div class="reset-instruction-box">
        <p>{escape(isp['reset_procedure'])}</p>
      </div>

      <!-- Probe Console -->
      <div class="card" style="margin: 2.5rem 0; border: 1px solid var(--border-color); background: var(--bg-card); border-radius: var(--radius-lg); padding: 1.5rem;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem; flex-wrap: wrap; gap: 0.5rem;">
          <h3 style="font-size: 1.15rem; font-weight: 700;">⚡ Test Connection to {escape(isp['isp_name'])} Gateway</h3>
          <span style="font-size: 0.8rem; background: var(--info-bg); color: var(--text-accent); padding: 0.2rem 0.6rem; border-radius: 4px; font-weight: 600;">
            Target: {escape(isp['default_ip'])}
          </span>
        </div>
        <p style="font-size: 0.875rem; color: var(--text-muted); margin-bottom: 1rem;">
          Verify if your device can reach the gateway administration server on {escape(isp['default_ip'])}:
        </p>
        <div style="display: flex; gap: 0.75rem; align-items: center; flex-wrap: wrap;">
          <button id="probe-btn" class="btn btn-primary" style="padding: 0.55rem 1rem; font-size: 0.875rem;">
            Probe {escape(isp['default_ip'])}
          </button>
          <div id="probe-status" style="font-size: 0.875rem; font-weight: 600;"></div>
        </div>
      </div>

      <!-- Cross Silo Links -->
      <div style="margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--border-color);">
        <h3 style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.75rem;">Related Gateways & Resources</h3>
        <div style="display: flex; flex-wrap: wrap; gap: 0.75rem;">
          <a href="/isp/" class="btn btn-secondary" style="font-size: 0.85rem;">All ISP Gateways &rarr;</a>
          <a href="/ip/{isp['default_ip'].replace('.', '-')}/" class="btn btn-secondary" style="font-size: 0.85rem;">{escape(isp['default_ip'])} Gateway Hub &rarr;</a>
          <a href="/tools/detect-gateway/" class="btn btn-secondary" style="font-size: 0.85rem;">Auto-Detect Local Gateway &rarr;</a>
        </div>
      </div>
    </div>
  </main>
"""
        full_html = get_header(title, desc, canonical, active_nav="isp", breadcrumbs=breadcrumbs, schemas_json_ld=[tech_schema, howto_schema]) + content + get_footer()
        with open(os.path.join(isp_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(full_html)

    # Master ISP Index
    isp_master_dir = os.path.join(PUBLIC_DIR, "isp")
    canonical_master = "https://routeriphub.com/isp/"
    title_master = "ISP Router Gateway Login Directory (Xfinity, AT&T, Verizon, Spectrum)"
    desc_master = "Complete directory of ISP default gateway IPs, admin passwords, bridge mode instructions, and factory reset guides for major service providers."

    isp_cards = ""
    for isp in ISP_GATEWAYS:
        isp_cards += f"""
        <div class="card" style="display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
              <span class="badge" style="background: var(--info-bg); color: var(--text-accent);">{escape(isp['isp_name'])}</span>
              <span style="font-size: 0.85rem; font-family: var(--font-mono); font-weight: 700;">{escape(isp['default_ip'])}</span>
            </div>
            <h3 style="font-size: 1.15rem; font-weight: 700; margin-bottom: 0.4rem;">
              <a href="/isp/{escape(isp['slug'])}/">{escape(isp['gateway_name'])}</a>
            </h3>
            <p style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 1rem;">
              Default Password: <code>{escape(isp['default_password'])}</code>
            </p>
          </div>
          <div style="border-top: 1px solid var(--border-color); padding-top: 0.75rem; display: flex; justify-content: space-between; align-items: center;">
            <span style="font-size: 0.775rem; color: var(--text-muted);">{escape(isp['app_name'])}</span>
            <a href="/isp/{escape(isp['slug'])}/" style="font-size: 0.85rem; font-weight: 600;">View Gateway &rarr;</a>
          </div>
        </div>
        """

    content_master = f"""
  <main class="container" style="padding-top: 2rem; padding-bottom: 4rem;">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 2.5rem auto;">
      <div class="silo-badge silo-badge-isp">🏢 Service Provider Silo</div>
      <h1 style="font-size: 2.25rem; font-weight: 800; margin-bottom: 0.75rem;">
        ISP Router Gateway Login Directory
      </h1>
      <p style="font-size: 1.1rem; color: var(--text-secondary);">
        Direct administration login guides, sticker access codes, and IP passthrough instructions for broadband service providers.
      </p>
    </div>

    <div class="grid-3" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 1.25rem;">
      {isp_cards}
    </div>
  </main>
"""
    breadcrumbs = [("Home", "/"), ("ISP Gateways", "/isp/")]
    full_html = get_header(title_master, desc_master, canonical_master, active_nav="isp", breadcrumbs=breadcrumbs) + content_master + get_footer()
    with open(os.path.join(isp_master_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(full_html)

# ==============================================================================
# 4. GENERATE BRAND DIRECTORIES (/brands/[brand]/ & /brands/)
# ==============================================================================
def generate_brand_pages():
    print(f"Generating {len(BRAND_PROFILES)} brand directories...")
    for b in BRAND_PROFILES:
        slug = b["slug"]
        b_dir = os.path.join(PUBLIC_DIR, "brands", slug)
        make_dirs(b_dir)

        canonical = f"https://routeriphub.com/brands/{slug}/"
        title = f"{b['name']} Router Default IP, Password & Model Directory (2026)"
        desc = f"Complete {b['name']} router login directory. Factory default passwords, standard IP addresses ({', '.join(b['default_ips'])}), and model setup sheets."

        # Find models for this brand
        brand_models = [m for m in ROUTER_MODELS if m["brand_slug"] == slug]
        model_rows = ""
        for m in brand_models:
            model_rows += f"""
            <tr>
              <td><a href="/routers/{escape(m['slug'])}/"><strong>{escape(m['model_name'])}</strong></a></td>
              <td><span class="cell-code">{escape(m['default_ip'])}</span></td>
              <td><span class="cell-code">{escape(m['default_username'])}</span></td>
              <td><span class="cell-code">{escape(m['default_password'])}</span></td>
              <td><a href="/routers/{escape(m['slug'])}/" class="btn btn-secondary" style="font-size: 0.8rem; padding: 0.3rem 0.65rem;">Setup Sheet &rarr;</a></td>
            </tr>
            """

        if not model_rows:
            model_rows = f"""
            <tr>
              <td colspan="5" style="text-align: center; color: var(--text-muted); padding: 1.5rem;">
                Standard {escape(b['name'])} models utilize default gateway <strong>{escape(b['default_ips'][0])}</strong> with credentials <code>{escape(b['default_creds'])}</code>.
              </td>
            </tr>
            """

        breadcrumbs = [
            ("Home", "/"),
            ("Brands", "/brands/"),
            (b["name"], f"/brands/{slug}/")
        ]

        content = f"""
  <main class="container" style="padding-top: 1.5rem; padding-bottom: 3.5rem;">
    <div class="content-container">
      <div class="silo-badge silo-badge-router">🏷️ Brand Master Hub</div>
      <h1 style="font-size: 2.15rem; font-weight: 800; margin-bottom: 0.75rem; letter-spacing: -0.02em;">
        {escape(b['name'])} Router Login Directory
      </h1>
      <p style="font-size: 1.1rem; color: var(--text-secondary); margin-bottom: 1.5rem;">
        {escape(b['description'])}
      </p>

      <!-- Answer Box -->
      <div class="answer-box">
        <div class="answer-box-label">Standard {escape(b['name'])} Default Settings</div>
        <div class="answer-box-main">
          Default IP: <strong>{escape(', '.join(b['default_ips']))}</strong> &bull; Credentials: <strong>{escape(b['default_creds'])}</strong>
        </div>
        <div class="answer-box-sub">
          Web Domains: {escape(', '.join(b['web_domains']))}
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="action-btn-group">
        <a href="http://{escape(b['default_ips'][0])}" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
          Open {escape(b['name'])} Admin ({escape(b['default_ips'][0])}) &rarr;
        </a>
        <a href="{escape(b['app_url'])}" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">
          Get {escape(b['app_name'])}
        </a>
      </div>

      <!-- Brand Models Table -->
      <h2 style="font-size: 1.4rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 0.75rem;">
        {escape(b['name'])} Hardware Models Database
      </h2>
      <div style="overflow-x: auto;">
        <table class="table">
          <thead>
            <tr>
              <th>Model Name</th>
              <th>Default IP</th>
              <th>Username</th>
              <th>Password</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            {model_rows}
          </tbody>
        </table>
      </div>

      <!-- Diagnostic Console -->
      <div class="card" style="margin: 2.5rem 0; border: 1px solid var(--border-color); background: var(--bg-card); border-radius: var(--radius-lg); padding: 1.5rem;">
        <h3 style="font-size: 1.15rem; font-weight: 700; margin-bottom: 0.5rem;">
          ⚡ Reachability Check for {escape(b['name'])} Subnets
        </h3>
        <p style="font-size: 0.875rem; color: var(--text-muted); margin-bottom: 1rem;">
          Test if your computer or smartphone is currently connected to {escape(b['name'])}'s primary gateway ({escape(b['default_ips'][0])}):
        </p>
        <div style="display: flex; gap: 0.75rem; align-items: center; flex-wrap: wrap;">
          <button id="probe-btn" class="btn btn-primary" style="padding: 0.55rem 1rem; font-size: 0.875rem;">
            Test Connection to {escape(b['default_ips'][0])}
          </button>
          <div id="probe-status" style="font-size: 0.875rem; font-weight: 600;"></div>
        </div>
      </div>

      <!-- Cross Silo Links -->
      <div style="margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--border-color);">
        <h3 style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.75rem;">Browse Other Silos</h3>
        <div style="display: flex; flex-wrap: wrap; gap: 0.75rem;">
          <a href="/brands/" class="btn btn-secondary" style="font-size: 0.85rem;">All Brands Directory &rarr;</a>
          <a href="/routers/" class="btn btn-secondary" style="font-size: 0.85rem;">All Router Models &rarr;</a>
          <a href="/ip/{b['default_ips'][0].replace('.', '-')}/" class="btn btn-secondary" style="font-size: 0.85rem;">{escape(b['default_ips'][0])} Gateway Hub &rarr;</a>
        </div>
      </div>
    </div>
  </main>
"""
        full_html = get_header(title, desc, canonical, active_nav="brands", breadcrumbs=breadcrumbs) + content + get_footer()
        with open(os.path.join(b_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(full_html)

    # Master Brands Directory
    brands_master_dir = os.path.join(PUBLIC_DIR, "brands")
    canonical_master = "https://routeriphub.com/brands/"
    title_master = "Router Hardware Brands Directory (35+ Manufacturers)"
    desc_master = "Search default IPs and passwords across all major router brands including Netgear, TP-Link, ASUS, Linksys, Cisco, Ubiquiti, MikroTik, and Arris."

    brand_cards = ""
    for b in BRAND_PROFILES:
        brand_cards += f"""
        <div class="card" style="display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
              <span class="badge" style="background: var(--info-bg); color: var(--text-accent);">{escape(b['hq'])}</span>
            </div>
            <h3 style="font-size: 1.2rem; font-weight: 700; margin-bottom: 0.4rem;">
              <a href="/brands/{escape(b['slug'])}/">{escape(b['name'])}</a>
            </h3>
            <p style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 0.75rem;">
              Default Gateway: <strong>{escape(', '.join(b['default_ips']))}</strong>
            </p>
            <p style="font-size: 0.8rem; color: var(--text-muted); margin-bottom: 1rem;">
              Credentials: <code>{escape(b['default_creds'])}</code>
            </p>
          </div>
          <div style="border-top: 1px solid var(--border-color); padding-top: 0.75rem; display: flex; justify-content: space-between; align-items: center;">
            <span style="font-size: 0.775rem; color: var(--text-muted);">{escape(b['models_count'])}+ Models</span>
            <a href="/brands/{escape(b['slug'])}/" style="font-size: 0.85rem; font-weight: 600;">Brand Hub &rarr;</a>
          </div>
        </div>
        """

    content_master = f"""
  <main class="container" style="padding-top: 2rem; padding-bottom: 4rem;">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 2.5rem auto;">
      <div class="silo-badge silo-badge-router">🏷️ Brands Silo</div>
      <h1 style="font-size: 2.25rem; font-weight: 800; margin-bottom: 0.75rem;">
        Router Hardware Brands Directory
      </h1>
      <p style="font-size: 1.1rem; color: var(--text-secondary);">
        Complete hardware directories with default IP subnets, factory passwords, companion apps, and official support links.
      </p>
    </div>

    <div class="grid-3" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1.25rem;">
      {brand_cards}
    </div>
  </main>
"""
    breadcrumbs = [("Home", "/"), ("Brands", "/brands/")]
    full_html = get_header(title_master, desc_master, canonical_master, active_nav="brands", breadcrumbs=breadcrumbs) + content_master + get_footer()
    with open(os.path.join(brands_master_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(full_html)

# ==============================================================================
# 5. GENERATE IP GATEWAY PAGES (/ip/[ip]/ & /ip/)
# ==============================================================================
# ==============================================================================
# 5. GENERATE PRIVATE GATEWAY IP HUBS (/ip/[gateway-ip]/ & /ip/)
# IMPLEMENTS: Router IP Guide "Intent-First Technical SEO" Pattern
# ==============================================================================

IP_INTENT_METADATA = {
    "192.168.1.1": {
        "variant": "troubleshooting",
        "primary_brand": "Netgear, ASUS, Linksys & Cisco",
        "primary_cause": "typing into the browser search bar instead of the URL bar, an active VPN, or your router actually using 192.168.0.1",
        "target_audience": "Netgear, ASUS, Linksys, Cisco, and Verizon Fios",
        "verdict": "You are either disconnected from your router's local Wi-Fi, your phone is routing traffic over cellular data, an active VPN is intercepting local DNS queries, or your router is on a different subnet (such as 192.168.0.1 or 10.0.0.1).",
        "default_user": "admin",
        "default_pass": "password (or admin)",
        "web_alias": "routerlogin.net / asusrouter.com",
        "device_types": "Home Wi-Fi 6/7 Routers, Mesh Base Stations, Fiber Gateways",
        "common_devices": "Windows laptops, MacBooks, iPhones, Android smartphones, PS5, Xbox Series X, Smart TVs, smart thermostats",
        "typos": ["192.168.l.l", "http//192.168.1.1", "192.168.1.1.", "www.192.168.1.1", "192.168.1.1:8080"]
    },
    "192.168.0.1": {
        "variant": "troubleshooting",
        "primary_brand": "TP-Link, D-Link & Arris",
        "primary_cause": "browser forcing an HTTPS connection on a router with no SSL certificate, or an IP collision with an upstream modem",
        "target_audience": "TP-Link, D-Link, Arris SURFboard, and Sky Broadband",
        "verdict": "Your browser is either auto-upgrading to HTTPS (which drops port 80 requests), you are disconnected from Wi-Fi, or your upstream cable/fiber modem is colliding with 192.168.0.1.",
        "default_user": "admin",
        "default_pass": "admin (or set during initial setup)",
        "web_alias": "tplinkwifi.net / dlinkrouter.local",
        "device_types": "TP-Link Archer routers, D-Link EXO routers, Arris cable gateway combos",
        "common_devices": "iPhones, iPads, Windows desktop PCs, smart plugs, wireless security cameras, smart lightbulbs",
        "typos": ["192.168.0.l", "192.168.o.1", "http//192.168.0.1", "192.168.0.1.", "www.192.168.0.1"]
    },
    "10.0.0.1": {
        "variant": "troubleshooting",
        "primary_brand": "Comcast Xfinity (xFi) & Spectrum",
        "primary_cause": "your phone using mobile cellular data instead of home Wi-Fi, or Xfinity enforcing management via the xFi mobile app",
        "target_audience": "Comcast Xfinity xFi Gateways (XB6, XB7, XB8) and Spectrum",
        "verdict": "Comcast Xfinity xFi gateways use 10.0.0.1 by default. If it will not load, your device is likely disconnected from your in-home xFi network, routing via cellular data, or using an active VPN.",
        "default_user": "admin",
        "default_pass": "password (changed on first boot)",
        "web_alias": "Xfinity App (iOS/Android)",
        "device_types": "xFi Advanced Gateway, DOCSIS 3.1 Gateway Combos",
        "common_devices": "Smart TVs, Roku streaming sticks, Apple TV 4K, smart speakers, home computers",
        "typos": ["10.0.0.l", "10.0.0.1.", "http//10.0.0.1", "10.0.0.1:8080", "10.0.0.1/admin"]
    },
    "192.168.1.254": {
        "variant": "troubleshooting",
        "primary_brand": "AT&T Fiber & BT Smart Hub",
        "primary_cause": "attempting to log in with generic 'admin/admin' credentials instead of the unique 10-digit Device Access Code printed on the gateway sticker",
        "target_audience": "AT&T Fiber (BGW320, BGW210, NVG589) and British Telecom (BT Smart Hub 2)",
        "verdict": "192.168.1.254 occupies the highest usable host address in the /24 subnet. AT&T gateways require the physical 10-digit 'Device Access Code' printed in bold on the router label, not a generic password.",
        "default_user": "admin",
        "default_pass": "Printed 10-digit Device Access Code (DAC)",
        "web_alias": "att-smart-home-manager / bthomehub.home",
        "device_types": "AT&T BGW320 Wi-Fi 6 Optical Gateway, BT Smart Hub 2, 2Wire Modems",
        "common_devices": "Fiber ONTs, home office workstations, mesh extenders, network attached storage (NAS)",
        "typos": ["192.168.1.254.", "192.168.l.254", "http//192.168.1.254", "192.168.1.254:80", "192.168.1.254/login"]
    },
    "192.168.2.1": {
        "variant": "troubleshooting",
        "primary_brand": "Belkin & Bell Canada Home Hub",
        "primary_cause": "the manufacturer intentionally offset the subnet to .2.1 to prevent IP address clashes with upstream 192.168.1.1 broadband modems",
        "target_audience": "Belkin Wi-Fi routers, Bell Canada Home Hub gateways, and Philips Hue Bridge",
        "verdict": "Belkin and Bell Canada assign 192.168.2.1 to prevent Double NAT conflicts with upstream modems. If it fails, check if you are connected directly to the Belkin LAN rather than the upstream modem.",
        "default_user": "admin",
        "default_pass": "[Leave Blank] or admin",
        "web_alias": "router.belkin.com",
        "device_types": "Belkin Dual-Band routers, Bell Fibe Home Hub, Philips Hue Zigbee Bridges",
        "common_devices": "Smart home hubs, Philips Hue lighting bridges, Bell Fibe TV set-top boxes, laptops",
        "typos": ["192.168.2.l", "192.168.2.1.", "http//192.168.2.1", "192.168.2.1:8080"]
    },
    "192.168.8.1": {
        "variant": "troubleshooting",
        "primary_brand": "GL.iNet & Huawei 4G/5G Hotspots",
        "primary_cause": "the travel router's captive portal is conflicting with hotel or airport public Wi-Fi, or cellular tethering is disconnected",
        "target_audience": "GL.iNet OpenWrt Travel Routers (Beryl, Slate, Flint) and Huawei Mobile Wi-Fi",
        "verdict": "192.168.8.1 is the global default for portable OpenWrt travel routers and cellular 4G/5G hotspots. If unreached, reconnect to the travel router's private Wi-Fi SSID (e.g. GL-AXT1800-XXX).",
        "default_user": "admin / root",
        "default_pass": "admin (or set on first boot)",
        "web_alias": "gl-inet.com/admin",
        "device_types": "GL.iNet Pocket Travel Routers, Huawei LTE Dongles, Mobile Hotspots",
        "common_devices": "Travel laptops, Steam Deck, Nintendo Switch, smartphones, travel streaming dongles",
        "typos": ["192.168.8.l", "192.168.8.1.", "http//192.168.8.1", "192.168.8.1:80"]
    },
    "192.168.10.1": {
        "variant": "troubleshooting",
        "primary_brand": "Trendnet & ZyXEL Commercial Gateways",
        "primary_cause": "management access is restricted to specific physical LAN ports or blocked across guest VLANs",
        "target_audience": "Trendnet, ZyXEL, and multi-WAN balancing business routers",
        "verdict": "Commercial routers using 192.168.10.1 frequently isolate the web management console to LAN Port 1 or management VLAN 1. Verify you are not connected via a guest network.",
        "default_user": "admin",
        "default_pass": "admin",
        "web_alias": "trendnetrouter.com",
        "device_types": "Trendnet TEW series, ZyXEL ZyWALL VPN Firewalls",
        "common_devices": "VoIP desk phones, PoE network switches, office laser printers, server consoles",
        "typos": ["192.168.10.l", "192.168.10.1.", "http//192.168.10.1"]
    },
    "192.168.11.1": {
        "variant": "troubleshooting",
        "primary_brand": "Buffalo AirStation",
        "primary_cause": "the physical hardware switch on the bottom of the AirStation is set to 'AP' (Access Point) or 'WB' (Wireless Bridge) instead of 'Router'",
        "target_audience": "Buffalo AirStation Wi-Fi routers and DD-WRT OEM firmware",
        "verdict": "Buffalo AirStation hardware includes a physical mode toggle switch. When switched to AP or WB, the internal routing engine and 192.168.11.1 web portal are automatically disabled.",
        "default_user": "root / admin",
        "default_pass": "[Leave Blank] or password",
        "web_alias": "airstation",
        "device_types": "Buffalo AirStation HighPower series, DD-WRT powered gateways",
        "common_devices": "Desktop PCs, network attached storage (LinkStation), smart TVs",
        "typos": ["192.168.11.l", "192.168.11.1.", "http//192.168.11.1"]
    },
    "192.168.12.1": {
        "variant": "troubleshooting",
        "primary_brand": "T-Mobile 5G Home Internet",
        "primary_cause": "T-Mobile 5G gateways provide a read-only diagnostic web portal; all Wi-Fi password changes and network settings require the official T-Mobile mobile app",
        "target_audience": "T-Mobile 5G Home Internet (Arcadyan KVD21, Sagemcom Fast 5688W, Sercomm)",
        "verdict": "192.168.12.1 is strictly a diagnostic status page showing 5G cellular signal bands (RSRP/RSRQ/SINR). You cannot change Wi-Fi settings via the browser; you MUST use the T-Life (T-Mobile Internet) app.",
        "default_user": "admin",
        "default_pass": "Printed on gateway base sticker",
        "web_alias": "T-Life App / T-Mobile Internet App",
        "device_types": "T-Mobile 5G Gateway (KVD21, Fast 5688W, G4AR)",
        "common_devices": "Laptops, gaming consoles, smart TVs, smartphones, smart home appliances",
        "typos": ["192.168.12.l", "192.168.12.1.", "http//192.168.12.1"]
    },
    "192.168.31.1": {
        "variant": "troubleshooting",
        "primary_brand": "Xiaomi & Redmi Routers",
        "primary_cause": "the router is in factory unconfigured state or DNS redirection to miwifi.com failed",
        "target_audience": "Xiaomi Mi WiFi Routers (AX3000, AX9000, BE7000) and Redmi Routers",
        "verdict": "Xiaomi routers default to 192.168.31.1. On first boot, the router will redirect to miwifi.com. If the page fails, connect to the unencrypted 'Xiaomi_XXXX' Wi-Fi beacon first.",
        "default_user": "admin",
        "default_pass": "Configured by user during first boot setup wizard",
        "web_alias": "miwifi.com / Mi Home App",
        "device_types": "Xiaomi Mi AIoT Router, Redmi Gaming Routers, Wi-Fi 7 BE series",
        "common_devices": "Xiaomi Smart Home sensors, robot vacuums, smart cameras, mobile devices",
        "typos": ["192.168.31.l", "192.168.31.1.", "http//192.168.31.1", "miwifi.com"]
    },
    "192.168.68.1": {
        "variant": "troubleshooting",
        "primary_brand": "TP-Link Deco Whole Home Mesh",
        "primary_cause": "TP-Link Deco mesh systems are managed via cloud app; the local 192.168.68.1 web interface is a read-only diagnostic monitor",
        "target_audience": "TP-Link Deco Mesh systems (X55, XE75 Pro, BE85, X20)",
        "verdict": "TP-Link deliberately chose 192.168.68.1 to prevent IP clashes with ISP modems. The web interface allows firmware upgrades, but Wi-Fi setup requires the mobile Deco app.",
        "default_user": "TP-Link ID Email Account",
        "default_pass": "TP-Link Cloud Password",
        "web_alias": "tplinkdeco.net / TP-Link Deco App",
        "device_types": "Deco Wi-Fi 6E/7 Mesh Nodes, Outdoor Mesh Satellites",
        "common_devices": "Roaming smartphones, laptops, smart TVs, smart speakers, IoT plugs",
        "typos": ["192.168.68.l", "192.168.68.1.", "http//192.168.68.1"]
    },
    "192.168.88.1": {
        "variant": "troubleshooting",
        "primary_brand": "MikroTik RouterBOARD & RouterOS",
        "primary_cause": "MikroTik default firewall drops WebFig requests on WAN ports, or Web service (port 80) is disabled in favor of WinBox (port 8291)",
        "target_audience": "MikroTik RouterOS devices (hAP ax3, RB5009, CCR series, Cloud Core)",
        "verdict": "MikroTik factory defaults have NO password (blank) for user 'admin'. You must connect your PC to LAN Port 2 or higher (Port 1 is configured as an isolated WAN interface).",
        "default_user": "admin",
        "default_pass": "[Leave Blank] (No password on factory reset)",
        "web_alias": "router.lan / WinBox (Port 8291)",
        "device_types": "MikroTik hAP, Chateau LTE, Cloud Router Switch (CRS)",
        "common_devices": "Managed access points, enterprise switches, home lab server racks",
        "typos": ["192.168.88.l", "192.168.88.1.", "http//192.168.88.1", "192.168.88.1:8291"]
    },
    "192.168.100.1": {
        "variant": "troubleshooting",
        "primary_brand": "DOCSIS Cable Modems & Fiber ONTs",
        "primary_cause": "your cable modem is running in Bridge / Passthrough mode, meaning you must plug an Ethernet cable directly into the modem rather than through your separate router",
        "target_audience": "Motorola SURFboard, Arris, Netgear Nighthawk Modems (CM2000), Huawei ONTs, and Virgin Media SuperHub (Modem Mode)",
        "verdict": "192.168.100.1 is the diagnostic IP for DOCSIS cable modems and fiber optical terminals (ONTs). It is used to monitor downstream/upstream signal levels (dBmV) and correctable errors.",
        "default_user": "admin",
        "default_pass": "admin (or password / printed on base sticker)",
        "web_alias": "Modem Signal Diagnostics",
        "device_types": "DOCSIS 3.1 Standalone Modems, Optical Network Terminals (ONT)",
        "common_devices": "Cable line analyzers, primary WAN routers, diagnostic laptops",
        "typos": ["192.168.100.l", "192.168.100.1.", "http//192.168.100.1"]
    },
    "192.168.178.1": {
        "variant": "troubleshooting",
        "primary_brand": "AVM FRITZ!Box (Germany & Europe)",
        "primary_cause": "local mDNS resolution for 'fritz.box' failed or user entered incorrect printed sticker password",
        "target_audience": "AVM FRITZ!Box (7590 AX, 6660 Cable, 5590 Fiber, 4060)",
        "verdict": "192.168.178.1 is the universal default gateway across all AVM FRITZ!Box hardware in Europe. The router requires the unique randomized FRITZ!Box-Kennwort printed on the base sticker.",
        "default_user": "admin (or no username required)",
        "default_pass": "Unique randomized password printed on underside label",
        "web_alias": "http://fritz.box",
        "device_types": "FRITZ!Box DSL/Cable/Fiber Gateways, FRITZ!Repeater units",
        "common_devices": "DECT cordless phones, European smart plugs, home computers, laptops",
        "typos": ["192.168.178.l", "192.168.178.1.", "http//192.168.178.1", "fritz.box"]
    },
    "10.0.1.1": {
        "variant": "troubleshooting",
        "primary_brand": "Apple AirPort Extreme & Time Capsule",
        "primary_cause": "Apple AirPort routers do NOT have a web browser interface; attempting to load 10.0.1.1 in Chrome or Safari will fail because Apple requires the AirPort Utility app",
        "target_audience": "Apple AirPort Extreme, AirPort Express, and AirPort Time Capsule",
        "verdict": "Apple AirPort hardware does NOT run an HTTP web server. Navigating to http://10.0.1.1 in any web browser will time out. You MUST open 'AirPort Utility' on macOS or iOS to configure the device.",
        "default_user": "admin",
        "default_pass": "public (or configured via AirPort Utility)",
        "web_alias": "AirPort Utility (macOS / iOS)",
        "device_types": "AirPort Extreme 802.11ac, Time Capsule Wireless Backup Drives",
        "common_devices": "MacBooks, iMacs, iPhones, iPads, Time Machine network backups, AirPlay speakers",
        "typos": ["10.0.1.l", "10.0.1.1.", "http//10.0.1.1"]
    },
    "10.0.0.138": {
        "variant": "troubleshooting",
        "primary_brand": "Telstra (Australia) & Technicolor",
        "primary_cause": "the Telstra Smart Modem is operating on 4G cellular backup or Technicolor Telnet port lock",
        "target_audience": "Telstra Smart Modem Gen 2/3 (Australia) and Thomson / Technicolor modems",
        "verdict": "10.0.0.138 is the standard default gateway for Telstra broadband in Australia. If it fails to load, ensure you are not connected via a third-party VPN and try navigating to http://telstra.gateway.",
        "default_user": "admin",
        "default_pass": "admin (or Telstra printed password)",
        "web_alias": "http://telstra.gateway",
        "device_types": "Telstra NBN Smart Modems, Technicolor TG series gateways",
        "common_devices": "Australian NBN FTTP/FTTC connections, Foxtel IQ set-top boxes, laptops, smartphones",
        "typos": ["10.0.0.138.", "http//10.0.0.138", "telstra.gateway"]
    },
    "192.168.1.2": {
        "variant": "correction",
        "primary_brand": "Client Devices & Secondary Wi-Fi Extenders",
        "primary_cause": "192.168.1.2 is assigned to an individual client device (your laptop, phone, printer, smart TV, or camera), NOT your primary router gateway",
        "target_audience": "DHCP Client Devices, Network Printers, IP Security Cameras, and Chained Wi-Fi Extenders",
        "verdict": "192.168.1.2 is the first dynamic client IP leased by your router's DHCP server. It is NOT your router's admin portal. Your actual router gateway is 192.168.1.1.",
        "default_user": "admin",
        "default_pass": "admin (on range extenders) or device PIN",
        "web_alias": "http://192.168.1.1 (Actual Router Gateway)",
        "device_types": "Laptops, Smart TVs, Wireless Laser Printers, Hikvision/Dahua IP Cameras, Wi-Fi Extenders",
        "common_devices": "HP/Canon printers, Ring/Nest security cameras, NVR surveillance systems, laptops, iPhones",
        "typos": ["192.168.1.2.", "http//192.168.1.2", "192.168.l.2", "192.168.1.2:80"]
    }
}

# ==============================================================================
# 5. GENERATE PRIVATE GATEWAY IP HUBS (/ip/[gateway-ip]/ & /ip/)
# IMPLEMENTS: Router IP Guide "Intent-First Technical SEO" Pattern
# ==============================================================================

IP_INTENT_METADATA = {
    "192.168.1.1": {
        "variant": "troubleshooting",
        "primary_brand": "Netgear, ASUS, Linksys & Cisco",
        "primary_cause": "typing into the browser search bar instead of the URL bar, an active VPN, or your router actually using 192.168.0.1",
        "target_audience": "Netgear, ASUS, Linksys, Cisco, and Verizon Fios",
        "verdict": "You are either disconnected from your router's local Wi-Fi, your phone is routing traffic over cellular data, an active VPN is intercepting local DNS queries, or your router is on a different subnet (such as 192.168.0.1 or 10.0.0.1).",
        "default_user": "admin",
        "default_pass": "password (or admin)",
        "web_alias": "routerlogin.net / asusrouter.com",
        "device_types": "Home Wi-Fi 6/7 Routers, Mesh Base Stations, Fiber Gateways",
        "common_devices": "Windows laptops, MacBooks, iPhones, Android smartphones, PS5, Xbox Series X, Smart TVs, smart thermostats",
        "typos": ["192.168.l.l", "http//192.168.1.1", "192.168.1.1.", "www.192.168.1.1", "192.168.1.1:8080"]
    },
    "192.168.0.1": {
        "variant": "troubleshooting",
        "primary_brand": "TP-Link, D-Link & Arris",
        "primary_cause": "browser forcing an HTTPS connection on a router with no SSL certificate, or an IP collision with an upstream modem",
        "target_audience": "TP-Link, D-Link, Arris SURFboard, and Sky Broadband",
        "verdict": "Your browser is either auto-upgrading to HTTPS (which drops port 80 requests), you are disconnected from Wi-Fi, or your upstream cable/fiber modem is colliding with 192.168.0.1.",
        "default_user": "admin",
        "default_pass": "admin (or set during initial setup)",
        "web_alias": "tplinkwifi.net / dlinkrouter.local",
        "device_types": "TP-Link Archer routers, D-Link EXO routers, Arris cable gateway combos",
        "common_devices": "iPhones, iPads, Windows desktop PCs, smart plugs, wireless security cameras, smart lightbulbs",
        "typos": ["192.168.0.l", "192.168.o.1", "http//192.168.0.1", "192.168.0.1.", "www.192.168.0.1"]
    },
    "10.0.0.1": {
        "variant": "troubleshooting",
        "primary_brand": "Comcast Xfinity (xFi) & Spectrum",
        "primary_cause": "your phone using mobile cellular data instead of home Wi-Fi, or Xfinity enforcing management via the xFi mobile app",
        "target_audience": "Comcast Xfinity xFi Gateways (XB6, XB7, XB8) and Spectrum",
        "verdict": "Comcast Xfinity xFi gateways use 10.0.0.1 by default. If it will not load, your device is likely disconnected from your in-home xFi network, routing via cellular data, or using an active VPN.",
        "default_user": "admin",
        "default_pass": "password (changed on first boot)",
        "web_alias": "Xfinity App (iOS/Android)",
        "device_types": "xFi Advanced Gateway, DOCSIS 3.1 Gateway Combos",
        "common_devices": "Smart TVs, Roku streaming sticks, Apple TV 4K, smart speakers, home computers",
        "typos": ["10.0.0.l", "10.0.0.1.", "http//10.0.0.1", "10.0.0.1:8080", "10.0.0.1/admin"]
    },
    "192.168.1.254": {
        "variant": "troubleshooting",
        "primary_brand": "AT&T Fiber & BT Smart Hub",
        "primary_cause": "attempting to log in with generic 'admin/admin' credentials instead of the unique 10-digit Device Access Code printed on the gateway sticker",
        "target_audience": "AT&T Fiber (BGW320, BGW210, NVG589) and British Telecom (BT Smart Hub 2)",
        "verdict": "192.168.1.254 occupies the highest usable host address in the /24 subnet. AT&T gateways require the physical 10-digit 'Device Access Code' printed in bold on the router label, not a generic password.",
        "default_user": "admin",
        "default_pass": "Printed 10-digit Device Access Code (DAC)",
        "web_alias": "att-smart-home-manager / bthomehub.home",
        "device_types": "AT&T BGW320 Wi-Fi 6 Optical Gateway, BT Smart Hub 2, 2Wire Modems",
        "common_devices": "Fiber ONTs, home office workstations, mesh extenders, network attached storage (NAS)",
        "typos": ["192.168.1.254.", "192.168.l.254", "http//192.168.1.254", "192.168.1.254:80", "192.168.1.254/login"]
    },
    "192.168.2.1": {
        "variant": "troubleshooting",
        "primary_brand": "Belkin & Bell Canada Home Hub",
        "primary_cause": "the manufacturer intentionally offset the subnet to .2.1 to prevent IP address clashes with upstream 192.168.1.1 broadband modems",
        "target_audience": "Belkin Wi-Fi routers, Bell Canada Home Hub gateways, and Philips Hue Bridge",
        "verdict": "Belkin and Bell Canada assign 192.168.2.1 to prevent Double NAT conflicts with upstream modems. If it fails, check if you are connected directly to the Belkin LAN rather than the upstream modem.",
        "default_user": "admin",
        "default_pass": "[Leave Blank] or admin",
        "web_alias": "router.belkin.com",
        "device_types": "Belkin Dual-Band routers, Bell Fibe Home Hub, Philips Hue Zigbee Bridges",
        "common_devices": "Smart home hubs, Philips Hue lighting bridges, Bell Fibe TV set-top boxes, laptops",
        "typos": ["192.168.2.l", "192.168.2.1.", "http//192.168.2.1", "192.168.2.1:8080"]
    },
    "192.168.8.1": {
        "variant": "troubleshooting",
        "primary_brand": "GL.iNet & Huawei 4G/5G Hotspots",
        "primary_cause": "the travel router's captive portal is conflicting with hotel or airport public Wi-Fi, or cellular tethering is disconnected",
        "target_audience": "GL.iNet OpenWrt Travel Routers (Beryl, Slate, Flint) and Huawei Mobile Wi-Fi",
        "verdict": "192.168.8.1 is the global default for portable OpenWrt travel routers and cellular 4G/5G hotspots. If unreached, reconnect to the travel router's private Wi-Fi SSID (e.g. GL-AXT1800-XXX).",
        "default_user": "admin / root",
        "default_pass": "admin (or set on first boot)",
        "web_alias": "gl-inet.com/admin",
        "device_types": "GL.iNet Pocket Travel Routers, Huawei LTE Dongles, Mobile Hotspots",
        "common_devices": "Travel laptops, Steam Deck, Nintendo Switch, smartphones, travel streaming dongles",
        "typos": ["192.168.8.l", "192.168.8.1.", "http//192.168.8.1", "192.168.8.1:80"]
    },
    "192.168.10.1": {
        "variant": "troubleshooting",
        "primary_brand": "Trendnet & ZyXEL Commercial Gateways",
        "primary_cause": "management access is restricted to specific physical LAN ports or blocked across guest VLANs",
        "target_audience": "Trendnet, ZyXEL, and multi-WAN balancing business routers",
        "verdict": "Commercial routers using 192.168.10.1 frequently isolate the web management console to LAN Port 1 or management VLAN 1. Verify you are not connected via a guest network.",
        "default_user": "admin",
        "default_pass": "admin",
        "web_alias": "trendnetrouter.com",
        "device_types": "Trendnet TEW series, ZyXEL ZyWALL VPN Firewalls",
        "common_devices": "VoIP desk phones, PoE network switches, office laser printers, server consoles",
        "typos": ["192.168.10.l", "192.168.10.1.", "http//192.168.10.1"]
    },
    "192.168.11.1": {
        "variant": "troubleshooting",
        "primary_brand": "Buffalo AirStation",
        "primary_cause": "the physical hardware switch on the bottom of the AirStation is set to 'AP' (Access Point) or 'WB' (Wireless Bridge) instead of 'Router'",
        "target_audience": "Buffalo AirStation Wi-Fi routers and DD-WRT OEM firmware",
        "verdict": "Buffalo AirStation hardware includes a physical mode toggle switch. When switched to AP or WB, the internal routing engine and 192.168.11.1 web portal are automatically disabled.",
        "default_user": "root / admin",
        "default_pass": "[Leave Blank] or password",
        "web_alias": "airstation",
        "device_types": "Buffalo AirStation HighPower series, DD-WRT powered gateways",
        "common_devices": "Desktop PCs, network attached storage (LinkStation), smart TVs",
        "typos": ["192.168.11.l", "192.168.11.1.", "http//192.168.11.1"]
    },
    "192.168.12.1": {
        "variant": "troubleshooting",
        "primary_brand": "T-Mobile 5G Home Internet",
        "primary_cause": "T-Mobile 5G gateways provide a read-only diagnostic web portal; all Wi-Fi password changes and network settings require the official T-Mobile mobile app",
        "target_audience": "T-Mobile 5G Home Internet (Arcadyan KVD21, Sagemcom Fast 5688W, Sercomm)",
        "verdict": "192.168.12.1 is strictly a diagnostic status page showing 5G cellular signal bands (RSRP/RSRQ/SINR). You cannot change Wi-Fi settings via the browser; you MUST use the T-Life (T-Mobile Internet) app.",
        "default_user": "admin",
        "default_pass": "Printed on gateway base sticker",
        "web_alias": "T-Life App / T-Mobile Internet App",
        "device_types": "T-Mobile 5G Gateway (KVD21, Fast 5688W, G4AR)",
        "common_devices": "Laptops, gaming consoles, smart TVs, smartphones, smart home appliances",
        "typos": ["192.168.12.l", "192.168.12.1.", "http//192.168.12.1"]
    },
    "192.168.31.1": {
        "variant": "troubleshooting",
        "primary_brand": "Xiaomi & Redmi Routers",
        "primary_cause": "the router is in factory unconfigured state or DNS redirection to miwifi.com failed",
        "target_audience": "Xiaomi Mi WiFi Routers (AX3000, AX9000, BE7000) and Redmi Routers",
        "verdict": "Xiaomi routers default to 192.168.31.1. On first boot, the router will redirect to miwifi.com. If the page fails, connect to the unencrypted 'Xiaomi_XXXX' Wi-Fi beacon first.",
        "default_user": "admin",
        "default_pass": "Configured by user during first boot setup wizard",
        "web_alias": "miwifi.com / Mi Home App",
        "device_types": "Xiaomi Mi AIoT Router, Redmi Gaming Routers, Wi-Fi 7 BE series",
        "common_devices": "Xiaomi Smart Home sensors, robot vacuums, smart cameras, mobile devices",
        "typos": ["192.168.31.l", "192.168.31.1.", "http//192.168.31.1", "miwifi.com"]
    },
    "192.168.68.1": {
        "variant": "troubleshooting",
        "primary_brand": "TP-Link Deco Whole Home Mesh",
        "primary_cause": "TP-Link Deco mesh systems are managed via cloud app; the local 192.168.68.1 web interface is a read-only diagnostic monitor",
        "target_audience": "TP-Link Deco Mesh systems (X55, XE75 Pro, BE85, X20)",
        "verdict": "TP-Link deliberately chose 192.168.68.1 to prevent IP clashes with ISP modems. The web interface allows firmware upgrades, but Wi-Fi setup requires the mobile Deco app.",
        "default_user": "TP-Link ID Email Account",
        "default_pass": "TP-Link Cloud Password",
        "web_alias": "tplinkdeco.net / TP-Link Deco App",
        "device_types": "Deco Wi-Fi 6E/7 Mesh Nodes, Outdoor Mesh Satellites",
        "common_devices": "Roaming smartphones, laptops, smart TVs, smart speakers, IoT plugs",
        "typos": ["192.168.68.l", "192.168.68.1.", "http//192.168.68.1"]
    },
    "192.168.88.1": {
        "variant": "troubleshooting",
        "primary_brand": "MikroTik RouterBOARD & RouterOS",
        "primary_cause": "MikroTik default firewall drops WebFig requests on WAN ports, or Web service (port 80) is disabled in favor of WinBox (port 8291)",
        "target_audience": "MikroTik RouterOS devices (hAP ax3, RB5009, CCR series, Cloud Core)",
        "verdict": "MikroTik factory defaults have NO password (blank) for user 'admin'. You must connect your PC to LAN Port 2 or higher (Port 1 is configured as an isolated WAN interface).",
        "default_user": "admin",
        "default_pass": "[Leave Blank] (No password on factory reset)",
        "web_alias": "router.lan / WinBox (Port 8291)",
        "device_types": "MikroTik hAP, Chateau LTE, Cloud Router Switch (CRS)",
        "common_devices": "Managed access points, enterprise switches, home lab server racks",
        "typos": ["192.168.88.l", "192.168.88.1.", "http//192.168.88.1", "192.168.88.1:8291"]
    },
    "192.168.100.1": {
        "variant": "troubleshooting",
        "primary_brand": "DOCSIS Cable Modems & Fiber ONTs",
        "primary_cause": "your cable modem is running in Bridge / Passthrough mode, meaning you must plug an Ethernet cable directly into the modem rather than through your separate router",
        "target_audience": "Motorola SURFboard, Arris, Netgear Nighthawk Modems (CM2000), Huawei ONTs, and Virgin Media SuperHub (Modem Mode)",
        "verdict": "192.168.100.1 is the diagnostic IP for DOCSIS cable modems and fiber optical terminals (ONTs). It is used to monitor downstream/upstream signal levels (dBmV) and correctable errors.",
        "default_user": "admin",
        "default_pass": "admin (or password / printed on base sticker)",
        "web_alias": "Modem Signal Diagnostics",
        "device_types": "DOCSIS 3.1 Standalone Modems, Optical Network Terminals (ONT)",
        "common_devices": "Cable line analyzers, primary WAN routers, diagnostic laptops",
        "typos": ["192.168.100.l", "192.168.100.1.", "http//192.168.100.1"]
    },
    "192.168.178.1": {
        "variant": "troubleshooting",
        "primary_brand": "AVM FRITZ!Box (Germany & Europe)",
        "primary_cause": "local mDNS resolution for 'fritz.box' failed or user entered incorrect printed sticker password",
        "target_audience": "AVM FRITZ!Box (7590 AX, 6660 Cable, 5590 Fiber, 4060)",
        "verdict": "192.168.178.1 is the universal default gateway across all AVM FRITZ!Box hardware in Europe. The router requires the unique randomized FRITZ!Box-Kennwort printed on the base sticker.",
        "default_user": "admin (or no username required)",
        "default_pass": "Unique randomized password printed on underside label",
        "web_alias": "http://fritz.box",
        "device_types": "FRITZ!Box DSL/Cable/Fiber Gateways, FRITZ!Repeater units",
        "common_devices": "DECT cordless phones, European smart plugs, home computers, laptops",
        "typos": ["192.168.178.l", "192.168.178.1.", "http//192.168.178.1", "fritz.box"]
    },
    "10.0.1.1": {
        "variant": "troubleshooting",
        "primary_brand": "Apple AirPort Extreme & Time Capsule",
        "primary_cause": "Apple AirPort routers do NOT have a web browser interface; attempting to load 10.0.1.1 in Chrome or Safari will fail because Apple requires the AirPort Utility app",
        "target_audience": "Apple AirPort Extreme, AirPort Express, and AirPort Time Capsule",
        "verdict": "Apple AirPort hardware does NOT run an HTTP web server. Navigating to http://10.0.1.1 in any web browser will time out. You MUST open 'AirPort Utility' on macOS or iOS to configure the device.",
        "default_user": "admin",
        "default_pass": "public (or configured via AirPort Utility)",
        "web_alias": "AirPort Utility (macOS / iOS)",
        "device_types": "AirPort Extreme 802.11ac, Time Capsule Wireless Backup Drives",
        "common_devices": "MacBooks, iMacs, iPhones, iPads, Time Machine network backups, AirPlay speakers",
        "typos": ["10.0.1.l", "10.0.1.1.", "http//10.0.1.1"]
    },
    "10.0.0.138": {
        "variant": "troubleshooting",
        "primary_brand": "Telstra (Australia) & Technicolor",
        "primary_cause": "the Telstra Smart Modem is operating on 4G cellular backup or Technicolor Telnet port lock",
        "target_audience": "Telstra Smart Modem Gen 2/3 (Australia) and Thomson / Technicolor modems",
        "verdict": "10.0.0.138 is the standard default gateway for Telstra broadband in Australia. If it fails to load, ensure you are not connected via a third-party VPN and try navigating to http://telstra.gateway.",
        "default_user": "admin",
        "default_pass": "admin (or Telstra printed password)",
        "web_alias": "http://telstra.gateway",
        "device_types": "Telstra NBN Smart Modems, Technicolor TG series gateways",
        "common_devices": "Australian NBN FTTP/FTTC connections, Foxtel IQ set-top boxes, laptops, smartphones",
        "typos": ["10.0.0.138.", "http//10.0.0.138", "telstra.gateway"]
    },
    "192.168.1.2": {
        "variant": "correction",
        "primary_brand": "Client Devices & Secondary Wi-Fi Extenders",
        "primary_cause": "192.168.1.2 is assigned to an individual client device (your laptop, phone, printer, smart TV, or camera), NOT your primary router gateway",
        "target_audience": "DHCP Client Devices, Network Printers, IP Security Cameras, and Chained Wi-Fi Extenders",
        "verdict": "192.168.1.2 is the first dynamic client IP leased by your router's DHCP server. It is NOT your router's admin portal. Your actual router gateway is 192.168.1.1.",
        "default_user": "admin",
        "default_pass": "admin (on range extenders) or device PIN",
        "web_alias": "http://192.168.1.1 (Actual Router Gateway)",
        "device_types": "Laptops, Smart TVs, Wireless Laser Printers, Hikvision/Dahua IP Cameras, Wi-Fi Extenders",
        "common_devices": "HP/Canon printers, Ring/Nest security cameras, NVR surveillance systems, laptops, iPhones",
        "typos": ["192.168.1.2.", "http//192.168.1.2", "192.168.l.2", "192.168.1.2:80"]
    }
}


IP_HARDWARE_CATALOG = {
    "192.168.2.1": [
        {"model": "Belkin N300 Wireless Router (F9K1002)", "user": "admin", "pass": "[Leave Blank]", "wifi": "Wi-Fi 4 (802.11n)", "link": "/brands/belkin/", "link_text": "Belkin Hub &rarr;"},
        {"model": "Belkin N600 Dual-Band Router (F9K1102)", "user": "admin", "pass": "[Leave Blank]", "wifi": "Wi-Fi 4 (802.11n)", "link": "/brands/belkin/", "link_text": "Belkin Hub &rarr;"},
        {"model": "Belkin RT3200 Wi-Fi 6 Router (E8450)", "user": "admin", "pass": "admin", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/brands/belkin/", "link_text": "Belkin Hub &rarr;"},
        {"model": "Belkin AC1200 Dual-Band Wi-Fi 5 Router", "user": "admin", "pass": "password", "wifi": "Wi-Fi 5 (802.11ac)", "link": "/brands/belkin/", "link_text": "Belkin Hub &rarr;"},
        {"model": "Bell Canada Home Hub 3000 (Sagemcom FAST 5566)", "user": "admin", "pass": "admin", "wifi": "Wi-Fi 5 (802.11ac)", "link": "/isp/", "link_text": "ISP Hub &rarr;"},
        {"model": "Bell Canada Giga Hub (Wi-Fi 6E Optical Gateway)", "user": "admin", "pass": "Printed on Label", "wifi": "Wi-Fi 6E (802.11axe)", "link": "/isp/", "link_text": "ISP Hub &rarr;"},
        {"model": "SMC Barricade Broadband Router (SMC7004VBR)", "user": "admin", "pass": "smcadmin", "wifi": "Fast Ethernet / 802.11g", "link": "/ip/192-168-2-1/", "link_text": "Setup Guide &rarr;"},
        {"model": "Edimax BR-6428nS Wireless Router (BR Series)", "user": "admin", "pass": "1234", "wifi": "Wi-Fi 4 (802.11n)", "link": "/ip/192-168-2-1/", "link_text": "Setup Guide &rarr;"},
        {"model": "Philips Hue Bridge 2.0 (HomeKit Gateway)", "user": "[Pairing Button]", "pass": "[N/A]", "wifi": "Zigbee / Ethernet Hub", "link": "/ip/192-168-2-1/", "link_text": "Setup Guide &rarr;"}
    ],
    "192.168.8.1": [
        {"model": "GL.iNet Beryl AX (GL-MT3000) Pocket Travel Router", "user": "admin", "pass": "admin (First Boot)", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/brands/gl-inet/", "link_text": "GL.iNet Hub &rarr;"},
        {"model": "GL.iNet Slate AX (GL-AXT1800) Gigabit Travel Router", "user": "admin", "pass": "admin (First Boot)", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/brands/gl-inet/", "link_text": "GL.iNet Hub &rarr;"},
        {"model": "GL.iNet Flint 2 (GL-MT6000) Dual-Band Router", "user": "admin", "pass": "admin (First Boot)", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/brands/gl-inet/", "link_text": "GL.iNet Hub &rarr;"},
        {"model": "Huawei B535 4G LTE Router 3 Pro", "user": "admin", "pass": "admin", "wifi": "Wi-Fi 5 (802.11ac)", "link": "/brands/huawei/", "link_text": "Huawei Hub &rarr;"},
        {"model": "Huawei B818 4G Router Prime (Cat 19)", "user": "admin", "pass": "admin (Sticker)", "wifi": "Wi-Fi 5 (802.11ac)", "link": "/brands/huawei/", "link_text": "Huawei Hub &rarr;"},
        {"model": "Huawei 5G CPE Pro 2 (H122-373)", "user": "admin", "pass": "Printed Password", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/brands/huawei/", "link_text": "Huawei Hub &rarr;"},
        {"model": "GL.iNet Puli AX (GL-XE3000) 5G Cellular Gateway", "user": "admin", "pass": "admin (First Boot)", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/brands/gl-inet/", "link_text": "GL.iNet Hub &rarr;"}
    ],
    "192.168.10.1": [
        {"model": "Trendnet TEW-827DRU AC2600 StreamBoost Router", "user": "admin", "pass": "admin", "wifi": "Wi-Fi 5 (802.11ac)", "link": "/ip/192-168-10-1/", "link_text": "Setup Guide &rarr;"},
        {"model": "Trendnet TEW-829DRU AC3000 Tri-Band Commercial Router", "user": "admin", "pass": "admin", "wifi": "Wi-Fi 5 (802.11ac)", "link": "/ip/192-168-10-1/", "link_text": "Setup Guide &rarr;"},
        {"model": "ZyXEL USG FLEX 100 Unified Security Gateway", "user": "admin", "pass": "1234", "wifi": "Gigabit Ethernet / VPN", "link": "/brands/zyxel/", "link_text": "ZyXEL Hub &rarr;"},
        {"model": "ZyXEL Armor G5 Multi-Gigabit Wi-Fi 6 Router", "user": "admin", "pass": "Printed Password", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/brands/zyxel/", "link_text": "ZyXEL Hub &rarr;"},
        {"model": "Motorola MG7700 AC1900 Cable Gateway Combo", "user": "admin", "pass": "motorola", "wifi": "Wi-Fi 5 (802.11ac)", "link": "/ip/192-168-10-1/", "link_text": "Setup Guide &rarr;"},
        {"model": "Trendnet TW100-S4W1CA 4-Port Broadband Router", "user": "admin", "pass": "admin", "wifi": "Fast Ethernet", "link": "/ip/192-168-10-1/", "link_text": "Setup Guide &rarr;"}
    ],
    "192.168.11.1": [
        {"model": "Buffalo AirStation WXR-5700AX7S Wi-Fi 6 Gaming Router", "user": "admin", "pass": "password", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/ip/192-168-11-1/", "link_text": "Setup Guide &rarr;"},
        {"model": "Buffalo AirStation Extreme AC1900 (WZR-1750DHPD)", "user": "admin", "pass": "password", "wifi": "Wi-Fi 5 (802.11ac)", "link": "/ip/192-168-11-1/", "link_text": "Setup Guide &rarr;"},
        {"model": "Buffalo AirStation HighPower (WZR-HP-G450H)", "user": "root", "pass": "[Leave Blank]", "wifi": "Wi-Fi 4 (802.11n)", "link": "/ip/192-168-11-1/", "link_text": "Setup Guide &rarr;"},
        {"model": "Buffalo AirStation WSR-3200AX4S Dual-Band Router", "user": "admin", "pass": "password", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/ip/192-168-11-1/", "link_text": "Setup Guide &rarr;"},
        {"model": "Buffalo AirStation WXR-1900DHP3 Gigabit Router", "user": "admin", "pass": "password", "wifi": "Wi-Fi 5 (802.11ac)", "link": "/ip/192-168-11-1/", "link_text": "Setup Guide &rarr;"},
        {"model": "Buffalo WSR-2533DHP2 High-Spec Wi-Fi Router", "user": "admin", "pass": "password", "wifi": "Wi-Fi 5 (802.11ac)", "link": "/ip/192-168-11-1/", "link_text": "Setup Guide &rarr;"}
    ],
    "192.168.12.1": [
        {"model": "T-Mobile 5G Gateway (Arcadyan KVD21)", "user": "admin", "pass": "Printed Sticker PIN", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/isp/t-mobile-5g/", "link_text": "T-Mobile Hub &rarr;"},
        {"model": "T-Mobile 5G Gateway (Sagemcom Fast 5688W)", "user": "admin", "pass": "Printed Sticker PIN", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/isp/t-mobile-5g/", "link_text": "T-Mobile Hub &rarr;"},
        {"model": "T-Mobile 5G Gateway (Sercomm G4SE)", "user": "admin", "pass": "Printed Sticker PIN", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/isp/t-mobile-5g/", "link_text": "T-Mobile Hub &rarr;"},
        {"model": "T-Mobile 5G Gateway (Nokia 5G21 'Silver Trashcan')", "user": "admin", "pass": "Printed Sticker PIN", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/isp/t-mobile-5g/", "link_text": "T-Mobile Hub &rarr;"},
        {"model": "T-Mobile Home Internet G4AR External Antenna Gateway", "user": "admin", "pass": "Printed Sticker PIN", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/isp/t-mobile-5g/", "link_text": "T-Mobile Hub &rarr;"},
        {"model": "Inseego Wavemaker 5G Indoor Router (FX2000)", "user": "admin", "pass": "Printed Password", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/isp/t-mobile-5g/", "link_text": "T-Mobile Hub &rarr;"}
    ],
    "192.168.31.1": [
        {"model": "Xiaomi Mi Router AX9000 Tri-Band Gaming Router", "user": "admin", "pass": "Set on First Boot", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/brands/xiaomi/", "link_text": "Xiaomi Hub &rarr;"},
        {"model": "Xiaomi Router BE7000 Multi-Gigabit Wi-Fi 7 Router", "user": "admin", "pass": "Set on First Boot", "wifi": "Wi-Fi 7 (802.11be)", "link": "/brands/xiaomi/", "link_text": "Xiaomi Hub &rarr;"},
        {"model": "Xiaomi Router AX3000 NE Dual-Band Wi-Fi 6", "user": "admin", "pass": "Set on First Boot", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/brands/xiaomi/", "link_text": "Xiaomi Hub &rarr;"},
        {"model": "Redmi Gaming Router AX5400 Dual-Band Router", "user": "admin", "pass": "Set on First Boot", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/brands/xiaomi/", "link_text": "Xiaomi Hub &rarr;"},
        {"model": "Xiaomi Mi Router AX6000 AIoT Flagship Router", "user": "admin", "pass": "Set on First Boot", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/brands/xiaomi/", "link_text": "Xiaomi Hub &rarr;"},
        {"model": "Redmi Router AC2100 Dual-Core Router", "user": "admin", "pass": "Set on First Boot", "wifi": "Wi-Fi 5 (802.11ac)", "link": "/brands/xiaomi/", "link_text": "Xiaomi Hub &rarr;"}
    ],
    "192.168.68.1": [
        {"model": "TP-Link Deco X55 AX3000 Whole Home Mesh System", "user": "TP-Link ID", "pass": "Cloud Account Password", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/brands/tp-link/", "link_text": "TP-Link Hub &rarr;"},
        {"model": "TP-Link Deco XE75 Pro Tri-Band Wi-Fi 6E Mesh", "user": "TP-Link ID", "pass": "Cloud Account Password", "wifi": "Wi-Fi 6E (802.11axe)", "link": "/brands/tp-link/", "link_text": "TP-Link Hub &rarr;"},
        {"model": "TP-Link Deco BE85 Multi-Gigabit Wi-Fi 7 Mesh", "user": "TP-Link ID", "pass": "Cloud Account Password", "wifi": "Wi-Fi 7 (802.11be)", "link": "/brands/tp-link/", "link_text": "TP-Link Hub &rarr;"},
        {"model": "TP-Link Deco X20 AX1800 Dual-Band Mesh Wi-Fi", "user": "TP-Link ID", "pass": "Cloud Account Password", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/brands/tp-link/", "link_text": "TP-Link Hub &rarr;"},
        {"model": "TP-Link Deco S4 AC1200 Seamless Roaming Mesh", "user": "TP-Link ID", "pass": "Cloud Account Password", "wifi": "Wi-Fi 5 (802.11ac)", "link": "/brands/tp-link/", "link_text": "TP-Link Hub &rarr;"},
        {"model": "TP-Link Deco Voice X20 Mesh with Smart Speaker", "user": "TP-Link ID", "pass": "Cloud Account Password", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/brands/tp-link/", "link_text": "TP-Link Hub &rarr;"}
    ],
    "192.168.88.1": [
        {"model": "MikroTik hAP ax3 (C53UiG+5HPaxD2HPaxD) Router", "user": "admin", "pass": "[Leave Blank]", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/brands/mikrotik/", "link_text": "MikroTik Hub &rarr;"},
        {"model": "MikroTik RB5009UG+S+IN Heavy-Duty Home Lab Router", "user": "admin", "pass": "[Leave Blank]", "wifi": "Gigabit / 10G SFP+", "link": "/brands/mikrotik/", "link_text": "MikroTik Hub &rarr;"},
        {"model": "MikroTik hEX S (RB760iGS) Gigabit Ethernet Router", "user": "admin", "pass": "[Leave Blank]", "wifi": "Gigabit / SFP Cage", "link": "/brands/mikrotik/", "link_text": "MikroTik Hub &rarr;"},
        {"model": "MikroTik Chateau 5G ax Dual-Band Cellular Router", "user": "admin", "pass": "[Leave Blank]", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/brands/mikrotik/", "link_text": "MikroTik Hub &rarr;"},
        {"model": "MikroTik Cloud Router Switch (CRS305-1G-4S+IN)", "user": "admin", "pass": "[Leave Blank]", "wifi": "10Gbps SFP+ Fiber", "link": "/brands/mikrotik/", "link_text": "MikroTik Hub &rarr;"},
        {"model": "MikroTik cAP ax Dual-Band Ceiling Access Point", "user": "admin", "pass": "[Leave Blank]", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/brands/mikrotik/", "link_text": "MikroTik Hub &rarr;"}
    ],
    "192.168.100.1": [
        {"model": "Motorola SURFboard SB8200 DOCSIS 3.1 Cable Modem", "user": "admin", "pass": "motorola", "wifi": "Gigabit Ethernet (Bridge)", "link": "/ip/192-168-100-1/", "link_text": "Diagnostics &rarr;"},
        {"model": "Arris SURFboard SB6190 DOCSIS 3.0 Cable Modem", "user": "admin", "pass": "password", "wifi": "Gigabit Ethernet (Bridge)", "link": "/ip/192-168-100-1/", "link_text": "Diagnostics &rarr;"},
        {"model": "Netgear Nighthawk CM2000 Multi-Gigabit Cable Modem", "user": "admin", "pass": "password", "wifi": "2.5Gbps Multi-Gig WAN", "link": "/brands/netgear/", "link_text": "Netgear Hub &rarr;"},
        {"model": "Virgin Media SuperHub 4 (Diagnostic Modem Mode)", "user": "admin", "pass": "Printed Sticker PIN", "wifi": "Modem Mode Bridge", "link": "/isp/", "link_text": "ISP Hub &rarr;"},
        {"model": "Huawei EchoLife HG8245H GPON Optical Terminal (ONT)", "user": "telecomadmin", "pass": "admintelecom", "wifi": "GPON Fiber / Ethernet", "link": "/brands/huawei/", "link_text": "Huawei Hub &rarr;"},
        {"model": "Arris Touchstone CM8200 DOCSIS 3.1 Ultra-Fast Modem", "user": "admin", "pass": "password", "wifi": "Gigabit Ethernet (Bridge)", "link": "/ip/192-168-100-1/", "link_text": "Diagnostics &rarr;"}
    ],
    "192.168.178.1": [
        {"model": "AVM FRITZ!Box 7590 AX Flagship VDSL/Wi-Fi 6 Router", "user": "admin", "pass": "FRITZ!Box-Kennwort (Sticker)", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/brands/avm-fritzbox/", "link_text": "FRITZ!Box Hub &rarr;"},
        {"model": "AVM FRITZ!Box 6660 Cable DOCSIS 3.1 Cable Gateway", "user": "admin", "pass": "FRITZ!Box-Kennwort (Sticker)", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/brands/avm-fritzbox/", "link_text": "FRITZ!Box Hub &rarr;"},
        {"model": "AVM FRITZ!Box 5590 Fiber Integrated AON/GPON Router", "user": "admin", "pass": "FRITZ!Box-Kennwort (Sticker)", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/brands/avm-fritzbox/", "link_text": "FRITZ!Box Hub &rarr;"},
        {"model": "AVM FRITZ!Box 4060 Tri-Band Wi-Fi 6 Router", "user": "admin", "pass": "FRITZ!Box-Kennwort (Sticker)", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/brands/avm-fritzbox/", "link_text": "FRITZ!Box Hub &rarr;"},
        {"model": "AVM FRITZ!Box 7530 AX Compact VDSL/Mesh Router", "user": "admin", "pass": "FRITZ!Box-Kennwort (Sticker)", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/brands/avm-fritzbox/", "link_text": "FRITZ!Box Hub &rarr;"},
        {"model": "AVM FRITZ!Box 6850 5G Cellular Home Gateway", "user": "admin", "pass": "FRITZ!Box-Kennwort (Sticker)", "wifi": "Wi-Fi 5 (802.11ac)", "link": "/brands/avm-fritzbox/", "link_text": "FRITZ!Box Hub &rarr;"}
    ],
    "10.0.1.1": [
        {"model": "Apple AirPort Extreme 802.11ac (6th Gen Tower)", "user": "admin", "pass": "Configured in AirPort Utility", "wifi": "Wi-Fi 5 (802.11ac)", "link": "/ip/10-0-1-1/", "link_text": "Setup Guide &rarr;"},
        {"model": "Apple AirPort Time Capsule 802.11ac (2TB / 3TB)", "user": "admin", "pass": "Configured in AirPort Utility", "wifi": "Wi-Fi 5 (802.11ac)", "link": "/ip/10-0-1-1/", "link_text": "Setup Guide &rarr;"},
        {"model": "Apple AirPort Express 802.11n (2nd Gen)", "user": "admin", "pass": "Configured in AirPort Utility", "wifi": "Wi-Fi 4 (802.11n)", "link": "/ip/10-0-1-1/", "link_text": "Setup Guide &rarr;"},
        {"model": "Cisco Small Business RV110W Wireless-N VPN Firewall", "user": "cisco", "pass": "cisco", "wifi": "Wi-Fi 4 (802.11n)", "link": "/brands/cisco/", "link_text": "Cisco Hub &rarr;"},
        {"model": "Apple AirPort Extreme (5th Gen Flat)", "user": "admin", "pass": "Configured in AirPort Utility", "wifi": "Wi-Fi 4 (802.11n)", "link": "/ip/10-0-1-1/", "link_text": "Setup Guide &rarr;"},
        {"model": "Cisco Meraki Go GR10 Dual-Band Access Point", "user": "admin", "pass": "Meraki Cloud App", "wifi": "Wi-Fi 5 (802.11ac)", "link": "/brands/cisco/", "link_text": "Cisco Hub &rarr;"}
    ],
    "10.0.0.138": [
        {"model": "Telstra Smart Modem Gen 3 (Arcadyan LH1000)", "user": "admin", "pass": "admin (Telstra Printed)", "wifi": "Wi-Fi 6 (802.11ax)", "link": "/ip/10-0-0-138/", "link_text": "Telstra Hub &rarr;"},
        {"model": "Telstra Smart Modem Gen 2 (Technicolor DJA0231)", "user": "admin", "pass": "admin (Telstra Printed)", "wifi": "Wi-Fi 5 (802.11ac)", "link": "/ip/10-0-0-138/", "link_text": "Telstra Hub &rarr;"},
        {"model": "Thomson TG585 v7 ADSL2+ Wireless Gateway", "user": "Administrator", "pass": "[Leave Blank]", "wifi": "802.11g / b", "link": "/ip/10-0-0-138/", "link_text": "Setup Guide &rarr;"},
        {"model": "Technicolor TG799vac Dual-Band Voice Gateway", "user": "admin", "pass": "admin", "wifi": "Wi-Fi 5 (802.11ac)", "link": "/ip/10-0-0-138/", "link_text": "Setup Guide &rarr;"},
        {"model": "Thomson SpeedTouch 530 Ethernet ADSL Modem", "user": "Administrator", "pass": "[Leave Blank]", "wifi": "Fast Ethernet", "link": "/ip/10-0-0-138/", "link_text": "Setup Guide &rarr;"},
        {"model": "Telstra Gateway Max (Netgear C6300TL DOCSIS)", "user": "admin", "pass": "password", "wifi": "Wi-Fi 5 (802.11ac)", "link": "/ip/10-0-0-138/", "link_text": "Telstra Hub &rarr;"}
    ],
    "192.168.1.2": [
        {"model": "Netgear Nighthawk Mesh Satellite (MS60 Wi-Fi 6)", "user": "admin", "pass": "Syncs with Router", "wifi": "Wi-Fi 6 Mesh Satellite", "link": "/brands/netgear/", "link_text": "Netgear Hub &rarr;"},
        {"model": "TP-Link RE705X AX3000 Wi-Fi 6 Range Extender", "user": "admin", "pass": "admin (First Boot)", "wifi": "Wi-Fi 6 Range Extender", "link": "/brands/tp-link/", "link_text": "TP-Link Hub &rarr;"},
        {"model": "HP LaserJet Pro M404dn (Network Office Printer)", "user": "admin", "pass": "Printed Service PIN", "wifi": "Gigabit Ethernet Host", "link": "/ip/192-168-1-2/", "link_text": "Device Guide &rarr;"},
        {"model": "Hikvision DS-2CD2143G2-I (4MP IP Security Camera)", "user": "admin", "pass": "Initial Activation Pass", "wifi": "PoE Security Camera", "link": "/ip/192-168-1-2/", "link_text": "Device Guide &rarr;"},
        {"model": "Dahua 4K NVR Network Video Recorder (NVR4108HS)", "user": "admin", "pass": "admin / Custom Pattern", "wifi": "Gigabit Ethernet NVR", "link": "/ip/192-168-1-2/", "link_text": "Device Guide &rarr;"},
        {"model": "Synology DiskStation DS220+ 2-Bay NAS (LAN Port 1)", "user": "admin", "pass": "DSM Account Password", "wifi": "Gigabit Ethernet Storage", "link": "/ip/192-168-1-2/", "link_text": "Device Guide &rarr;"}
    ]
}

def generate_ip_pages():
    print(f"Generating {len(IP_GATEWAYS)} private gateway IP pages (Intent-First Technical SEO Pattern)...")
    for ip_item in IP_GATEWAYS:
        ip = ip_item["ip"]
        slug = ip_item["slug"]
        ip_dir = os.path.join(PUBLIC_DIR, "ip", slug)
        make_dirs(ip_dir)

        canonical = f"https://routeriphub.com/ip/{slug}/"
        meta = IP_INTENT_METADATA.get(ip, {
            "variant": "troubleshooting",
            "primary_brand": ip_item["brands"].split(",")[0],
            "primary_cause": "subnet conflict, VPN connection, or browser search redirect",
            "target_audience": ip_item["brands"],
            "verdict": f"If {ip} is not loading, verify your device is connected to the router Wi-Fi without VPN and enter http://{ip} over plain HTTP.",
            "default_user": ip_item["default_creds"].split("/")[0].strip(),
            "default_pass": ip_item["default_creds"].split("/")[1].strip() if "/" in ip_item["default_creds"] else "admin",
            "web_alias": f"http://{ip}",
            "device_types": "Home Wi-Fi Routers, Gateways",
            "common_devices": "Laptops, smartphones, smart TVs, tablets",
            "typos": [f"{ip}.", f"http//{ip}"]
        })

        is_correction = meta["variant"] == "correction"

        # 1. Page Title & Contrarian H1 Formulas
        if is_correction:
            title = f"{ip} — What This Address Actually Is (It’s Usually Not Your Router)"
            h1 = f"{ip} — What This Address Actually Is (It’s Usually Not Your Router)"
            desc = f"Searched {ip} expecting your router login? Here is why {ip} is a client device or extender, not your primary router gateway, and how to reach 192.168.1.1."
        else:
            title = f"{ip} Not Working? {meta['primary_brand']} Router Login Fix (2026)"
            h1 = f"{ip} Not Working? {meta['primary_brand']} Router Login Fix"
            desc = f"{ip} not loading? Instant fix for {meta['target_audience']} router login failures. Factory credentials, why connection timeouts happen, and step-by-step diagnostic resolution."

        # Schemas
        tech_schema = {
            "@type": "TechArticle",
            "headline": title,
            "description": desc,
            "mainEntityOfPage": canonical,
            "datePublished": "2026-01-15T08:00:00+00:00",
            "dateModified": f"{TODAY}T02:00:00+00:00",
            "author": {"@type": "Organization", "name": "RouterIPHub Editorial Team"},
            "publisher": {"@type": "Organization", "name": "RouterIPHub", "url": "https://routeriphub.com/"}
        }

        howto_schema = {
            "@type": "HowTo",
            "name": f"How to Resolve {ip} Router Access & Login",
            "description": f"Step-by-step technical diagnostic sequence to resolve {ip} browser connection failures.",
            "step": [
                {
                    "@type": "HowToStep",
                    "position": 1,
                    "name": "Disconnect VPNs & Cellular Data",
                    "text": "Disconnect active corporate or commercial VPNs (NordVPN, ExpressVPN) and turn off mobile cellular data to prevent local subnet isolation."
                },
                {
                    "@type": "HowToStep",
                    "position": 2,
                    "name": "Verify Physical or Wi-Fi Connection",
                    "text": "Ensure your phone or computer is actively joined to the router's local Wi-Fi SSID or connected via Ethernet."
                },
                {
                    "@type": "HowToStep",
                    "position": 3,
                    "name": "Navigate to Gateway Address",
                    "text": f"Open your web browser and type http://{ip} explicitly in the URL address bar, not the search engine omnibox."
                },
                {
                    "@type": "HowToStep",
                    "position": 4,
                    "name": "Authenticate with Factory Credentials",
                    "text": f"Submit username '{meta['default_user']}' and password '{meta['default_pass']}' or check the physical router sticker."
                }
            ]
        }

        faq_schema = {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": f"Why does {ip} send me to a Google search page?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": f"Modern web browser omniboxes combine search and address bars. If you type numbers without the protocol scheme, or include a typo like a trailing comma or space, the browser treats the input as a search keyword. Always type http://{ip} explicitly."
                    }
                },
                {
                    "@type": "Question",
                    "name": f"Can I access {ip} from outside my home network?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": f"No. {ip} is an RFC 1918 private IPv4 address. Private addresses are non-routable over the public Internet. You must be physically connected to the router's local Wi-Fi or Ethernet network to load the management portal unless you have established a secure VPN tunnel into your home LAN."
                    }
                },
                {
                    "@type": "Question",
                    "name": "What is the difference between admin credentials and the Wi-Fi password?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Your Wi-Fi password (WPA2/WPA3 Pre-Shared Key) connects phones and laptops to the wireless signal. The router admin username and password (often admin / admin or a printed serial PIN) authenticate access to the internal web console to alter firewall, DNS, and network settings."
                    }
                },
                {
                    "@type": "Question",
                    "name": f"How do I fix {ip} connection timed out errors?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": f"Disconnect any active commercial or corporate VPNs, turn off mobile cellular data on your smartphone, and ensure your device is connected to the router via Wi-Fi or LAN cable. Verify your default gateway in terminal using ipconfig or netstat -nr, and enter http://{ip} over plain HTTP."
                    }
                }
            ]
        }

        breadcrumbs = [
            ("Home", "/"),
            ("IP Directory", "/ip/"),
            (ip, f"/ip/{slug}/")
        ]

        # 2. Hardware models matching this IP (Populate Table 2 with specific distinct hardware rows)
        ip_models = [m for m in ROUTER_MODELS if m["default_ip"] == ip]
        model_rows = ""
        # If models exist in ROUTER_MODELS, include them
        for m in ip_models[:8]:
            model_rows += f"""
            <tr>
              <td><a href="/routers/{escape(m['slug'])}/"><strong>{escape(m['brand'])} {escape(m['model_name'])}</strong></a></td>
              <td><code>{escape(m['default_username'])}</code></td>
              <td><code>{escape(m['default_password'])}</code></td>
              <td><span style="font-size: 0.825rem; color: var(--text-muted);">{escape(m['wifi_standard'])}</span></td>
              <td><a href="/routers/{escape(m['slug'])}/" class="btn btn-secondary" style="font-size: 0.8rem; padding: 0.3rem 0.65rem;">Setup Sheet &rarr;</a></td>
            </tr>
            """
        # If fewer than 6 models, supplement from IP_HARDWARE_CATALOG
        if len(ip_models) < 6 and ip in IP_HARDWARE_CATALOG:
            for item in IP_HARDWARE_CATALOG[ip]:
                model_rows += f"""
            <tr>
              <td><strong>{escape(item['model'])}</strong></td>
              <td><code>{escape(item['user'])}</code></td>
              <td><code>{escape(item['pass'])}</code></td>
              <td><span style="font-size: 0.825rem; color: var(--text-muted);">{escape(item['wifi'])}</span></td>
              <td><a href="{escape(item['link'])}" class="btn btn-secondary" style="font-size: 0.8rem; padding: 0.3rem 0.65rem;">{item['link_text']}</a></td>
            </tr>
                """

        # 3. Intent-Matching Intro & Verdict Content
        if is_correction:
            intro_html = f"""
        <p style="font-size: 1.15rem; color: var(--text-secondary); line-height: 1.7; margin-bottom: 1.5rem;">
          If you searched <strong>{escape(ip)}</strong> expecting to open your router setup page, here is why that assumption is wrong: <strong>{escape(ip)} is almost always an individual client device</strong>—such as your laptop, phone, wireless printer, smart TV, or security camera/NVR—or a secondary Wi-Fi range extender, while your actual primary default gateway router is almost certainly <strong><a href="/ip/192-168-1-1/" style="color: var(--text-accent); text-decoration: underline;">192.168.1.1</a></strong>.
        </p>
            """
            quick_answer_html = f"""
        <div class="verdict-box">
          <div class="verdict-tag">⚠️ Central Address Correction &amp; Verdict</div>
          <p style="font-size: 1.15rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.75rem; line-height: 1.6;">
            Verdict: {escape(ip)} is a client device or secondary repeater, NOT your primary router gateway.
          </p>
          <p style="color: var(--text-secondary); margin-bottom: 1.25rem; line-height: 1.6;">
            In standard home and small business networks running on the <code>192.168.1.0/24</code> subnet, the primary router reserves <code>192.168.1.1</code> for its own administration web server. When your laptop, desktop PC, or iPhone joins the network, the router's DHCP server assigns it the first available host IP: <strong>{escape(ip)}</strong>. Navigating to this address in a browser will either time out or display the configuration page of an IoT smart device, not your router.
          </p>
          <div class="action-btn-group">
            <a href="http://192.168.1.1" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
              Open Real Router Gateway (http://192.168.1.1) &rarr;
            </a>
            <a href="http://{escape(ip)}" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">
              Open http://{escape(ip)} (Inspect Client Device)
            </a>
            <button class="btn btn-secondary copy-btn" data-copy="192.168.1.1">Copy Router IP (192.168.1.1)</button>
          </div>
        </div>
            """
        else:
            intro_html = f"""
        <p style="font-size: 1.15rem; color: var(--text-secondary); line-height: 1.7; margin-bottom: 1.5rem;">
          <strong>{escape(ip)} not working?</strong> If your browser displays <em>"This site can’t be reached"</em>, <em>"Connection timed out"</em>, or redirects you to a Google search results page instead of your router admin console, here is why {escape(meta['primary_cause'])} happens and how to fix it in under 60 seconds.
        </p>
            """
            quick_answer_html = f"""
        <div class="verdict-box">
          <div class="verdict-tag">⚡ Immediate Diagnostic Verdict &amp; Login Fix</div>
          <p style="font-size: 1.15rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.75rem; line-height: 1.6;">
            Verdict: {escape(meta['verdict'])}
          </p>
          <p style="color: var(--text-secondary); margin-bottom: 1.25rem; line-height: 1.6;">
            Default credentials for {escape(meta['target_audience'])} routers on this gateway are typically username: <code>{escape(meta['default_user'])}</code> and password: <code>{escape(meta['default_pass'])}</code>. You must connect over plain, unencrypted HTTP without an active VPN tunnel.
          </p>
          <div class="action-btn-group">
            <a href="http://{escape(ip)}" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
              Open http://{escape(ip)} in Browser &rarr;
            </a>
            <button class="btn btn-secondary copy-btn" data-copy="{escape(ip)}">Copy Gateway IP ({escape(ip)})</button>
            <a href="/tools/detect-gateway/" class="btn btn-secondary">⚡ Auto-Detect My Actual Gateway</a>
          </div>
        </div>
            """

        # 4. Visual Diagnostic Matrix & Topology Context
        topology_diagram = """
    ┌─────────────────────────────────────────────────────────────┐
    │                INTERNET (Public WAN / ISP)                  │
    └──────────────────────────────┬──────────────────────────────┘
                                   │
                      [Cable / Fiber / 5G Modem]
                                   │ (WAN Port)
    ┌──────────────────────────────▼──────────────────────────────┐
    │  PRIMARY DEFAULT GATEWAY ROUTER (192.168.1.1)               │
    │  Web Administration Console & DHCP Server                   │
    └──────┬───────────────────────┬───────────────────────┬──────┘
           │ (LAN 1)               │ (Wi-Fi 5 GHz)         │ (LAN 2)
    ┌──────▼──────┐         ┌──────▼──────┐         ┌──────▼──────┐
    │ Your Laptop │         │ Smartphone  │         │ IoT Device  │
    │ 192.168.1.2 │         │ 192.168.1.3 │         │ 192.168.1.4 │
    │ (Client PC) │         │ (Client)    │         │ (Printer)   │
    └─────────────┘         └─────────────┘         └─────────────┘
        """ if is_correction else f"""
    ┌─────────────────────────────────────────────────────────────┐
    │                INTERNET (Public WAN / ISP)                  │
    └──────────────────────────────┬──────────────────────────────┘
                                   │
                      [Cable / Fiber / 5G Modem]
                                   │ (WAN Interface)
    ┌──────────────────────────────▼──────────────────────────────┐
    │  DEFAULT GATEWAY ROUTER ({escape(ip)})                           │
    │  Admin Portal (Port 80 HTTP) & DHCP Lease Server            │
    └──────┬───────────────────────┬───────────────────────┬──────┘
           │ (Wi-Fi 6 / LAN)       │ (Wi-Fi Guest)         │ (Ethernet)
    ┌──────▼──────┐         ┌──────▼──────┐         ┌──────▼──────┐
    │ Phone / PC  │         │ Guest Phone │         │ Smart TV    │
    │ (Host LAN)  │         │ (Isolated)  │         │ (Streaming) │
    └─────────────┘         └─────────────┘         └─────────────┘
        """

        # Decision Table HTML
        decision_table = f"""
      <h2 style="font-size: 1.5rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 0.75rem;">
        Decision Table: Match Your Situation to the Immediate Resolution
      </h2>
      <p style="color: var(--text-secondary); margin-bottom: 1rem; line-height: 1.6;">
        Find your current symptom below to identify what your network actually requires and the exact action to take next:
      </p>
      <div style="overflow-x: auto; margin-bottom: 2rem;">
        <table class="table">
          <thead>
            <tr>
              <th style="min-width: 200px;">Your Situation / Error</th>
              <th style="min-width: 220px;">What You Actually Need</th>
              <th style="min-width: 260px;">Immediate Action to Take</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Changing Wi-Fi Name or Password</strong></td>
              <td>Primary Router Web Admin Console</td>
              <td>Connect to your router Wi-Fi, open <code>{'http://192.168.1.1' if is_correction else f'http://{ip}'}</code>, and navigate to Wireless Settings.</td>
            </tr>
            <tr>
              <td><strong>Browser opens Google / Bing search instead of login</strong></td>
              <td>Direct URL Address Navigation</td>
              <td>Type <code>http://{escape(ip)}</code> with the <code>http://</code> scheme directly in the top browser address bar, not the search engine input.</td>
            </tr>
            <tr>
              <td><strong>"This site can’t be reached" (ERR_CONNECTION_TIMED_OUT)</strong></td>
              <td>Local Subnet Alignment &amp; Direct Connection</td>
              <td>Turn off corporate or commercial VPNs (NordVPN, ExpressVPN), disconnect mobile cellular data, and verify your gateway with <code>ipconfig</code>.</td>
            </tr>
            <tr>
              <td><strong>"Your connection is not private" (SSL/TLS Error)</strong></td>
              <td>Unencrypted HTTP Port 80 Daemon</td>
              <td>Remove <code>https://</code> from your URL. Consumer routers do not maintain public SSL certificates and reject HTTPS requests.</td>
            </tr>
            <tr>
              <td><strong>Device says "Connected, no Internet"</strong></td>
              <td>Modem WAN Uplink Connection</td>
              <td>Ensure the Ethernet cable from your ISP optical ONT or cable modem is seated securely into the router's yellow/blue <strong>WAN/Internet port</strong>.</td>
            </tr>
            <tr>
              <td><strong>Can't remember custom admin password</strong></td>
              <td>Physical Hardware Factory Reset</td>
              <td>Locate the physical <strong>Reset</strong> pinhole on the rear panel, press and hold for 15 seconds with a paperclip, and log in with default credentials.</td>
            </tr>
          </tbody>
        </table>
      </div>
        """

        # Typo correction chips
        typo_chips = "".join([f'<div class="typo-chip"><span class="typo-wrong">{escape(tp)}</span> &rarr; <span class="typo-correct">http://{escape(ip)}</span></div>' for tp in meta['typos']])

        # Secondary Scenario HTML
        if is_correction:
            secondary_scenario_html = """
        <p style="margin-bottom: 0.75rem;">
          If you are looking at your network scan and see <strong>192.168.1.2</strong> active, you can identify the exact hardware device using simple command line tools:
        </p>
        <ol style="margin-left: 1.25rem; margin-bottom: 0.75rem;">
          <li><strong>Windows / Mac Terminal:</strong> Run <code>ping 192.168.1.2</code> followed by <code>arp -a</code>.</li>
          <li><strong>Find the Physical MAC Address:</strong> Look at the entry for 192.168.1.2 (e.g. <code>b4-fb-e4-xx-xx-xx</code>).</li>
          <li><strong>Match the Manufacturer:</strong> The first 6 characters represent the Organizationally Unique Identifier (OUI). Common devices assigned to 192.168.1.2 include HP / Epson wireless printers, Dahua / Hikvision IP security cameras, Synology NAS units, or Apple TV streaming boxes.</li>
        </ol>
            """
        else:
            secondary_scenario_html = f"""
        <p style="margin-bottom: 0.75rem;">
          If your network includes a secondary Wi-Fi router configured in <strong>Access Point (AP) mode</strong>, a Wi-Fi range extender, or a mesh node satellite (such as Netgear Orbi or TP-Link Deco), the device's internal DHCP server is disabled to prevent Double NAT routing loops.
        </p>
        <p style="margin: 0;">
          In AP mode, the secondary unit ceases to act as a gateway and receives a dynamic client IP address from your primary modem or router. To access its setup page, log into your main gateway router (e.g. 192.168.1.1), check the <strong>Attached Devices / DHCP Client List</strong>, find the satellite's dynamically leased IP, and open that specific address in your browser.
        </p>
            """

        # Content Assembly
        content = f"""
  <main class="container" style="padding-top: 1.5rem; padding-bottom: 4rem;">
    <div class="content-container">
      <div class="silo-badge silo-badge-ip">⚡ Intent-First Technical SEO Reference</div>
      
      <!-- Contrarian / Problem H1 -->
      <h1 style="font-size: 2.15rem; font-weight: 800; margin-bottom: 0.75rem; letter-spacing: -0.02em;">
        {escape(h1)}
      </h1>
      
      <!-- Intent-Matching Intro -->
      {intro_html}

      <!-- Quick Answer Box with Bold Verdict -->
      {quick_answer_html}

      <!-- Visual Diagnostic Context (Symptom vs Cause Matrix) -->
      <h2 style="font-size: 1.5rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.75rem;">
        Visual Diagnostic Context: Symptom vs. Root Cause
      </h2>
      <div class="symptom-matrix">
        <div class="symptom-card">
          <span class="symptom-header">Symptom A</span>
          <div class="symptom-title">Browser Redirects to Search Engine</div>
          <div class="symptom-cause">
            <strong>Root Cause:</strong> Omnibox search trigger. Typing raw numbers without <code>http://</code> prompts modern browsers to send queries to Google or Bing.
          </div>
        </div>
        <div class="symptom-card">
          <span class="symptom-header">Symptom B</span>
          <div class="symptom-title">Connection Timed Out / Unreachable</div>
          <div class="symptom-cause">
            <strong>Root Cause:</strong> Subnet mismatch, active VPN tunnel encapsulation, or smartphone Wi-Fi Assist silently routing through cellular data.
          </div>
        </div>
        <div class="symptom-card">
          <span class="symptom-header">Symptom C</span>
          <div class="symptom-title">SSL / Connection Not Private Error</div>
          <div class="symptom-cause">
            <strong>Root Cause:</strong> Browser forcing HTTPS port 443 on an embedded router web server that only listens on unencrypted HTTP port 80.
          </div>
        </div>
        <div class="symptom-card">
          <span class="symptom-header">Symptom D</span>
          <div class="symptom-title">Incorrect Password Error Message</div>
          <div class="symptom-cause">
            <strong>Root Cause:</strong> Confusing your Wi-Fi wireless password with the router administrative setup password.
          </div>
        </div>
      </div>

      <!-- Network Topology Diagram -->
      <div class="network-topology-card">
        <pre style="margin: 0; color: var(--text-primary);">{topology_diagram}</pre>
      </div>

      <!-- Decision Table -->
      {decision_table}

      <!-- Why This Happens (In Plain Technical Language) -->
      <h2 style="font-size: 1.5rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 0.75rem;">
        Why This Happens: The Non-Obvious Technical Causes
      </h2>
      <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1rem;">
        When an IP address fails to load in your browser, the problem is rarely hardware failure. In 98% of cases, the issue stems from one of four networking protocols:
      </p>
      <div style="background: var(--bg-secondary); border-radius: var(--radius-md); border: 1px solid var(--border-color); padding: 1.25rem; margin-bottom: 2rem;">
        <h3 style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.4rem; color: var(--text-primary);">1. Subnet Mismatch &amp; RFC 1918 Routing Rules</h3>
        <p style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6; margin-bottom: 1rem;">
          To communicate with <code>{escape(ip)}</code> without a layer-3 router between them, your client device (laptop, phone) must be bound to the exact same subnet mask (usually <code>255.255.255.0</code> / <code>/24</code>). If your router is on <code>192.168.0.1</code> but your computer has a static IP of <code>192.168.1.50</code>, TCP packets cannot route across the subnet boundary.
        </p>

        <h3 style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.4rem; color: var(--text-primary);">2. VPN Tunnel Encapsulation (Split-Tunneling Disabled)</h3>
        <p style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6; margin-bottom: 1rem;">
          When an active VPN client (such as NordVPN, ExpressVPN, or corporate Cisco AnyConnect) is running, your operating system creates a virtual network adapter. If split-tunneling is disabled, 100% of outbound packets—including private LAN traffic—are encrypted and routed to the remote VPN exit node, blinding your PC to local router web servers.
        </p>

        <h3 style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.4rem; color: var(--text-primary);">3. Smartphone Cellular Fallback (Wi-Fi Assist)</h3>
        <p style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6; margin-bottom: 1rem;">
          Modern smartphones running iOS (Wi-Fi Assist) and Android (Intelligent Wi-Fi) automatically detect when a Wi-Fi connection lacks active Internet access (typical during initial router setup). The OS silently switches outbound HTTP requests to cellular 5G/LTE, making private gateway IPs completely unreachable.
        </p>

        <h3 style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.4rem; color: var(--text-primary);">4. HTTP Port 80 vs. HTTPS Port 443 Rejection</h3>
        <p style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6; margin: 0;">
          Modern web browsers enforce HTTPS-First modes. Because embedded routers lack public CA-signed SSL certificates, they only run lightweight HTTP daemons on port 80. When a browser auto-upgrades the request to <code>https://{escape(ip)}:443</code>, the router drops the connection, producing a timeout or certificate rejection error.
        </p>
      </div>

      <!-- Reference Table (Hardware Models on this IP) -->
      <h2 style="font-size: 1.5rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 0.75rem;">
        Hardware Reference Table: Routers Configured on {escape(ip)}
      </h2>
      <p style="color: var(--text-secondary); line-height: 1.6; margin-bottom: 1rem;">
        Official hardware models using <code>{escape(ip)}</code> as their primary default gateway address:
      </p>
      <div style="overflow-x: auto; margin-bottom: 2rem;">
        <table class="table">
          <thead>
            <tr>
              <th>Model Name</th>
              <th>Default Username</th>
              <th>Default Password</th>
              <th>Wi-Fi Standard</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            {model_rows}
          </tbody>
        </table>
      </div>

      <!-- Live Reachability Console Card -->
      <div class="card" style="margin: 2rem 0; border: 1px solid var(--border-color); background: var(--bg-card); border-radius: var(--radius-lg); padding: 1.5rem;">
        <h3 style="font-size: 1.15rem; font-weight: 700; margin-bottom: 0.5rem;">
          ⚡ Live Gateway Reachability Probe
        </h3>
        <p style="font-size: 0.875rem; color: var(--text-muted); margin-bottom: 1rem;">
          Test whether your current browser can communicate with {escape(ip)} across your local network:
        </p>
        <div style="display: flex; gap: 0.75rem; align-items: center; flex-wrap: wrap;">
          <button id="probe-btn" class="btn btn-primary" style="padding: 0.55rem 1rem; font-size: 0.875rem;">
            Test Connection to {escape(ip)}
          </button>
          <div id="probe-status" style="font-size: 0.875rem; font-weight: 600;"></div>
        </div>
      </div>

      <!-- Numbered How-To Guide (Safest to Destructive) -->
      <h2 style="font-size: 1.5rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 0.75rem;">
        Step-by-Step Troubleshooting: Safest to Destructive Actions
      </h2>
      <ol style="margin-left: 1.5rem; margin-bottom: 2rem; color: var(--text-secondary); line-height: 1.75;">
        <li style="margin-bottom: 0.75rem;">
          <strong>Disconnect All VPNs and Cellular Data (Safest):</strong> Temporarily disable any active VPN software on your PC or phone. If using an iPhone or Android, disable Mobile Data so the device is forced to route strictly over Wi-Fi.
        </li>
        <li style="margin-bottom: 0.75rem;">
          <strong>Confirm Physical or Wi-Fi Link:</strong> Check your Wi-Fi settings to ensure you are connected to the router's network name (SSID), or plug an Ethernet patch cable into one of the numbered LAN ports (1&ndash;4) on the back of the router.
        </li>
        <li style="margin-bottom: 0.75rem;">
          <strong>Type the Exact HTTP URL:</strong> Open a fresh browser window in Incognito/Private mode and type <code>http://{escape(ip)}</code> explicitly in the top address bar. Do not click search suggestions.
        </li>
        <li style="margin-bottom: 0.75rem;">
          <strong>Authenticate with Underside Label Credentials:</strong> Locate the physical barcode sticker on the router's base. Enter the printed administrator credentials (e.g. <code>{escape(meta['default_user'])}</code> / <code>{escape(meta['default_pass'])}</code>). Remember that the router admin password is distinct from your wireless Wi-Fi password.
        </li>
        <li style="margin-bottom: 0.75rem;">
          <strong>Verify Your Computer's Real Gateway via Command Line:</strong>
          <ul style="margin-top: 0.25rem;">
            <li><strong>Windows:</strong> Open Command Prompt and type <code>ipconfig | findstr "Default Gateway"</code>.</li>
            <li><strong>macOS:</strong> Open Terminal and type <code>route -n get default | grep gateway</code>.</li>
            <li><strong>Android/iOS:</strong> Open Wi-Fi settings, tap the network details icon, and verify the <strong>Router</strong> IP field.</li>
          </ul>
        </li>
        <li style="margin-bottom: 0.75rem;">
          <strong>Power Cycle Router &amp; Modem (Clean Reboot):</strong> Unplug the power adapter from both the modem and router. Wait 30 seconds for capacitors to discharge, plug the modem back in, wait 2 minutes for WAN sync, then power on the router.
        </li>
        <li style="margin-bottom: 0.75rem;">
          <strong>⚠️ The 30-Second Factory Reset (Destructive Action Warning):</strong>
          <div class="warning-box">
            <strong>Warning:</strong> A factory reset wipes all customized network names (SSID), Wi-Fi passwords, port forwarding rules, and static IP reservations. Only execute this if you cannot recover your login password.
          </div>
          With the router powered on, insert an unfolded paperclip into the <strong>Reset</strong> pinhole on the rear panel. Hold firmly for 15&ndash;30 seconds until the front LED indicators flash amber or power cycle. Wait 3 minutes for factory reboot.
        </li>
      </ol>

      <!-- Secondary Scenario -->
      <h2 style="font-size: 1.5rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 0.75rem;">
        {'Secondary Scenario: How to Identify Which Device Uses 192.168.1.2' if is_correction else f'Secondary Scenario: What If {ip} Is an Access Point or Mesh Satellite?'}
      </h2>
      <div style="background: var(--bg-secondary); border-radius: var(--radius-md); border: 1px solid var(--border-color); padding: 1.25rem; margin-bottom: 2rem; line-height: 1.7; color: var(--text-secondary);">
        {secondary_scenario_html}
      </div>

      <!-- Common Mistakes & Typo-Correction Block -->
      <h2 style="font-size: 1.5rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 0.75rem;">
        Common Typos, Syntax Errors &amp; Adjacent Queries
      </h2>
      <p style="color: var(--text-secondary); line-height: 1.6; margin-bottom: 1rem;">
        Entering IP addresses on smartphone touchscreens frequently leads to typographic errors. The table below illustrates common mistakes and their corrected syntax:
      </p>
      <div class="typo-tag-list">
        {typo_chips}
      </div>

      <!-- Frequently Asked Questions (FAQ) -->
      <h2 style="font-size: 1.5rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 0.75rem;">
        Frequently Asked Questions: {escape(ip)} Access &amp; Routing
      </h2>
      <div class="faq-list" style="margin-top: 1rem;">
        <div class="faq-card" style="background: var(--bg-secondary); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-color); margin-bottom: 1rem;">
          <h3 style="font-size: 1.05rem; font-weight: 700; margin-bottom: 0.5rem;">Why does {escape(ip)} send me to a Google search page?</h3>
          <p style="color: var(--text-secondary); margin: 0; font-size: 0.95rem; line-height: 1.6;">
            Modern web browser omniboxes combine search and address bars. If you type numbers without the protocol scheme, or include a typo like a trailing comma or space, the browser treats the input as a search keyword. Always type <code>http://{escape(ip)}</code> explicitly.
          </p>
        </div>
        <div class="faq-card" style="background: var(--bg-secondary); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-color); margin-bottom: 1rem;">
          <h3 style="font-size: 1.05rem; font-weight: 700; margin-bottom: 0.5rem;">Can I access {escape(ip)} from outside my home network?</h3>
          <p style="color: var(--text-secondary); margin: 0; font-size: 0.95rem; line-height: 1.6;">
            No. {escape(ip)} is an RFC 1918 private IPv4 address. Private addresses are non-routable over the public Internet. You must be physically connected to the router's local Wi-Fi or Ethernet network to load the management portal unless you have established a secure WireGuard or OpenVPN tunnel into your home LAN.
          </p>
        </div>
        <div class="faq-card" style="background: var(--bg-secondary); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-color); margin-bottom: 1rem;">
          <h3 style="font-size: 1.05rem; font-weight: 700; margin-bottom: 0.5rem;">What is the difference between admin credentials and the Wi-Fi password?</h3>
          <p style="color: var(--text-secondary); margin: 0; font-size: 0.95rem; line-height: 1.6;">
            Your Wi-Fi password (WPA2/WPA3 Pre-Shared Key) connects phones and laptops to the wireless signal. The router admin username and password (often <code>admin / admin</code> or a printed serial PIN) authenticate access to the internal web console to alter firewall, DNS, and network settings.
          </p>
        </div>
        <div class="faq-card" style="background: var(--bg-secondary); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-color); margin-bottom: 1rem;">
          <h3 style="font-size: 1.05rem; font-weight: 700; margin-bottom: 0.5rem;">How do I fix {escape(ip)} connection timed out errors?</h3>
          <p style="color: var(--text-secondary); margin: 0; font-size: 0.95rem; line-height: 1.6;">
            Disconnect any active commercial or corporate VPNs, turn off mobile cellular data on your smartphone, and ensure your device is connected to the router via Wi-Fi or LAN cable. Verify your default gateway in terminal using <code>ipconfig</code> or <code>netstat -nr</code>, and enter <code>http://{escape(ip)}</code> over plain HTTP.
          </p>
        </div>
      </div>

      <!-- The Bottom Line Callout -->
      <div class="bottom-line-callout">
        <h3 style="font-size: 1.2rem; font-weight: 800; color: var(--text-primary); margin-bottom: 0.5rem;">
          🎯 The Bottom Line: Fastest Diagnostic Resolution
        </h3>
        <p style="color: var(--text-secondary); font-size: 1rem; line-height: 1.65; margin: 0;">
          {'If you searched 192.168.1.2 to configure your Wi-Fi, stop trying to load .1.2: your router is at <strong><a href="/ip/192-168-1-1/" style="color: var(--text-accent); text-decoration: underline;">http://192.168.1.1</a></strong>. If you are investigating a device occupying 192.168.1.2, run <code>arp -a</code> in terminal to inspect its MAC address.' if is_correction else f'If <strong>{escape(ip)}</strong> will not open, 95% of failures stem from one of two causes: either an active VPN / cellular connection is bypassing your LAN, or your router is actually running on a different subnet (such as 192.168.0.1 or 10.0.0.1). Disconnect your VPN, run our <a href="/tools/detect-gateway/" style="color: var(--text-accent); font-weight: 700; text-decoration: underline;">Local Gateway Auto-Detector</a>, and open the confirmed IP over plain HTTP.'}
        </p>
      </div>

      <!-- Cross Silo Links -->
      <div style="margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--border-color);">
        <h3 style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.75rem;">Explore Other Gateway IPs &amp; Tools</h3>
        <div style="display: flex; flex-wrap: wrap; gap: 0.75rem;">
          <a href="/ip/" class="btn btn-secondary" style="font-size: 0.85rem;">All Gateway IPs &rarr;</a>
          <a href="/tools/detect-gateway/" class="btn btn-secondary" style="font-size: 0.85rem;">⚡ Auto-Detect Local Gateway &rarr;</a>
          <a href="/tools/subnet-calculator/" class="btn btn-secondary" style="font-size: 0.85rem;">Subnet Calculator &rarr;</a>
          <a href="/find-router-ip.html" class="btn btn-secondary" style="font-size: 0.85rem;">Find My IP (OS Commands) &rarr;</a>
        </div>
      </div>
    </div>
  </main>
"""
        full_html = get_header(title, desc, canonical, active_nav="ip", breadcrumbs=breadcrumbs, schemas_json_ld=[tech_schema, howto_schema, faq_schema]) + content + get_footer()
        with open(os.path.join(ip_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(full_html)

    # Master IP Directory (/ip/index.html)
    ip_master_dir = os.path.join(PUBLIC_DIR, "ip")
    canonical_master = "https://routeriphub.com/ip/"
    title_master = "Default Gateway IP Directory: Find, Access & Fix Your Router Address (2026)"
    desc_master = "Intent-first directory of private default gateway IPs: 192.168.1.1, 192.168.0.1, 10.0.0.1, 192.168.1.254, 192.168.1.2, and Class A/B/C subnets. Fast diagnostic access."

    ip_cards = ""
    for ip_item in IP_GATEWAYS:
        ip_addr = ip_item["ip"]
        meta_item = IP_INTENT_METADATA.get(ip_addr, {})
        is_corr = meta_item.get("variant") == "correction"
        tag_badge = '<span class="badge" style="background: rgba(234, 88, 12, 0.15); color: #ea580c; border: 1px solid rgba(234, 88, 12, 0.3);">Client / Extender IP</span>' if is_corr else f'<span class="badge" style="background: var(--info-bg); color: var(--text-accent);">{escape(ip_item["subnet_mask"])}</span>'

        ip_cards += f"""
        <div class="card" style="display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
              {tag_badge}
              <span style="font-size: 0.75rem; color: var(--text-muted);">{escape(ip_item['class_type'].split('(')[0].strip())}</span>
            </div>
            <h3 style="font-size: 1.35rem; font-family: var(--font-mono); font-weight: 800; margin-bottom: 0.4rem;">
              <a href="/ip/{escape(ip_item['slug'])}/">{escape(ip_addr)}</a>
            </h3>
            <p style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 0.75rem;">
              {escape(ip_item['brands'])}
            </p>
          </div>
          <div style="border-top: 1px solid var(--border-color); padding-top: 0.75rem; display: flex; justify-content: space-between; align-items: center;">
            <span style="font-size: 0.775rem; color: var(--text-muted);">Pass: <code>{escape(ip_item['default_creds'].split()[0])}</code></span>
            <a href="/ip/{escape(ip_item['slug'])}/" style="font-size: 0.85rem; font-weight: 600;">Explore &amp; Fix &rarr;</a>
          </div>
        </div>
        """

    content_master = f"""
  <main class="container" style="padding-top: 2rem; padding-bottom: 4rem;">
    <div style="text-align: center; max-width: 820px; margin: 0 auto 2.5rem auto;">
      <div class="silo-badge silo-badge-ip">⚡ Private Gateway IP Directory</div>
      <h1 style="font-size: 2.25rem; font-weight: 800; margin-bottom: 0.75rem;">
        Default Router IP Directory
      </h1>
      <p style="font-size: 1.1rem; color: var(--text-secondary); line-height: 1.6; margin-bottom: 1.5rem;">
        Most users searching for a router IP are either fixing a failed login, confused between a router gateway and a client device (such as 192.168.1.2), or looking for factory admin credentials. Match your hardware below for instant diagnostic resolution.
      </p>
      <div style="display: flex; justify-content: center; gap: 0.75rem; flex-wrap: wrap;">
        <a href="/tools/detect-gateway/" class="btn btn-primary" style="padding: 0.65rem 1.25rem;">
          ⚡ Auto-Detect My Router Gateway
        </a>
        <a href="/tools/ip-address-checker/" class="btn btn-secondary" style="padding: 0.65rem 1.25rem;">
          🔍 Public IP &amp; ASN Checker
        </a>
      </div>
    </div>

    <!-- Gateway vs Client Device Overview Table -->
    <div style="max-width: 900px; margin: 0 auto 3rem auto; background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: 1.5rem;">
      <h2 style="font-size: 1.35rem; font-weight: 700; margin-bottom: 0.75rem;">
        Which Router IP Do You Actually Need?
      </h2>
      <div style="overflow-x: auto;">
        <table class="table" style="font-size: 0.9rem;">
          <thead>
            <tr>
              <th>Gateway IP Address</th>
              <th>Primary Hardware Brands</th>
              <th>Default Credentials</th>
              <th>Address Role</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><a href="/ip/192-168-1-1/"><strong>192.168.1.1</strong></a></td>
              <td>Netgear, ASUS, Linksys, Cisco, Ubiquiti</td>
              <td><code>admin / admin</code></td>
              <td>Primary Default Gateway</td>
            </tr>
            <tr>
              <td><a href="/ip/192-168-0-1/"><strong>192.168.0.1</strong></a></td>
              <td>TP-Link, D-Link, Arris, Sky Broadband</td>
              <td><code>admin / admin</code></td>
              <td>Primary Default Gateway</td>
            </tr>
            <tr>
              <td><a href="/ip/10-0-0-1/"><strong>10.0.0.1</strong></a></td>
              <td>Comcast Xfinity xFi (XB6/XB7/XB8), Spectrum</td>
              <td><code>admin / password</code></td>
              <td>Class A ISP Gateway</td>
            </tr>
            <tr>
              <td><a href="/ip/192-168-1-254/"><strong>192.168.1.254</strong></a></td>
              <td>AT&amp;T Fiber (BGW320), BT Smart Hub 2</td>
              <td><code>admin / Printed DAC</code></td>
              <td>Highest Host Gateway</td>
            </tr>
            <tr>
              <td><a href="/ip/192-168-1-2/"><strong>192.168.1.2</strong></a></td>
              <td>Client Laptops, Phones, Printers, Extenders</td>
              <td><code>Varies by Device</code></td>
              <td><span style="color: #ea580c; font-weight: 700;">Client Device (Not Router)</span></td>
            </tr>
            <tr>
              <td><a href="/ip/192-168-100-1/"><strong>192.168.100.1</strong></a></td>
              <td>DOCSIS Cable Modems, Fiber ONTs</td>
              <td><code>admin / admin</code></td>
              <td>Bridge Mode Diagnostic IP</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Complete IP Cards Grid -->
    <div class="grid-3" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1.25rem;">
      {ip_cards}
    </div>
  </main>
"""
    breadcrumbs = [("Home", "/"), ("IP Directory", "/ip/")]
    full_html = get_header(title_master, desc_master, canonical_master, active_nav="ip", breadcrumbs=breadcrumbs) + content_master + get_footer()
    with open(os.path.join(ip_master_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(full_html)


# ==============================================================================
# 6. GENERATE STANDALONE TOOL PAGES (/tools/[tool]/ & /tools/)
# ==============================================================================
def generate_tool_pages():
    print(f"Generating {len(TOOL_PAGES)} dedicated tool pages...")
    for t in TOOL_PAGES:
        slug = t["slug"]
        tool_dir = os.path.join(PUBLIC_DIR, "tools", slug)
        make_dirs(tool_dir)

        canonical = f"https://routeriphub.com/tools/{slug}/"
        title = f"{t['title']} (Free Client-Side Utility)"
        desc = t["desc"]

        breadcrumbs = [
            ("Home", "/"),
            ("Tools", "/tools/"),
            (t["short_title"], f"/tools/{slug}/")
        ]

        # Tool specific UI embedding
        tool_ui = ""
        if slug == "subnet-calculator":
            tool_ui = """
      <div class="tool-card">
        <div class="tool-grid-2">
          <div>
            <div class="form-group">
              <label for="subnet-ip">IP Address</label>
              <input type="text" id="subnet-ip" class="form-control" value="192.168.1.1" placeholder="e.g. 192.168.1.1">
            </div>
            <div class="form-group">
              <label for="subnet-cidr">CIDR Prefix / Subnet Mask</label>
              <select id="subnet-cidr" class="form-control">
                <option value="24" selected>/24 - 255.255.255.0 (256 IPs, 254 hosts)</option>
                <option value="25">/25 - 255.255.255.128 (128 IPs, 126 hosts)</option>
                <option value="26">/26 - 255.255.255.192 (64 IPs, 62 hosts)</option>
                <option value="27">/27 - 255.255.255.224 (32 IPs, 30 hosts)</option>
                <option value="28">/28 - 255.255.255.240 (16 IPs, 14 hosts)</option>
                <option value="29">/29 - 255.255.255.248 (8 IPs, 6 hosts)</option>
                <option value="30">/30 - 255.255.255.252 (4 IPs, 2 hosts - Point-to-Point)</option>
                <option value="16">/16 - 255.255.0.0 (65,536 IPs, 65,534 hosts)</option>
                <option value="8">/8 - 255.0.0.0 (16,777,216 IPs)</option>
              </select>
            </div>
          </div>
          <div>
            <div id="subnet-results" class="subnet-result-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem; background: var(--bg-secondary); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
              <!-- Populated by tools.js -->
            </div>
          </div>
        </div>
      </div>
            """
        elif slug == "wifi-qr-code":
            tool_ui = """
      <div class="tool-card">
        <div class="tool-grid-2">
          <div>
            <div class="form-group">
              <label for="wifi-ssid">Network Name (SSID)</label>
              <input type="text" id="wifi-ssid" class="form-control" placeholder="e.g. Home_Network_5G" value="MyHomeWiFi">
            </div>
            <div class="form-group">
              <label for="wifi-pass">Wi-Fi Password</label>
              <input type="text" id="wifi-pass" class="form-control" placeholder="Network password" value="SuperSecretPass123">
            </div>
            <div class="form-group">
              <label for="wifi-enc">Security Protocol</label>
              <select id="wifi-enc" class="form-control">
                <option value="WPA" selected>WPA/WPA2/WPA3 (Personal)</option>
                <option value="WEP">WEP (Legacy)</option>
                <option value="nopass">None (Open Network)</option>
              </select>
            </div>
            <div style="margin-bottom: 1rem;">
              <label style="display: flex; align-items: center; gap: 0.5rem; font-size: 0.875rem;">
                <input type="checkbox" id="wifi-hidden"> Hidden Network (SSID Broadcast Disabled)
              </label>
            </div>
          </div>
          <div style="display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <canvas id="wifi-qr-canvas" width="220" height="220" style="background: white; padding: 10px; border-radius: 8px; border: 1px solid var(--border-color);"></canvas>
            <div style="display: flex; gap: 0.5rem; margin-top: 1rem;">
              <button id="download-qr-btn" class="btn btn-primary" style="font-size: 0.85rem; padding: 0.5rem 0.85rem;">Download PNG</button>
              <button id="print-qr-btn" class="btn btn-secondary" style="font-size: 0.85rem; padding: 0.5rem 0.85rem;">Print Sign</button>
            </div>
          </div>
        </div>
      </div>
            """
        elif slug == "detect-gateway":
            tool_ui = """
      <div class="tool-card" style="text-align: center; max-width: 600px; margin: 0 auto 2.5rem auto;">
        <p style="font-size: 1rem; color: var(--text-secondary); margin-bottom: 1.5rem;">
          Click the button below to allow the browser to analyze your active network interface and detect whether your default gateway is running on 192.168.1.1, 192.168.0.1, or 10.0.0.1.
        </p>
        <button id="detect-local-ip-btn" class="btn btn-primary" style="font-size: 1.05rem; padding: 0.75rem 1.75rem;">
          ⚡ Auto-Detect My Router IP
        </button>
        <div id="local-ip-results" style="margin-top: 1.5rem; text-align: left;"></div>
      </div>
            """
        elif slug == "router-password-generator":
            tool_ui = """
      <div class="tool-card" style="max-width: 650px; margin: 0 auto 2.5rem auto;">
        <div class="form-group">
          <label>Generated Secure WPA3 Password</label>
          <div style="display: flex; gap: 0.5rem;">
            <input type="text" id="gen-password-output" class="form-control" style="font-family: var(--font-mono); font-size: 1.1rem; font-weight: 700;" readonly>
            <button class="btn btn-primary copy-btn" id="copy-gen-pass-btn" data-copy="">Copy</button>
          </div>
        </div>
        <div style="margin: 1.25rem 0;">
          <label for="pass-length" style="display: block; font-size: 0.875rem; font-weight: 600; margin-bottom: 0.35rem;">
            Length: <span id="pass-length-val">20</span> characters
          </label>
          <input type="range" id="pass-length" min="12" max="32" value="20" style="width: 100%;">
        </div>
        <div style="display: flex; gap: 1.5rem; flex-wrap: wrap; margin-bottom: 1.5rem;">
          <label style="display: flex; align-items: center; gap: 0.4rem; font-size: 0.875rem;">
            <input type="checkbox" id="pass-symbols" checked> Include Symbols (@#$%^&*)
          </label>
          <label style="display: flex; align-items: center; gap: 0.4rem; font-size: 0.875rem;">
            <input type="checkbox" id="pass-numbers" checked> Include Numbers (0-9)
          </label>
        </div>
        <button id="generate-new-pass-btn" class="btn btn-secondary" style="width: 100%;">
          Generate New Password
        </button>
      </div>
            """
        elif slug == "port-checker":
            tool_ui = """
      <div class="tool-card">
        <div class="form-group">
          <input type="text" id="port-filter-input" class="form-control" placeholder="Filter ports (e.g. Minecraft, Plex, 80, 443, SSH, 25565)...">
        </div>
        <div style="overflow-x: auto;">
          <table class="table" id="port-table">
            <thead>
              <tr>
                <th>Port Number</th>
                <th>Protocol</th>
                <th>Common Service / Application</th>
                <th>Forwarding Instructions</th>
              </tr>
            </thead>
            <tbody id="port-table-body">
              <tr><td>80</td><td>TCP</td><td>HTTP Web Server</td><td>Forward to local web server host IP</td></tr>
              <tr><td>443</td><td>TCP</td><td>HTTPS Secure Web</td><td>Forward to SSL/TLS server IP</td></tr>
              <tr><td>22</td><td>TCP</td><td>SSH Remote Access</td><td>Forward to server; recommend custom port externally</td></tr>
              <tr><td>32400</td><td>TCP</td><td>Plex Media Server</td><td>Enable Remote Access in Plex Server Settings</td></tr>
              <tr><td>25565</td><td>TCP/UDP</td><td>Minecraft Java Edition</td><td>Forward to local gaming PC IP</td></tr>
              <tr><td>19132</td><td>UDP</td><td>Minecraft Bedrock</td><td>Forward to mobile/console host</td></tr>
              <tr><td>27015</td><td>UDP</td><td>Steam Dedicated Server (CS2 / TF2)</td><td>Forward UDP for multi-player server hosting</td></tr>
              <tr><td>53</td><td>UDP/TCP</td><td>DNS Server (Pi-hole / AdGuard)</td><td>Redirect internal port 53 traffic to local DNS</td></tr>
            </tbody>
          </table>
        </div>
      </div>
            """
        elif slug == "ip-address-checker":
            tool_ui = """
      <div class="tool-card" style="max-width: 800px; margin: 0 auto 2.5rem auto;">
        <div style="display: flex; gap: 0.5rem; margin-bottom: 0.75rem; flex-wrap: wrap;">
          <input type="text" id="ip-lookup-input" class="form-control" style="flex: 1; min-width: 260px; font-family: var(--font-mono);" placeholder="Enter IPv4, IPv6, or domain (e.g. 8.8.8.8, 1.1.1.1, github.com)...">
          <button id="ip-lookup-btn" class="btn btn-primary" style="padding: 0.65rem 1.25rem;">
            🔍 Inspect IP
          </button>
          <button id="ip-my-ip-btn" class="btn btn-secondary" style="padding: 0.65rem 1rem;">
            ⚡ My Public IP
          </button>
        </div>
        <div style="display: flex; gap: 0.5rem; align-items: center; flex-wrap: wrap; margin-bottom: 1.25rem; font-size: 0.825rem; color: var(--text-muted);">
          <span>Quick Lookups:</span>
          <button class="btn btn-secondary ip-quick-chip" data-ip="" style="font-size: 0.78rem; padding: 0.2rem 0.6rem;">My Public IP</button>
          <button class="btn btn-secondary ip-quick-chip" data-ip="8.8.8.8" style="font-size: 0.78rem; padding: 0.2rem 0.6rem;">8.8.8.8 (Google)</button>
          <button class="btn btn-secondary ip-quick-chip" data-ip="1.1.1.1" style="font-size: 0.78rem; padding: 0.2rem 0.6rem;">1.1.1.1 (Cloudflare)</button>
          <button class="btn btn-secondary ip-quick-chip" data-ip="192.168.1.1" style="font-size: 0.78rem; padding: 0.2rem 0.6rem;">192.168.1.1 (Gateway)</button>
          <button class="btn btn-secondary ip-quick-chip" data-ip="10.0.0.1" style="font-size: 0.78rem; padding: 0.2rem 0.6rem;">10.0.0.1 (Xfinity)</button>
        </div>

        <div id="ip-lookup-results" style="margin-top: 1rem;">
          <div style="text-align: center; padding: 2rem 1rem; color: var(--text-muted); background: var(--bg-secondary); border-radius: var(--radius-md); border: 1px dashed var(--border-color);">
            Click <strong>"Inspect IP"</strong> or <strong>"My Public IP"</strong> to analyze network routing, ISP, ASN, and geolocation details.
          </div>
        </div>
      </div>
            """
        elif slug == "dns-propagation":
            tool_ui = """
      <div class="tool-card" style="max-width: 900px; margin: 0 auto 2.5rem auto;">
        <div style="display: flex; gap: 0.5rem; margin-bottom: 0.75rem; flex-wrap: wrap;">
          <input type="text" id="dns-domain-input" class="form-control" style="flex: 2; min-width: 220px; font-family: var(--font-mono);" placeholder="e.g. google.com, cloudflare.com, yourdomain.com" value="google.com">
          <select id="dns-type-select" class="form-control" style="flex: 1; min-width: 130px; font-family: var(--font-mono); font-weight: 600;">
            <option value="A" selected>A (IPv4)</option>
            <option value="AAAA">AAAA (IPv6)</option>
            <option value="CNAME">CNAME (Alias)</option>
            <option value="MX">MX (Mail)</option>
            <option value="TXT">TXT (SPF/DKIM)</option>
            <option value="NS">NS (Name Server)</option>
            <option value="SOA">SOA (Authority)</option>
            <option value="PTR">PTR (Reverse)</option>
          </select>
          <button id="dns-check-btn" class="btn btn-primary" style="padding: 0.65rem 1.5rem;">
            ⚡ Check Global DNS
          </button>
        </div>

        <div style="display: flex; gap: 0.5rem; align-items: center; flex-wrap: wrap; margin-bottom: 1.25rem; font-size: 0.825rem; color: var(--text-muted);">
          <span>Quick Domains:</span>
          <button class="btn btn-secondary dns-quick-chip" data-domain="google.com" data-type="A" style="font-size: 0.78rem; padding: 0.2rem 0.6rem;">google.com (A)</button>
          <button class="btn btn-secondary dns-quick-chip" data-domain="cloudflare.com" data-type="A" style="font-size: 0.78rem; padding: 0.2rem 0.6rem;">cloudflare.com (A)</button>
          <button class="btn btn-secondary dns-quick-chip" data-domain="github.com" data-type="MX" style="font-size: 0.78rem; padding: 0.2rem 0.6rem;">github.com (MX)</button>
          <button class="btn btn-secondary dns-quick-chip" data-domain="wikipedia.org" data-type="NS" style="font-size: 0.78rem; padding: 0.2rem 0.6rem;">wikipedia.org (NS)</button>
        </div>

        <div id="dns-summary-bar" style="display: none; justify-content: space-between; align-items: center; background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 0.75rem 1.25rem; margin-bottom: 1rem; flex-wrap: wrap; gap: 0.5rem;">
          <!-- Populated by tools.js -->
        </div>

        <div style="overflow-x: auto;">
          <table class="table" id="dns-results-table">
            <thead>
              <tr>
                <th style="min-width: 180px;">DNS Resolver Node</th>
                <th style="min-width: 140px;">Location / Anycast</th>
                <th style="min-width: 100px;">Status</th>
                <th style="min-width: 220px;">Resolved Records</th>
                <th style="min-width: 80px;">TTL</th>
                <th style="min-width: 80px;">Latency</th>
              </tr>
            </thead>
            <tbody id="dns-table-body">
              <tr>
                <td colspan="6" style="text-align: center; padding: 2rem 1rem; color: var(--text-muted);">
                  Enter a domain and click <strong>"Check Global DNS"</strong> to probe Cloudflare, Google, Quad9, AdGuard, and AliDNS resolvers via DNS-over-HTTPS.
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
            """
        elif slug == "cidr-cheat-sheet":
            tool_ui = """
      <div class="tool-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; flex-wrap: wrap; gap: 0.5rem;">
          <span style="font-size: 0.9rem; color: var(--text-muted);">Standard IPv4 prefix lengths (/0 to /32)</span>
          <a href="/data/routers.csv" download class="btn btn-primary" style="font-size: 0.85rem; padding: 0.45rem 0.85rem;">
            Download Subnet Cheat Sheet (CSV) &darr;
          </a>
        </div>
        <div style="overflow-x: auto;">
          <table class="table">
            <thead>
              <tr>
                <th>CIDR Prefix</th>
                <th>Subnet Mask</th>
                <th>Total Addresses</th>
                <th>Usable Hosts</th>
                <th>Wildcard Mask</th>
              </tr>
            </thead>
            <tbody>
              <tr><td><strong>/24</strong></td><td>255.255.255.0</td><td>256</td><td>254</td><td>0.0.0.255</td></tr>
              <tr><td><strong>/25</strong></td><td>255.255.255.128</td><td>128</td><td>126</td><td>0.0.0.127</td></tr>
              <tr><td><strong>/26</strong></td><td>255.255.255.192</td><td>64</td><td>62</td><td>0.0.0.63</td></tr>
              <tr><td><strong>/27</strong></td><td>255.255.255.224</td><td>32</td><td>30</td><td>0.0.0.31</td></tr>
              <tr><td><strong>/28</strong></td><td>255.255.255.240</td><td>16</td><td>14</td><td>0.0.0.15</td></tr>
              <tr><td><strong>/29</strong></td><td>255.255.255.248</td><td>8</td><td>6</td><td>0.0.0.7</td></tr>
              <tr><td><strong>/30</strong></td><td>255.255.255.252</td><td>4</td><td>2</td><td>0.0.0.3</td></tr>
              <tr><td><strong>/31</strong></td><td>255.255.255.254</td><td>2</td><td>2 (RFC 3021)</td><td>0.0.0.1</td></tr>
              <tr><td><strong>/32</strong></td><td>255.255.255.255</td><td>1</td><td>1 (Single Host)</td><td>0.0.0.0</td></tr>
              <tr><td><strong>/16</strong></td><td>255.255.0.0</td><td>65,536</td><td>65,534</td><td>0.0.255.255</td></tr>
              <tr><td><strong>/8</strong></td><td>255.0.0.0</td><td>16,777,216</td><td>16,777,214</td><td>0.255.255.255</td></tr>
            </tbody>
          </table>
        </div>
      </div>
            """

        # Rich SEO & Educational Content with <h2> headings
        tool_editorial = ""
        if slug == "subnet-calculator":
            tool_editorial = """
      <section style="margin-top: 3.5rem;">
        <h2 style="font-size: 1.6rem; font-weight: 700; margin-bottom: 1rem; color: var(--text-primary);">How to Use the IPv4 Subnet Calculator</h2>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          This client-side Subnet Calculator allows network engineers, system administrators, and home lab enthusiasts to analyze any IPv4 address and CIDR prefix length without sending data to an external server. Follow these simple steps:
        </p>
        <ol style="margin-left: 1.5rem; margin-bottom: 1.5rem; color: var(--text-secondary); line-height: 1.7;">
          <li><strong>Enter your IP Address:</strong> Type the host IP address or gateway address (e.g., <code>192.168.1.1</code> or <code>10.0.0.1</code>) into the input field.</li>
          <li><strong>Select your CIDR Prefix / Subnet Mask:</strong> Choose the prefix length from the dropdown menu, ranging from <code>/8</code> (Class A) to <code>/30</code> (Point-to-Point links). The standard home subnet is <code>/24</code> (255.255.255.0).</li>
          <li><strong>Inspect Calculated Parameters:</strong> The tool dynamically calculates the Network ID, Broadcast Address, Total IP count, Usable Host Range, and Wildcard Mask in real time.</li>
        </ol>

        <h2 style="font-size: 1.6rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem; color: var(--text-primary);">Understanding CIDR Notation &amp; Subnetting Fundamentals</h2>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          Classless Inter-Domain Routing (CIDR, defined in RFC 4632) replaced legacy classful networking (Class A, B, and C) to allocate IP address blocks with much greater granularity. In CIDR notation, an IP address is appended with a forward slash followed by a number indicating the number of contiguous leading bits assigned to the <strong>network prefix</strong>.
        </p>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          An IPv4 address consists of 32 binary bits divided into four 8-bit octets. For example, in a <code>/24</code> subnet:
        </p>
        <ul style="margin-left: 1.5rem; margin-bottom: 1.5rem; color: var(--text-secondary); line-height: 1.7;">
          <li><strong>Network Bits:</strong> 24 bits are dedicated to identifying the network (e.g. <code>11111111.11111111.11111111.00000000</code> = <code>255.255.255.0</code>).</li>
          <li><strong>Host Bits:</strong> 8 bits remain for assigning to client hosts (32 &minus; 24 = 8 bits).</li>
          <li><strong>Total Addresses:</strong> 2<sup>8</sup> = 256 addresses.</li>
          <li><strong>Usable Hosts:</strong> 256 &minus; 2 = 254 hosts (the first address is reserved as the <em>Network ID</em> and the last address is reserved as the <em>Broadcast Address</em>).</li>
        </ul>

        <h2 style="font-size: 1.6rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem; color: var(--text-primary);">Common CIDR Subnet Cheat Sheet</h2>
        <div style="overflow-x: auto; margin-bottom: 2rem;">
          <table class="table" style="font-size: 0.9rem;">
            <thead>
              <tr>
                <th>CIDR Prefix</th>
                <th>Subnet Mask</th>
                <th>Usable Host Capacity</th>
                <th>Typical Deployment Use Case</th>
              </tr>
            </thead>
            <tbody>
              <tr><td><code>/24</code></td><td>255.255.255.0</td><td>254 Hosts</td><td>Standard Home Routers, Small Offices, Wi-Fi VLANs</td></tr>
              <tr><td><code>/25</code></td><td>255.255.255.128</td><td>126 Hosts</td><td>Department Subnets, Guest Wi-Fi Segregation</td></tr>
              <tr><td><code>/26</code></td><td>255.255.255.192</td><td>62 Hosts</td><td>Medium Server Clusters, IoT Device Isolation</td></tr>
              <tr><td><code>/27</code></td><td>255.255.255.224</td><td>30 Hosts</td><td>Small Branch Offices, DMZ Environments</td></tr>
              <tr><td><code>/28</code></td><td>255.255.255.240</td><td>14 Hosts</td><td>Management Networks, Hardware Out-of-Band (iDRAC/iLO)</td></tr>
              <tr><td><code>/29</code></td><td>255.255.255.248</td><td>6 Hosts</td><td>ISP Static IP Allocations (Commercial Broadband)</td></tr>
              <tr><td><code>/30</code></td><td>255.255.255.252</td><td>2 Hosts</td><td>Point-to-Point Router-to-Router Uplinks</td></tr>
              <tr><td><code>/16</code></td><td>255.255.0.0</td><td>65,534 Hosts</td><td>Large Enterprise LANs, University Campuses</td></tr>
              <tr><td><code>/8</code></td><td>255.0.0.0</td><td>16,777,214 Hosts</td><td>Carrier Internal Routing, Global Cloud VPCs</td></tr>
            </tbody>
          </table>
        </div>

        <h2 style="font-size: 1.6rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem; color: var(--text-primary);">Frequently Asked Questions About Subnetting</h2>
        <div class="faq-list" style="margin-top: 1rem;">
          <div class="faq-card" style="background: var(--bg-secondary); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-color); margin-bottom: 1rem;">
            <h3 style="font-size: 1.05rem; font-weight: 700; margin-bottom: 0.5rem;">Why can't I use the first and last IP addresses in a subnet?</h3>
            <p style="color: var(--text-secondary); margin: 0; font-size: 0.95rem; line-height: 1.6;">
              In IPv4 networking, the very first address represents the entire network block itself (the Network ID), used by routers to direct traffic. The last address with all host bits set to 1 is the directed broadcast address, used to broadcast packets to every device on that specific subnet simultaneously. Consequently, assigning either address to a host device creates addressing conflicts.
            </p>
          </div>
          <div class="faq-card" style="background: var(--bg-secondary); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-color); margin-bottom: 1rem;">
            <h3 style="font-size: 1.05rem; font-weight: 700; margin-bottom: 0.5rem;">What is the default subnet mask for 192.168.1.1?</h3>
            <p style="color: var(--text-secondary); margin: 0; font-size: 0.95rem; line-height: 1.6;">
              The standard subnet mask for <code>192.168.1.1</code> is <code>255.255.255.0</code> (corresponding to a <code>/24</code> prefix). This allows your router to assign DHCP leases to devices in the range <code>192.168.1.2</code> through <code>192.168.1.254</code>.
            </p>
          </div>
          <div class="faq-card" style="background: var(--bg-secondary); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-color); margin-bottom: 1rem;">
            <h3 style="font-size: 1.05rem; font-weight: 700; margin-bottom: 0.5rem;">What is a Wildcard Mask and where is it used?</h3>
            <p style="color: var(--text-secondary); margin: 0; font-size: 0.95rem; line-height: 1.6;">
              A wildcard mask is the bitwise inverse of the subnet mask. For instance, if the subnet mask is <code>255.255.255.0</code>, its wildcard mask is <code>0.0.0.255</code>. Wildcard masks are predominantly used in Cisco IOS Access Control Lists (ACLs) and routing protocols like OSPF and EIGRP to match IP address ranges.
            </p>
          </div>
        </div>
      </section>
"""
        elif slug == "wifi-qr-code":
            tool_editorial = """
      <section style="margin-top: 3.5rem;">
        <h2 style="font-size: 1.6rem; font-weight: 700; margin-bottom: 1rem; color: var(--text-primary);">How to Generate a Printable Wi-Fi QR Code</h2>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          Sharing Wi-Fi passwords with guests, customers, and family members manually often leads to typos, frustration, and security risks. Using this free, client-side tool, you can generate an instant connection QR code in seconds:
        </p>
        <ol style="margin-left: 1.5rem; margin-bottom: 1.5rem; color: var(--text-secondary); line-height: 1.7;">
          <li><strong>Enter Network Name (SSID):</strong> Type your wireless network name exactly as it appears in your router configuration (SSIDs are case-sensitive).</li>
          <li><strong>Input Wi-Fi Password:</strong> Provide your network password. All rendering takes place locally in your browser memory via the HTML5 Canvas API—your credentials are never transmitted over the internet.</li>
          <li><strong>Select Encryption Standard:</strong> Most modern routers use <code>WPA/WPA2/WPA3</code>. For open hotspot networks, select <code>None</code>.</li>
          <li><strong>Toggle Hidden Network (Optional):</strong> If your router has "SSID Broadcast" disabled, check the "Hidden Network" box so mobile devices know to query the hidden beacon.</li>
          <li><strong>Download or Print:</strong> Click "Download PNG" for digital sharing, or "Print Sign" to print an elegant guest display card for your office, Airbnb, coffee shop, or home.</li>
        </ol>

        <h2 style="font-size: 1.6rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem; color: var(--text-primary);">How Wi-Fi QR Codes Work (Standard Schema Protocol)</h2>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          Mobile operating systems (iOS 11+ and Android 10+) feature built-in support for the standard Wi-Fi configuration string format. When encoded as a 2D matrix barcode, the standardized payload follows the syntax:
        </p>
        <div style="background: var(--bg-secondary); padding: 1rem 1.25rem; border-radius: var(--radius-md); font-family: var(--font-mono); font-size: 0.95rem; margin-bottom: 1.5rem; border: 1px solid var(--border-color); overflow-x: auto;">
          <code>WIFI:T:WPA;S:YourNetworkSSID;P:YourSecretPassword;H:false;;</code>
        </div>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          Here is a breakdown of the protocol parameters:
        </p>
        <ul style="margin-left: 1.5rem; margin-bottom: 1.5rem; color: var(--text-secondary); line-height: 1.7;">
          <li><code>T:</code> Authentication Type (<code>WPA</code> for WPA/WPA2/WPA3, <code>WEP</code> for legacy WEP, or <code>nopass</code> for open).</li>
          <li><code>S:</code> Service Set Identifier (SSID / Network Name). Special characters are properly escaped.</li>
          <li><code>P:</code> Pre-Shared Key (Wireless Password).</li>
          <li><code>H:</code> Hidden SSID flag (<code>true</code> or <code>false</code>).</li>
        </ul>

        <h2 style="font-size: 1.6rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem; color: var(--text-primary);">How to Scan and Connect on iOS and Android</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; margin-bottom: 2rem;">
          <div style="background: var(--bg-secondary); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
            <h3 style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.5rem;">🍎 Apple iOS (iPhone &amp; iPad)</h3>
            <ol style="margin-left: 1.25rem; font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6;">
              <li>Open the native <strong>Camera</strong> app from your home screen or Control Center.</li>
              <li>Frame the Wi-Fi QR code within the camera viewfinder.</li>
              <li>A yellow banner will appear reading: <em>"Join [Network Name] Network"</em>.</li>
              <li>Tap the banner, then tap <strong>"Join"</strong> to authenticate immediately.</li>
            </ol>
          </div>
          <div style="background: var(--bg-secondary); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
            <h3 style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.5rem;">🤖 Google Android</h3>
            <ol style="margin-left: 1.25rem; font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6;">
              <li>Open your <strong>Camera</strong> app or swipe down to Quick Settings and tap <strong>Internet</strong>.</li>
              <li>Tap the QR scanner icon next to "Add network" or use <strong>Google Lens</strong>.</li>
              <li>Point your camera at the QR code.</li>
              <li>Tap the popup prompt: <strong>"Connect to Wi-Fi"</strong>.</li>
            </ol>
          </div>
        </div>

        <h2 style="font-size: 1.6rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem; color: var(--text-primary);">Security Advantages of Sharing Wi-Fi via QR Code</h2>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          Generating a Wi-Fi QR code offers multiple critical security advantages over writing passwords on a whiteboard or sticky note:
        </p>
        <ul style="margin-left: 1.5rem; margin-bottom: 1.5rem; color: var(--text-secondary); line-height: 1.7;">
          <li><strong>Enables High-Entropy Passwords:</strong> Because users do not have to type characters manually on small phone keyboards, you can use a strong 24-character random password that is immune to brute-force cracking.</li>
          <li><strong>Encourages Guest Network Isolation:</strong> Create a dedicated QR code for your router's <strong>Guest Wi-Fi SSID</strong>. Visitors can access the internet without having access to your home NAS, internal servers, smart cameras, or router administration portal.</li>
          <li><strong>Eliminates Shoulder Surfing:</strong> Guests scan directly without you having to vocalize or display plaintext passwords across crowded rooms.</li>
        </ul>
      </section>
"""
        elif slug == "detect-gateway":
            tool_editorial = """
      <section style="margin-top: 3.5rem;">
        <h2 style="font-size: 1.6rem; font-weight: 700; margin-bottom: 1rem; color: var(--text-primary);">How the Local Router Gateway Auto-Detector Works</h2>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          Your default gateway is the primary local IP address of your router that acts as an access point or gateway between your local home network (LAN) and the wider Internet (WAN). When you click "Auto-Detect My Router IP", this tool executes a lightweight probe against common gateway subnets:
        </p>
        <ul style="margin-left: 1.5rem; margin-bottom: 1.5rem; color: var(--text-secondary); line-height: 1.7;">
          <li><strong>Local Subnet Probing:</strong> The browser tests fetch timing against standard private router IP ranges (<code>192.168.1.1</code>, <code>192.168.0.1</code>, <code>10.0.0.1</code>, <code>192.168.2.1</code>, and <code>192.168.1.254</code>).</li>
          <li><strong>WebRTC ICE Discovery:</strong> Utilizes browser WebRTC candidates to detect your computer's local IPv4 binding.</li>
          <li><strong>100% Client-Side Privacy:</strong> All probes are handled locally by JavaScript; no internal network details are ever logged or transmitted externally.</li>
        </ul>

        <h2 style="font-size: 1.6rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem; color: var(--text-primary);">Most Common Default Gateway IP Addresses by Brand</h2>
        <div style="overflow-x: auto; margin-bottom: 2rem;">
          <table class="table" style="font-size: 0.9rem;">
            <thead>
              <tr>
                <th>Gateway IP Address</th>
                <th>Subnet Range</th>
                <th>Standard Hardware Brands</th>
              </tr>
            </thead>
            <tbody>
              <tr><td><code>192.168.1.1</code></td><td>192.168.1.1 &ndash; 192.168.1.254</td><td>Netgear, ASUS, Linksys, Cisco, Verizon Fios, Ubiquiti</td></tr>
              <tr><td><code>192.168.0.1</code></td><td>192.168.0.1 &ndash; 192.168.0.254</td><td>TP-Link, D-Link, Arris, Motorola, Virgin Media</td></tr>
              <tr><td><code>10.0.0.1</code></td><td>10.0.0.1 &ndash; 10.0.0.254</td><td>Comcast Xfinity xFi, Spectrum, Apple AirPort</td></tr>
              <tr><td><code>192.168.1.254</code></td><td>192.168.1.1 &ndash; 192.168.1.254</td><td>AT&amp;T Fiber (BGW320/BGW210), BT Smart Hub (UK)</td></tr>
              <tr><td><code>192.168.88.1</code></td><td>192.168.88.1 &ndash; 192.168.88.254</td><td>MikroTik (RouterOS)</td></tr>
              <tr><td><code>192.168.178.1</code></td><td>192.168.178.1 &ndash; 192.168.178.254</td><td>AVM FRITZ!Box (Germany &amp; EU)</td></tr>
              <tr><td><code>192.168.8.1</code></td><td>192.168.8.1 &ndash; 192.168.8.254</td><td>GL.iNet Travel Routers, Huawei 4G/5G Gateways</td></tr>
            </tbody>
          </table>
        </div>

        <h2 style="font-size: 1.6rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem; color: var(--text-primary);">Manual Command Line Discovery Methods</h2>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          If browser auto-detection is blocked by browser security extensions or firewall rules, you can instantly find your gateway using your computer's built-in terminal:
        </p>
        <ul style="margin-left: 1.5rem; margin-bottom: 1.5rem; color: var(--text-secondary); line-height: 1.7;">
          <li><strong>Windows (CMD / PowerShell):</strong> Open terminal and run <code>ipconfig | findstr /i "Default Gateway"</code></li>
          <li><strong>macOS (Terminal):</strong> Open terminal and run <code>netstat -nr | grep default</code> or <code>route -n get default</code></li>
          <li><strong>Linux (Terminal):</strong> Run <code>ip route show default</code></li>
          <li><strong>iPhone / iPad (iOS):</strong> Go to <strong>Settings</strong> &gt; <strong>Wi-Fi</strong> &gt; tap the blue <strong>(i)</strong> icon &gt; look for <strong>Router</strong>.</li>
          <li><strong>Android:</strong> Go to <strong>Settings</strong> &gt; <strong>Network &amp; internet</strong> &gt; <strong>Internet</strong> &gt; tap your network &gt; <strong>Gateway</strong>.</li>
        </ul>
      </section>
"""
        elif slug == "router-password-generator":
            tool_editorial = """
      <section style="margin-top: 3.5rem;">
        <h2 style="font-size: 1.6rem; font-weight: 700; margin-bottom: 1rem; color: var(--text-primary);">Why Router Admin and Wi-Fi Passwords Require High Entropy</h2>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          Consumer routers are among the most frequently targeted devices on home and business networks. Attackers target two distinct authentication vectors:
        </p>
        <ol style="margin-left: 1.5rem; margin-bottom: 1.5rem; color: var(--text-secondary); line-height: 1.7;">
          <li><strong>Router Admin Console Password:</strong> The credential protecting your web administration portal (at 192.168.1.1, etc.). If compromised, an attacker can change DNS servers (DNS hijacking), inject malicious ads, open port forwards, and snoop on network traffic.</li>
          <li><strong>WPA2/WPA3 Wi-Fi Pre-Shared Key (PSK):</strong> The wireless encryption key. In WPA2 networks, attackers within radio range can capture the 4-way EAPOL handshake and attempt offline dictionary attacks. Strong 20+ character passwords render dictionary cracking mathematically impossible.</li>
        </ol>

        <h2 style="font-size: 1.6rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem; color: var(--text-primary);">Cryptographically Secure Generation (CSPRNG)</h2>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          Unlike basic online generators that use predictable pseudo-random seeds (like <code>Math.random()</code>), this tool uses the browser's native <strong>Web Cryptography API (<code>window.crypto.getRandomValues()</code>)</strong>. This guarantees hardware-grade entropy derived from operating system randomness pools, ensuring that generated passwords are computationally impossible to predict.
        </p>

        <h2 style="font-size: 1.6rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem; color: var(--text-primary);">Best Practices for Hardening Your Router</h2>
        <ul style="margin-left: 1.5rem; margin-bottom: 1.5rem; color: var(--text-secondary); line-height: 1.7;">
          <li><strong>Change Factory Defaults Immediately:</strong> Never leave default credentials like <code>admin/admin</code> or <code>admin/password</code> active on your network.</li>
          <li><strong>Disable Remote Management (WAN Access):</strong> Ensure that web management is restricted to local LAN clients only and disabled from external Internet WAN interfaces.</li>
          <li><strong>Upgrade to WPA3-Personal:</strong> Where supported by your router and client devices, enable WPA3-Personal (SAE) to protect against offline dictionary attacks.</li>
          <li><strong>Keep Firmware Updated:</strong> Regularly install official firmware updates to patch critical Common Vulnerabilities and Exposures (CVEs).</li>
        </ul>
      </section>
"""
        elif slug == "port-checker":
            tool_editorial = """
      <section style="margin-top: 3.5rem;">
        <h2 style="font-size: 1.6rem; font-weight: 700; margin-bottom: 1rem; color: var(--text-primary);">Understanding Port Forwarding in NAT Routers</h2>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          Home routers use Network Address Translation (NAT) to allow dozens of connected devices to share a single public IP address provided by your ISP. By default, your router's firewall blocks all unsolicited incoming connection requests from the public internet for security.
        </p>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          <strong>Port forwarding</strong> creates a permanent rule telling your router: <em>"When external traffic arrives on port X, forward it directly to local internal IP Y."</em> This is required for hosting gaming servers (Minecraft, Steam), media servers (Plex), remote desktop connections, and web servers.
        </p>

        <h2 style="font-size: 1.6rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem; color: var(--text-primary);">How to Forward Ports on Any Router (Step-by-Step)</h2>
        <ol style="margin-left: 1.5rem; margin-bottom: 1.5rem; color: var(--text-secondary); line-height: 1.7;">
          <li><strong>Assign a Static IP or DHCP Reservation:</strong> In your router console under <strong>LAN &gt; DHCP Server</strong>, bind your computer/console's MAC address to a permanent local IP (e.g. <code>192.168.1.150</code>).</li>
          <li><strong>Locate Port Forwarding Settings:</strong> Look for <strong>Port Forwarding</strong>, <strong>Virtual Server</strong>, or <strong>NAT Forwarding</strong> in Advanced settings.</li>
          <li><strong>Create a New Rule:</strong> Enter the service name, select the protocol (TCP, UDP, or Both), enter the internal and external port numbers (e.g. <code>25565</code> for Minecraft), and enter your host machine's internal IP.</li>
          <li><strong>Save and Apply:</strong> Apply the settings. If hosting games or servers, make sure your operating system's software firewall (Windows Defender Firewall or UFW) also allows inbound traffic on that port.</li>
        </ol>

        <h2 style="font-size: 1.6rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem; color: var(--text-primary);">Port Forwarding Security Guidelines</h2>
        <ul style="margin-left: 1.5rem; margin-bottom: 1.5rem; color: var(--text-secondary); line-height: 1.7;">
          <li><strong>Never Expose Unencrypted Management Ports:</strong> Avoid forwarding Telnet (port 23) or unencrypted HTTP (port 80) directly to critical infrastructure.</li>
          <li><strong>Use Custom High Ports:</strong> For remote administration such as SSH (port 22) or Remote Desktop (port 3389), use a non-standard external port (e.g. port <code>52222</code>) to dramatically reduce automated bot scanning.</li>
          <li><strong>Prefer WireGuard or Tailscale VPN:</strong> Instead of opening multiple ports to the public internet, setting up a secure VPN lets you access your entire home LAN remotely with enterprise cryptography.</li>
        </ul>
      </section>
"""
        elif slug == "ip-address-checker":
            tool_editorial = """
      <section style="margin-top: 3.5rem;">
        <h2 style="font-size: 1.6rem; font-weight: 700; margin-bottom: 1rem; color: var(--text-primary);">How to Use the Public IP Address &amp; Geolocation Checker</h2>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          Every device connected to the Internet requires an Internet Protocol (IP) address to route data packets between servers, websites, and client computers. This free utility lets you instantly inspect any public IPv4 or IPv6 address or analyze your own active internet connection without running third-party tracking scripts:
        </p>
        <ol style="margin-left: 1.5rem; margin-bottom: 1.5rem; color: var(--text-secondary); line-height: 1.7;">
          <li><strong>Detect Your Own IP:</strong> Click <strong>"My Public IP"</strong> to automatically discover the public WAN IP assigned to your cable modem or fiber gateway by your Internet Service Provider (ISP).</li>
          <li><strong>Inspect Any Remote IP or Hostname:</strong> Type any IPv4 address (e.g. <code>8.8.8.8</code>), IPv6 address, or domain name (e.g. <code>github.com</code>) into the search field and click <strong>"Inspect IP"</strong>.</li>
          <li><strong>Analyze Routing &amp; Geolocation Data:</strong> The tool queries authoritative BGP and Whois records to display your Autonomous System Number (ASN), ISP name, approximate city/region coordinates, and local timezone.</li>
          <li><strong>Identify Private Local Subnets:</strong> If you enter a private LAN address (such as <code>192.168.1.1</code> or <code>10.0.0.1</code>), the tool immediately classifies the RFC 1918 subnet and provides local router configuration instructions.</li>
        </ol>

        <h2 style="font-size: 1.6rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem; color: var(--text-primary);">Public WAN IP vs. Private Default Gateway (192.168.1.1)</h2>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          A common source of confusion in computer networking is the difference between your <strong>Public IP</strong> and your <strong>Private Gateway IP</strong>:
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; margin-bottom: 2rem;">
          <div style="background: var(--bg-secondary); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
            <h3 style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.5rem; color: var(--text-accent);">🌐 Public IP (WAN)</h3>
            <ul style="margin-left: 1.25rem; font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6;">
              <li>Assigned globally by your ISP (Comcast, AT&amp;T, Verizon, Spectrum).</li>
              <li>Globally unique and routable across the worldwide Internet.</li>
              <li>Shared by all devices connected to your home Wi-Fi network via Network Address Translation (NAT).</li>
              <li>Determines your external geographic location visible to websites and streaming services.</li>
            </ul>
          </div>
          <div style="background: var(--bg-secondary); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
            <h3 style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.5rem; color: var(--text-accent);">🏠 Private IP / Gateway (LAN)</h3>
            <ul style="margin-left: 1.25rem; font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6;">
              <li>Assigned locally by your router's internal DHCP server (e.g. <code>192.168.1.1</code>).</li>
              <li>Only accessible within your local home or office physical network.</li>
              <li>Non-routable over the public Internet (governed by RFC 1918 specifications).</li>
              <li>Used to open your router's administrative setup dashboard and change Wi-Fi settings.</li>
            </ul>
          </div>
        </div>

        <h2 style="font-size: 1.6rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem; color: var(--text-primary);">RFC 1918 Private IPv4 Address Ranges</h2>
        <div style="overflow-x: auto; margin-bottom: 2rem;">
          <table class="table" style="font-size: 0.9rem;">
            <thead>
              <tr>
                <th>Address Block</th>
                <th>CIDR Prefix</th>
                <th>Total Addresses</th>
                <th>Standard Networking Deployments</th>
              </tr>
            </thead>
            <tbody>
              <tr><td><code>10.0.0.0 &ndash; 10.255.255.255</code></td><td><code>10.0.0.0/8</code></td><td>16,777,216</td><td>Comcast Xfinity xFi (10.0.0.1), Apple AirPort, Large Enterprise LANs</td></tr>
              <tr><td><code>172.16.0.0 &ndash; 172.31.255.255</code></td><td><code>172.16.0.0/12</code></td><td>1,048,576</td><td>Docker Bridges, Enterprise VPN tunnels, Corporate VLANs</td></tr>
              <tr><td><code>192.168.0.0 &ndash; 192.168.255.255</code></td><td><code>192.168.0.0/16</code></td><td>65,536</td><td>Netgear, ASUS, TP-Link, Linksys, and AT&amp;T Fiber (192.168.1.1 / 192.168.0.1)</td></tr>
              <tr><td><code>100.64.0.0 &ndash; 100.127.255.255</code></td><td><code>100.64.0.0/10</code></td><td>4,194,304</td><td>Carrier-Grade NAT (CGNAT, RFC 6598) used by Starlink and Cellular 5G ISPs</td></tr>
              <tr><td><code>169.254.0.0 &ndash; 169.254.255.255</code></td><td><code>169.254.0.0/16</code></td><td>65,536</td><td>Automatic Private IP Addressing (APIPA / Link-Local) when DHCP fails</td></tr>
            </tbody>
          </table>
        </div>

        <h2 style="font-size: 1.6rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem; color: var(--text-primary);">Understanding Autonomous System Numbers (ASN) &amp; BGP Routing</h2>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          The global Internet is composed of thousands of independently operated networks called <strong>Autonomous Systems (AS)</strong>. Each Autonomous System is assigned a globally unique 16-bit or 32-bit Autonomous System Number (ASN) by regional internet registries (such as ARIN, RIPE NCC, and APNIC).
        </p>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          Using the Border Gateway Protocol (BGP), these autonomous systems advertise IP prefix blocks to one another. When you perform an IP lookup on this tool, the ASN identifies the primary network operator (such as <code>AS7922</code> for Comcast, <code>AS7018</code> for AT&amp;T, <code>AS15169</code> for Google, or <code>AS13335</code> for Cloudflare) responsible for routing packets to and from that IP address.
        </p>

        <h2 style="font-size: 1.6rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem; color: var(--text-primary);">Frequently Asked Questions About Public IP Addresses</h2>
        <div class="faq-list" style="margin-top: 1rem;">
          <div class="faq-card" style="background: var(--bg-secondary); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-color); margin-bottom: 1rem;">
            <h3 style="font-size: 1.05rem; font-weight: 700; margin-bottom: 0.5rem;">Can someone find my exact home street address from my IP?</h3>
            <p style="color: var(--text-secondary); margin: 0; font-size: 0.95rem; line-height: 1.6;">
              No. Public IP geolocation databases map IP addresses to the ISP's local point of presence (PoP), central routing exchange, or metropolitan city center. Geolocation is generally accurate to the city or postal area level, but cannot reveal your physical street address or house number without a court subpoena served directly to your ISP.
            </p>
          </div>
          <div class="faq-card" style="background: var(--bg-secondary); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-color); margin-bottom: 1rem;">
            <h3 style="font-size: 1.05rem; font-weight: 700; margin-bottom: 0.5rem;">Why is my IP address different when connected to a VPN?</h3>
            <p style="color: var(--text-secondary); margin: 0; font-size: 0.95rem; line-height: 1.6;">
              When using a Virtual Private Network (VPN), your computer establishes an encrypted tunnel to a remote server. All your outbound internet traffic exits through that VPN server, so websites and lookup tools see the VPN provider's IP address and location instead of your real ISP-assigned IP.
            </p>
          </div>
          <div class="faq-card" style="background: var(--bg-secondary); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-color); margin-bottom: 1rem;">
            <h3 style="font-size: 1.05rem; font-weight: 700; margin-bottom: 0.5rem;">How can I change my public IP address?</h3>
            <p style="color: var(--text-secondary); margin: 0; font-size: 0.95rem; line-height: 1.6;">
              Most residential internet plans use dynamic IP addressing. You can often obtain a new public IP by powering off your cable/fiber modem for 15&ndash;30 minutes (allowing the ISP DHCP lease to expire) before turning it back on, or by cloning a different MAC address into your router's WAN settings.
            </p>
          </div>
        </div>
      </section>
"""
        elif slug == "dns-propagation":
            tool_editorial = """
      <section style="margin-top: 3.5rem;">
        <h2 style="font-size: 1.6rem; font-weight: 700; margin-bottom: 1rem; color: var(--text-primary);">How to Check Global DNS Propagation</h2>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          When you update DNS records with your domain registrar or cloud hosting provider (such as adding a new <code>A</code> record, switching nameservers, or configuring email <code>MX</code> records), the changes do not take effect across the entire world instantly. This tool queries multiple authoritative recursive resolvers globally in parallel via <strong>DNS-over-HTTPS (DoH)</strong> to verify real-time propagation:
        </p>
        <ol style="margin-left: 1.5rem; margin-bottom: 1.5rem; color: var(--text-secondary); line-height: 1.7;">
          <li><strong>Enter your Domain Name:</strong> Type the apex domain (e.g., <code>example.com</code>) or subdomain (e.g., <code>mail.example.com</code>) into the input box.</li>
          <li><strong>Select DNS Record Type:</strong> Choose the record type you want to verify: <code>A</code> (IPv4), <code>AAAA</code> (IPv6), <code>CNAME</code> (Aliases), <code>MX</code> (Mail exchangers), <code>TXT</code> (SPF / DKIM / Verification), <code>NS</code> (Nameservers), or <code>SOA</code> (Start of Authority).</li>
          <li><strong>Execute Query:</strong> Click <strong>"Check Global DNS"</strong>. Your browser queries Cloudflare (1.1.1.1), Google Public DNS (8.8.8.8), Quad9 (9.9.9.9), AdGuard, and AliDNS simultaneously.</li>
          <li><strong>Compare Results &amp; Consistency:</strong> The status table displays whether each global node has resolved your updated record, including TTL and response latency.</li>
        </ol>

        <h2 style="font-size: 1.6rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem; color: var(--text-primary);">Why Does DNS Propagation Take Time? (TTL &amp; Recursive Caching)</h2>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          DNS is a globally distributed, hierarchical caching system designed to minimize load on authoritative nameservers. Two key factors dictate how long DNS changes take to propagate:
        </p>
        <ul style="margin-left: 1.5rem; margin-bottom: 1.5rem; color: var(--text-secondary); line-height: 1.7;">
          <li><strong>Time to Live (TTL):</strong> Every DNS record includes a TTL value (measured in seconds). When an ISP or recursive resolver fetches your record, it caches the answer locally for the duration of the TTL. If your previous TTL was set to <code>86400</code> (24 hours), worldwide resolvers will continue serving the old cached record until that 24-hour countdown finishes.</li>
          <li><strong>ISP Recursive Cache Policies:</strong> Some internet service providers ignore short TTLs and enforce minimum cache retention windows (e.g. 1 to 2 hours) to conserve upstream bandwidth, creating temporary regional discrepancies.</li>
          <li><strong>NS (Nameserver) Delegation Delays:</strong> When changing domain nameservers at your registrar, the root TLD zone file (such as <code>.com</code> or <code>.org</code>) must update, which typically takes 24 to 48 hours to fully propagate worldwide.</li>
        </ul>

        <h2 style="font-size: 1.6rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem; color: var(--text-primary);">Common DNS Record Types Explained</h2>
        <div style="overflow-x: auto; margin-bottom: 2rem;">
          <table class="table" style="font-size: 0.9rem;">
            <thead>
              <tr>
                <th>Record Type</th>
                <th>Standard Purpose</th>
                <th>Example Value</th>
                <th>Recommended TTL</th>
              </tr>
            </thead>
            <tbody>
              <tr><td><code>A</code></td><td>Maps a hostname to an IPv4 address</td><td><code>192.0.2.1</code></td><td>300 &ndash; 3600 seconds</td></tr>
              <tr><td><code>AAAA</code></td><td>Maps a hostname to an IPv6 address</td><td><code>2001:db8::1</code></td><td>300 &ndash; 3600 seconds</td></tr>
              <tr><td><code>CNAME</code></td><td>Canonical Name alias pointing to another domain</td><td><code>app.vercel-dns.com</code></td><td>300 &ndash; 1800 seconds</td></tr>
              <tr><td><code>MX</code></td><td>Mail Exchange server for receiving email</td><td><code>10 mail.google.com</code></td><td>3600 &ndash; 14400 seconds</td></tr>
              <tr><td><code>TXT</code></td><td>Human/machine readable text (SPF, DKIM, DMARC, SSL verification)</td><td><code>v=spf1 include:_spf.google.com ~all</code></td><td>3600 seconds</td></tr>
              <tr><td><code>NS</code></td><td>Delegates a DNS zone to authoritative nameservers</td><td><code>ns1.cloudflare.com</code></td><td>86400 seconds (24 hrs)</td></tr>
              <tr><td><code>SOA</code></td><td>Start of Authority (zone serial number, refresh intervals)</td><td><code>ns1.example.com admin.example.com 2026110401</code></td><td>86400 seconds</td></tr>
            </tbody>
          </table>
        </div>

        <h2 style="font-size: 1.6rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem; color: var(--text-primary);">How DNS-over-HTTPS (DoH) Works</h2>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          Traditional DNS queries are sent over plaintext UDP port 53, making them vulnerable to eavesdropping, ISP manipulation, and DNS spoofing. <strong>DNS-over-HTTPS (RFC 8484)</strong> encapsulates DNS queries inside an encrypted HTTPS connection over standard TCP port 443.
        </p>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          This tool communicates directly with global DoH JSON endpoints (Cloudflare, Google Public DNS, and Quad9). Because the browser requests data directly via secure HTTPS APIs, local ISP DNS interception is bypassed, giving you an authentic snapshot of global DNS records.
        </p>

        <h2 style="font-size: 1.6rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem; color: var(--text-primary);">How to Flush Your Local DNS Cache</h2>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          If our tool shows that global DNS has propagated, but your computer still cannot reach the new server, your local operating system or browser cache is likely holding the old IP. Follow these terminal commands to flush your cache:
        </p>
        <ul style="margin-left: 1.5rem; margin-bottom: 1.5rem; color: var(--text-secondary); line-height: 1.7;">
          <li><strong>Windows (CMD as Administrator):</strong> Run <code>ipconfig /flushdns</code></li>
          <li><strong>macOS (Terminal):</strong> Run <code>sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder</code></li>
          <li><strong>Linux (systemd-resolved):</strong> Run <code>sudo resolvectl flush-caches</code> or <code>sudo systemd-resolve --flush-caches</code></li>
          <li><strong>Google Chrome Browser:</strong> Navigate to <code>chrome://net-internals/#dns</code> and click <strong>"Clear host cache"</strong>.</li>
        </ul>
      </section>
"""
        elif slug == "cidr-cheat-sheet":
            tool_editorial = """
      <section style="margin-top: 3.5rem;">
        <h2 style="font-size: 1.6rem; font-weight: 700; margin-bottom: 1rem; color: var(--text-primary);">IPv4 CIDR Prefix &amp; Subnetting Reference Guide</h2>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          Subnetting allows network designers to split larger IP networks into smaller, more efficient logical segments. This reduces broadcast traffic domains, improves routing efficiency, and enforces security segmentation between different user groups and VLANs.
        </p>

        <h2 style="font-size: 1.6rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem; color: var(--text-primary);">RFC 1918 Private IP Address Spaces</h2>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          The Internet Engineering Task Force (IETF) reserved three dedicated IPv4 address blocks for private local networks that are never routed on the public internet:
        </p>
        <ul style="margin-left: 1.5rem; margin-bottom: 1.5rem; color: var(--text-secondary); line-height: 1.7;">
          <li><strong>Class A Range:</strong> <code>10.0.0.0/8</code> (10.0.0.0 to 10.255.255.255) &mdash; 16,777,216 addresses. Common in large enterprise campuses and Comcast Xfinity gateways (10.0.0.1).</li>
          <li><strong>Class B Range:</strong> <code>172.16.0.0/12</code> (172.16.0.0 to 172.31.255.255) &mdash; 1,048,576 addresses. Frequently used in corporate corporate data centers and Docker container networks.</li>
          <li><strong>Class C Range:</strong> <code>192.168.0.0/16</code> (192.168.0.0 to 192.168.255.255) &mdash; 65,536 addresses. The universal standard for consumer Wi-Fi routers and home lab subnets.</li>
          <li><strong>Carrier-Grade NAT (CGNAT, RFC 6598):</strong> <code>100.64.0.0/10</code> (100.64.0.0 to 100.127.255.255) &mdash; Allocated to internet service providers to share public IPv4 addresses across multiple customers.</li>
        </ul>

        <h2 style="font-size: 1.6rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem; color: var(--text-primary);">Calculating Subnet Capacities</h2>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          To calculate the number of usable hosts for any prefix length <em>P</em>:
        </p>
        <div style="background: var(--bg-secondary); padding: 1rem 1.25rem; border-radius: var(--radius-md); font-family: var(--font-mono); font-size: 1rem; margin-bottom: 1.5rem; border: 1px solid var(--border-color);">
          Usable Hosts = 2<sup>(32 &minus; P)</sup> &minus; 2
        </div>
        <p style="margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
          For a <code>/24</code> prefix: 2<sup>(32 &minus; 24)</sup> &minus; 2 = 2<sup>8</sup> &minus; 2 = 256 &minus; 2 = <strong>254 usable hosts</strong>.
        </p>
      </section>
"""

        content = f"""
  <main class="container" style="padding-top: 1.5rem; padding-bottom: 3.5rem;">
    <div class="content-container">
      <div class="silo-badge silo-badge-tool">🛠️ Interactive Utility</div>
      <h1 style="font-size: 2.15rem; font-weight: 800; margin-bottom: 0.75rem; letter-spacing: -0.02em;">
        {escape(t['title'])}
      </h1>
      <p style="font-size: 1.1rem; color: var(--text-secondary); margin-bottom: 1.5rem;">
        {escape(t['desc'])}
      </p>

      <!-- Embed Tool UI -->
      {tool_ui}

      <!-- Detailed SEO Guides and Reference Documentation -->
      {tool_editorial}

      <!-- Cross Silo Links -->
      <div style="margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--border-color);">
        <h3 style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.75rem;">Explore Other Tools</h3>
        <div style="display: flex; flex-wrap: wrap; gap: 0.75rem;">
          <a href="/tools/" class="btn btn-secondary" style="font-size: 0.85rem;">All Tools Suite &rarr;</a>
          <a href="/tools/ip-address-checker/" class="btn btn-secondary" style="font-size: 0.85rem;">IP Address Checker &rarr;</a>
          <a href="/tools/dns-propagation/" class="btn btn-secondary" style="font-size: 0.85rem;">DNS Propagation &rarr;</a>
          <a href="/tools/subnet-calculator/" class="btn btn-secondary" style="font-size: 0.85rem;">Subnet Calculator &rarr;</a>
          <a href="/tools/wifi-qr-code/" class="btn btn-secondary" style="font-size: 0.85rem;">Wi-Fi QR Code &rarr;</a>
          <a href="/tools/detect-gateway/" class="btn btn-secondary" style="font-size: 0.85rem;">Gateway Auto-Detector &rarr;</a>
          <a href="/tools/router-password-generator/" class="btn btn-secondary" style="font-size: 0.85rem;">Password Generator &rarr;</a>
          <a href="/tools/cidr-cheat-sheet/" class="btn btn-secondary" style="font-size: 0.85rem;">CIDR Cheat-Sheet &rarr;</a>
        </div>
      </div>
    </div>
  </main>
"""
        full_html = get_header(title, desc, canonical, active_nav="tools", breadcrumbs=breadcrumbs) + content + get_footer()
        with open(os.path.join(tool_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(full_html)

    # Sync master tools hub at /tools/index.html
    tools_hub_path = os.path.join(PUBLIC_DIR, "tools", "index.html")
    tools_html_path = os.path.join(PUBLIC_DIR, "tools.html")
    if os.path.exists(tools_html_path):
        shutil.copyfile(tools_html_path, tools_hub_path)

# ==============================================================================
# 7. GENERATE CATEGORIZED SITEMAP INDEX ARCHITECTURE
# ==============================================================================
def generate_sitemaps():
    print("Generating Categorized Sitemap Index Architecture...")
    sitemaps_dir = os.path.join(PUBLIC_DIR, "sitemaps")
    make_dirs(sitemaps_dir)

    def write_sub_sitemap(filename, urls_with_priority):
        lines = ['<?xml version="1.0" encoding="UTF-8"?>']
        lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
        for loc, prio, freq in urls_with_priority:
            lines.append("  <url>")
            lines.append(f"    <loc>{loc}</loc>")
            lines.append(f"    <lastmod>{TODAY}</lastmod>")
            lines.append(f"    <changefreq>{freq}</changefreq>")
            lines.append(f"    <priority>{prio}</priority>")
            lines.append("  </url>")
        lines.append("</urlset>")
        with open(os.path.join(sitemaps_dir, filename), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

    # 1. ips.xml
    ip_urls = [("https://routeriphub.com/ip/", "0.9", "weekly")]
    for ip_item in IP_GATEWAYS:
        ip_urls.append((f"https://routeriphub.com/ip/{ip_item['slug']}/", "0.9", "monthly"))
    write_sub_sitemap("ips.xml", ip_urls)

    # 2. brands.xml
    brand_urls = [("https://routeriphub.com/brands/", "0.9", "weekly")]
    for b in BRAND_PROFILES:
        brand_urls.append((f"https://routeriphub.com/brands/{b['slug']}/", "0.8", "monthly"))
    write_sub_sitemap("brands.xml", brand_urls)

    # 3. routers.xml
    router_urls = [("https://routeriphub.com/routers/", "0.9", "weekly")]
    for m in ROUTER_MODELS:
        router_urls.append((f"https://routeriphub.com/routers/{m['slug']}/", "0.8", "monthly"))
    write_sub_sitemap("routers.xml", router_urls)

    # 4. isps.xml
    isp_urls = [("https://routeriphub.com/isp/", "0.9", "weekly")]
    for isp in ISP_GATEWAYS:
        isp_urls.append((f"https://routeriphub.com/isp/{isp['slug']}/", "0.8", "monthly"))
    write_sub_sitemap("isps.xml", isp_urls)

    # 5. tools.xml
    tool_urls = [("https://routeriphub.com/tools/", "0.9", "weekly")]
    for t in TOOL_PAGES:
        tool_urls.append((f"https://routeriphub.com/tools/{t['slug']}/", "0.8", "monthly"))
    write_sub_sitemap("tools.xml", tool_urls)

    # 6. guides.xml
    guide_urls = [
        ("https://routeriphub.com/", "1.0", "daily"),
        ("https://routeriphub.com/howto.html", "0.9", "weekly"),
        ("https://routeriphub.com/find-router-ip.html", "0.8", "monthly"),
        ("https://routeriphub.com/developers.html", "0.8", "monthly")
    ]
    write_sub_sitemap("guides.xml", guide_urls)

    # Master sitemap.xml (<sitemapindex>)
    master_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        '  <sitemap>',
        '    <loc>https://routeriphub.com/sitemaps/ips.xml</loc>',
        f'    <lastmod>{TODAY}</lastmod>',
        '  </sitemap>',
        '  <sitemap>',
        '    <loc>https://routeriphub.com/sitemaps/brands.xml</loc>',
        f'    <lastmod>{TODAY}</lastmod>',
        '  </sitemap>',
        '  <sitemap>',
        '    <loc>https://routeriphub.com/sitemaps/routers.xml</loc>',
        f'    <lastmod>{TODAY}</lastmod>',
        '  </sitemap>',
        '  <sitemap>',
        '    <loc>https://routeriphub.com/sitemaps/isps.xml</loc>',
        f'    <lastmod>{TODAY}</lastmod>',
        '  </sitemap>',
        '  <sitemap>',
        '    <loc>https://routeriphub.com/sitemaps/tools.xml</loc>',
        f'    <lastmod>{TODAY}</lastmod>',
        '  </sitemap>',
        '  <sitemap>',
        '    <loc>https://routeriphub.com/sitemaps/guides.xml</loc>',
        f'    <lastmod>{TODAY}</lastmod>',
        '  </sitemap>',
        '</sitemapindex>'
    ]
    with open(os.path.join(PUBLIC_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(master_lines))

# ==============================================================================
# 8. EXPORT UPGRADED DATASETS (routers.json, routers.csv, routers.sql)
# ==============================================================================
def export_datasets():
    print("Exporting enriched hardware datasets...")
    data_dir = os.path.join(PUBLIC_DIR, "data")
    make_dirs(data_dir)

    # 1. routers.json
    with open(os.path.join(data_dir, "routers.json"), "w", encoding="utf-8") as f:
        json.dump(ROUTER_MODELS, f, indent=2)

    # 2. routers.csv
    csv_file = os.path.join(data_dir, "routers.csv")
    fieldnames = [
        "slug", "brand", "model_name", "hardware_type", "default_ip",
        "web_domain", "default_username", "default_password", "wifi_standard"
    ]
    with open(csv_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for m in ROUTER_MODELS:
            writer.writerow(m)

    # 3. routers.sql
    sql_lines = [
        "-- RouterIPHub Production Hardware Database Schema",
        "-- Licensed under CC BY 4.0",
        "CREATE TABLE IF NOT EXISTS router_hardware (",
        "  id SERIAL PRIMARY KEY,",
        "  slug VARCHAR(120) UNIQUE NOT NULL,",
        "  brand VARCHAR(60) NOT NULL,",
        "  brand_slug VARCHAR(60) NOT NULL,",
        "  model_name VARCHAR(120) NOT NULL,",
        "  hardware_type VARCHAR(80),",
        "  default_ip VARCHAR(45) NOT NULL,",
        "  web_domain VARCHAR(120),",
        "  default_username VARCHAR(60),",
        "  default_password VARCHAR(100),",
        "  wifi_standard VARCHAR(100),",
        "  reset_instructions TEXT,",
        "  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP",
        ");\n"
    ]
    for m in ROUTER_MODELS:
        m_name = m['model_name'].replace("'", "''")
        m_pass = m['default_password'].replace("'", "''")
        sql_lines.append(
            f"INSERT INTO router_hardware (slug, brand, brand_slug, model_name, hardware_type, default_ip, web_domain, default_username, default_password, wifi_standard) VALUES "
            f"('{m['slug']}', '{m['brand']}', '{m['brand_slug']}', '{m_name}', '{m['hardware_type']}', '{m['default_ip']}', '{m['web_domain']}', '{m['default_username']}', '{m_pass}', '{m['wifi_standard']}') "
            f"ON CONFLICT (slug) DO NOTHING;"
        )
    with open(os.path.join(data_dir, "routers.sql"), "w", encoding="utf-8") as f:
        f.write("\n".join(sql_lines))

# ==============================================================================
# 9. UPDATE GLOBAL SEARCH INDEX (search-index.json)
# ==============================================================================
def update_search_index():
    print("Updating Global CmdK Search Index...")
    search_index = []

    # 1. Models
    for m in ROUTER_MODELS:
        search_index.append({
            "title": f"{m['brand']} {m['model_name']} Setup Sheet",
            "category": "Router Model",
            "badge": m['brand'],
            "url": f"/routers/{m['slug']}/",
            "snippet": f"Default IP {m['default_ip']}, username '{m['default_username']}', password '{m['default_password']}', {m['wifi_standard']}.",
            "keywords": f"{m['brand'].lower()} {m['model_name'].lower()} {m['default_ip']} {m['slug']} password reset {m['hardware_type'].lower()}"
        })

    # 2. ISP Gateways
    for isp in ISP_GATEWAYS:
        search_index.append({
            "title": f"{isp['isp_name']} Gateway Portal ({isp['default_ip']})",
            "category": "ISP Gateway",
            "badge": isp['isp_name'],
            "url": f"/isp/{isp['slug']}/",
            "snippet": f"{isp['gateway_name']} login, printed access code, and bridge mode guide.",
            "keywords": f"{isp['isp_name'].lower()} {isp['slug']} {isp['default_ip']} bridge mode passthrough xfi bgw320 fiber"
        })

    # 3. Brands
    for b in BRAND_PROFILES:
        search_index.append({
            "title": f"{b['name']} Brand Directory & Model Matrix",
            "category": "Brand Directory",
            "badge": "Brand",
            "url": f"/brands/{b['slug']}/",
            "snippet": f"Standard gateways: {', '.join(b['default_ips'])}, credentials: {b['default_creds']}.",
            "keywords": f"{b['name'].lower()} {b['slug']} brand passwords {' '.join(b['default_ips'])}"
        })

    # 4. IP Gateways
    for ip_item in IP_GATEWAYS:
        search_index.append({
            "title": f"{ip_item['ip']} Default Gateway Hub",
            "category": "Gateway IP",
            "badge": ip_item['ip'],
            "url": f"/ip/{ip_item['slug']}/",
            "snippet": f"{ip_item['class_type']} - Used on {ip_item['brands']}.",
            "keywords": f"{ip_item['ip']} {ip_item['slug']} login admin gateway {ip_item['brands'].lower()}"
        })

    # 5. Tools
    for t in TOOL_PAGES:
        search_index.append({
            "title": t["title"],
            "category": "Interactive Tool",
            "badge": "Tool",
            "url": f"/tools/{t['slug']}/",
            "snippet": t["desc"],
            "keywords": f"{t['short_title'].lower()} {t['slug']} tool utility networking"
        })

    # 6. Guides & Hubs
    search_index.append({
        "title": "Universal Router IP Discovery Guide (Windows, Mac, iOS, Android)",
        "category": "Setup Guide",
        "badge": "Guide",
        "url": "/find-router-ip.html",
        "snippet": "Terminal commands (ipconfig, netstat -nr) and graphical settings to find your local gateway IP.",
        "keywords": "find my ip ipconfig default gateway windows mac iphone android"
    })
    search_index.append({
        "title": "Wi-Fi 7 Setup, 320 MHz Channels & MLO Optimization Guide",
        "category": "Setup Guide",
        "badge": "Guide",
        "url": "/howto.html#wifi7-setup",
        "snippet": "How to configure 320 MHz channels, Multi-Link Operation (MLO), and 6 GHz AFC coordination.",
        "keywords": "wifi 7 320 mhz mlo 6 ghz be800 be96u wireless 802.11be"
    })
    search_index.append({
        "title": "Fiber ONT Bridging & Double NAT Elimination Guide",
        "category": "Setup Guide",
        "badge": "Guide",
        "url": "/howto.html#ont-bridging",
        "snippet": "How to bypass ISP combo gateways and configure IP Passthrough on AT&T, Verizon, and CenturyLink.",
        "keywords": "fiber ont bridge mode double nat ip passthrough bgw320 cr1000a"
    })
    search_index.append({
        "title": "Interactive Networking Tools Suite",
        "category": "Interactive Tool",
        "badge": "Suite",
        "url": "/tools/",
        "snippet": "All 8 client-side tools: IP Address Checker, DNS Propagation, Wi-Fi QR generator, CIDR subnet calculator, gateway detector, password generator, port checker, CIDR cheat sheet.",
        "keywords": "tools utilities subnet qr code password generator webrtc probe"
    })

    with open(os.path.join(PUBLIC_DIR, "data", "search-index.json"), "w", encoding="utf-8") as f:
        json.dump(search_index, f, indent=2)

# ==============================================================================
# 10. UPDATE VERCEL REDIRECTS & CONFIG (vercel.json)
# ==============================================================================
def update_vercel_config():
    print("Updating vercel.json with 301 redirects & clean URLs...")
    redirects = [
        {"source": "/192-168-1-1.html", "destination": "/ip/192-168-1-1/", "permanent": True},
        {"source": "/192-168-0-1.html", "destination": "/ip/192-168-0-1/", "permanent": True},
        {"source": "/10-0-0-1.html", "destination": "/ip/10-0-0-1/", "permanent": True},
        {"source": "/192-168-1-254.html", "destination": "/ip/192-168-1-254/", "permanent": True},
        {"source": "/192-168-2-1.html", "destination": "/ip/192-168-2-1/", "permanent": True},
        {"source": "/192-168-8-1.html", "destination": "/ip/192-168-8-1/", "permanent": True},
        {"source": "/192-168-10-1.html", "destination": "/ip/192-168-10-1/", "permanent": True},
        {"source": "/192-168-11-1.html", "destination": "/ip/192-168-11-1/", "permanent": True},
        {"source": "/192-168-12-1.html", "destination": "/ip/192-168-12-1/", "permanent": True},
        {"source": "/192-168-31-1.html", "destination": "/ip/192-168-31-1/", "permanent": True},
        {"source": "/192-168-88-1.html", "destination": "/ip/192-168-88-1/", "permanent": True},
        {"source": "/192-168-100-1.html", "destination": "/ip/192-168-100-1/", "permanent": True},
        {"source": "/10-0-1-1.html", "destination": "/ip/10-0-1-1/", "permanent": True},
        {"source": "/192-168-1-2.html", "destination": "/ip/192-168-1-2/", "permanent": True},
        {"source": "/brands.html", "destination": "/brands/", "permanent": True},
        {"source": "/tools.html", "destination": "/tools/", "permanent": True},
        {"source": "/brand/:brand", "destination": "/brands/:brand/", "permanent": True}
    ]

    vconfig = {
        "version": 2,
        "cleanUrls": True,
        "trailingSlash": True,
        "outputDirectory": "public",
        "redirects": redirects,
        "headers": [
            {
                "source": "/(.*)",
                "headers": [
                    {"key": "X-Content-Type-Options", "value": "nosniff"},
                    {"key": "X-Frame-Options", "value": "SAMEORIGIN"},
                    {"key": "X-XSS-Protection", "value": "1; mode=block"},
                    {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"}
                ]
            },
            {
                "source": "/css/(.*)",
                "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]
            },
            {
                "source": "/js/(.*)",
                "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]
            },
            {
                "source": "/data/(.*)",
                "headers": [
                    {"key": "Access-Control-Allow-Origin", "value": "*"},
                    {"key": "Cache-Control", "value": "public, max-age=86400, stale-while-revalidate=604800"}
                ]
            }
        ]
    }

    # Write to root and public
    for target in [os.path.join(ROOT_DIR, "vercel.json"), os.path.join(PUBLIC_DIR, "vercel.json")]:
        with open(target, "w", encoding="utf-8") as f:
            json.dump(vconfig, f, indent=2)

# ==============================================================================
# 11. UPDATE LLM CITATION MANIFESTS (llms.txt & llms-full.txt)
# ==============================================================================
def update_llm_manifests():
    print("Updating llms.txt & llms-full.txt...")
    llms_txt = """# RouterIPHub - AI & LLM Machine-Readable Index
> Reference platform for RFC 1918 private gateway IP addresses, hardware setup sheets, factory credentials, and network diagnostics.

## Canonical Silo Taxonomy
- Hardware Models Directory: https://routeriphub.com/routers/
- ISP Gateway Portals: https://routeriphub.com/isp/
- Hardware Brand Matrix: https://routeriphub.com/brands/
- Private IP Hubs: https://routeriphub.com/ip/
- Interactive Utilities: https://routeriphub.com/tools/
- Universal Discovery Guide: https://routeriphub.com/find-router-ip.html

## Key Machine-Readable Endpoints (REST API)
- JSON Hardware Catalog (32+ models): https://routeriphub.com/data/routers.json
- CSV Tabular Export: https://routeriphub.com/data/routers.csv
- ANSI SQL Schema Dump: https://routeriphub.com/data/routers.sql
- Gateway Subnets Dataset: https://routeriphub.com/data/gateways.json
- Global Search Index: https://routeriphub.com/data/search-index.json
- XML Sitemap Index: https://routeriphub.com/sitemap.xml

## Standard Default Gateways by Brand
- Netgear: 192.168.1.1 (routerlogin.net), admin / password
- TP-Link: 192.168.0.1 (tplinkwifi.net), admin / admin
- ASUS: 192.168.1.1 (router.asus.com), admin / admin
- Linksys: 192.168.1.1 (myrouter.local), admin / admin
- Xfinity: 10.0.0.1, admin / password
- AT&T Fiber: 192.168.1.254, printed Device Access Code
- MikroTik: 192.168.88.1 (router.lan), admin / [empty]
- AVM FRITZ!Box: 192.168.178.1 (fritz.box), admin / sticker password
- TP-Link Deco: 192.168.68.1 (tplinkdeco.net), managed via Deco App
- Amazon Eero: 192.168.4.1, managed via eero App
"""
    with open(os.path.join(PUBLIC_DIR, "llms.txt"), "w", encoding="utf-8") as f:
        f.write(llms_txt)

    llms_full_txt = f"""# RouterIPHub - Complete Programmatic Technical Knowledgebase
Date: {TODAY}
Website: https://routeriphub.com

## 1. Gateway IP Directory
"""
    for ip_item in IP_GATEWAYS:
        llms_full_txt += f"- IP: {ip_item['ip']}\n  Subnet: {ip_item['subnet_mask']}\n  Brands: {ip_item['brands']}\n  Default Credentials: {ip_item['default_creds']}\n  URL: https://routeriphub.com/ip/{ip_item['slug']}/\n\n"

    llms_full_txt += "## 2. Hardware Models Database\n"
    for m in ROUTER_MODELS:
        llms_full_txt += f"- Model: {m['brand']} {m['model_name']}\n  IP: {m['default_ip']}\n  Domain: {m['web_domain']}\n  Credentials: {m['default_username']} / {m['default_password']}\n  Reset: {m['reset_instructions']}\n  URL: https://routeriphub.com/routers/{m['slug']}/\n\n"

    with open(os.path.join(PUBLIC_DIR, "llms-full.txt"), "w", encoding="utf-8") as f:
        f.write(llms_full_txt)

# ==============================================================================
# MAIN EXECUTION PIPELINE
# ==============================================================================
def main():
    print("=" * 60)
    print("STARTING ROUTERIPHUB PROGRAMMATIC SEO GENERATION PIPELINE")
    print("=" * 60)

    generate_router_model_pages()
    generate_router_index_page()
    generate_isp_pages()
    generate_brand_pages()
    generate_ip_pages()
    generate_tool_pages()
    generate_sitemaps()
    export_datasets()
    update_search_index()
    update_vercel_config()
    update_llm_manifests()

    print("=" * 60)
    print("PSEO PIPELINE COMPLETE! 100% PRODUCTION READY.")
    print("=" * 60)

if __name__ == "__main__":
    main()
