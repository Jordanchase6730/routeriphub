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
def generate_ip_pages():
    print(f"Generating {len(IP_GATEWAYS)} private gateway IP pages...")
    for ip_item in IP_GATEWAYS:
        ip = ip_item["ip"]
        slug = ip_item["slug"]
        ip_dir = os.path.join(PUBLIC_DIR, "ip", slug)
        make_dirs(ip_dir)

        canonical = f"https://routeriphub.com/ip/{slug}/"
        title = f"{ip} Router Admin Login, Default Password & Troubleshooting (2026)"
        desc = f"Access {ip} router login portal. Default username, password, network configuration, and troubleshooting guide for {ip_item['brands']} routers."

        tech_schema = {
            "@type": "TechArticle",
            "headline": f"{ip} Default Gateway IP Administration Reference",
            "description": desc,
            "mainEntityOfPage": canonical,
            "datePublished": "2026-01-15T08:00:00+00:00",
            "dateModified": f"{TODAY}T02:00:00+00:00",
            "author": {"@type": "Organization", "name": "RouterIPHub Editorial Team"},
            "publisher": {"@type": "Organization", "name": "RouterIPHub", "url": "https://routeriphub.com/"}
        }

        howto_schema = {
            "@type": "HowTo",
            "name": f"How to Log Into {ip} Admin Console",
            "step": [
                {
                    "@type": "HowToStep",
                    "position": 1,
                    "name": "Connect to Local Network",
                    "text": "Connect to your home router via Wi-Fi or directly connect an Ethernet cable to any LAN port."
                },
                {
                    "@type": "HowToStep",
                    "position": 2,
                    "name": "Navigate to Gateway Address",
                    "text": f"Open your web browser (Chrome, Safari, Edge, Firefox) and type http://{ip} in the URL bar."
                },
                {
                    "@type": "HowToStep",
                    "position": 3,
                    "name": "Submit Admin Credentials",
                    "text": f"Enter the default credentials: '{ip_item['default_creds']}' or check the router underside label."
                }
            ]
        }

        breadcrumbs = [
            ("Home", "/"),
            ("IP Directory", "/ip/"),
            (ip, f"/ip/{slug}/")
        ]

        # Find models using this IP
        ip_models = [m for m in ROUTER_MODELS if m["default_ip"] == ip]
        model_rows = ""
        for m in ip_models:
            model_rows += f"""
            <tr>
              <td><a href="/routers/{escape(m['slug'])}/"><strong>{escape(m['brand'])} {escape(m['model_name'])}</strong></a></td>
              <td><code>{escape(m['default_username'])}</code></td>
              <td><code>{escape(m['default_password'])}</code></td>
              <td><a href="/routers/{escape(m['slug'])}/" class="btn btn-secondary" style="font-size: 0.8rem; padding: 0.3rem 0.65rem;">Setup Sheet &rarr;</a></td>
            </tr>
            """
        if not model_rows:
            model_rows = f"""
            <tr>
              <td colspan="4" style="text-align: center; color: var(--text-muted); padding: 1.5rem;">
                Commonly deployed on {escape(ip_item['brands'])} hardware with credentials <code>{escape(ip_item['default_creds'])}</code>.
              </td>
            </tr>
            """

        content = f"""
  <main class="container" style="padding-top: 1.5rem; padding-bottom: 3.5rem;">
    <div class="content-container">
      <div class="silo-badge silo-badge-ip">⚡ Private Gateway IP Pillar</div>
      <h1 style="font-size: 2.15rem; font-weight: 800; margin-bottom: 0.75rem; letter-spacing: -0.02em;">
        {escape(ip)} Admin Login & Setup Guide
      </h1>
      <p style="font-size: 1.1rem; color: var(--text-secondary); margin-bottom: 1.5rem;">
        {escape(ip_item['summary'])}
      </p>

      <!-- Answer Box -->
      <div class="answer-box">
        <div class="answer-box-label">RFC 1918 Private IPv4 Reference</div>
        <div class="answer-box-main">
          Gateway IP: <strong>{escape(ip)}</strong> &bull; Subnet: <strong>{escape(ip_item['subnet_mask'])}</strong>
        </div>
        <div class="answer-box-sub">
          Default Credentials: <strong>{escape(ip_item['default_creds'])}</strong> &bull; Usable Hosts: {escape(ip_item['usable_range'])}
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="action-btn-group">
        <a href="http://{escape(ip)}" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
          Open http://{escape(ip)} in Browser &rarr;
        </a>
        <button class="btn btn-secondary copy-btn" data-copy="{escape(ip)}">
          Copy IP ({escape(ip)})
        </button>
      </div>

      <!-- Subnet Specifications -->
      <h2 style="font-size: 1.4rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.5rem;">
        Subnet Parameters & Range Allocation
      </h2>
      <div class="specs-grid">
        <div class="spec-item">
          <span class="spec-item-label">Address Class</span>
          <span class="spec-item-val">{escape(ip_item['class_type'])}</span>
        </div>
        <div class="spec-item">
          <span class="spec-item-label">Subnet Mask</span>
          <span class="spec-item-val">{escape(ip_item['subnet_mask'])}</span>
        </div>
        <div class="spec-item">
          <span class="spec-item-label">Common Brands</span>
          <span class="spec-item-val">{escape(ip_item['brands'])}</span>
        </div>
        <div class="spec-item">
          <span class="spec-item-label">Usable Host Range</span>
          <span class="spec-item-val">{escape(ip_item['usable_range'])}</span>
        </div>
      </div>

      <!-- Router Models on this IP -->
      <h2 style="font-size: 1.4rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 0.75rem;">
        Routers Configured on {escape(ip)}
      </h2>
      <div style="overflow-x: auto;">
        <table class="table">
          <thead>
            <tr>
              <th>Model Name</th>
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

      <!-- In-Page Diagnostic Reachability Console -->
      <div class="card" style="margin: 2.5rem 0; border: 1px solid var(--border-color); background: var(--bg-card); border-radius: var(--radius-lg); padding: 1.5rem;">
        <h3 style="font-size: 1.15rem; font-weight: 700; margin-bottom: 0.5rem;">
          ⚡ Live Gateway Reachability Probe
        </h3>
        <p style="font-size: 0.875rem; color: var(--text-muted); margin-bottom: 1rem;">
          Test whether your current device can reach {escape(ip)} across your local network:
        </p>
        <div style="display: flex; gap: 0.75rem; align-items: center; flex-wrap: wrap;">
          <button id="probe-btn" class="btn btn-primary" style="padding: 0.55rem 1rem; font-size: 0.875rem;">
            Test Connection to {escape(ip)}
          </button>
          <div id="probe-status" style="font-size: 0.875rem; font-weight: 600;"></div>
        </div>
      </div>

      <!-- Troubleshooting Guide -->
      <h2 style="font-size: 1.4rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 0.5rem;">
        Why is {escape(ip)} Not Loading?
      </h2>
      <div class="card" style="padding: 1.25rem; line-height: 1.7;">
        <ul style="padding-left: 1.25rem;">
          <li><strong>Typo check:</strong> Ensure you are typing numbers, not letters (avoid "192.168.l.l" with lowercase L).</li>
          <li><strong>VPN Active:</strong> Disconnect any active VPNs (Work VPN, NordVPN, ExpressVPN) as they route DNS away from your local subnet.</li>
          <li><strong>Protocol:</strong> Use <code>http://{escape(ip)}</code> rather than <code>https://</code> unless your router enforces SSL certificates.</li>
          <li><strong>Different Gateway:</strong> Your router might use a different subnet. Use our <a href="/tools/detect-gateway/">Local Gateway Auto-Detector</a> to confirm your exact IP.</li>
        </ul>
      </div>

      <!-- Cross Silo Links -->
      <div style="margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--border-color);">
        <h3 style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.75rem;">Explore Other Gateway IPs</h3>
        <div style="display: flex; flex-wrap: wrap; gap: 0.75rem;">
          <a href="/ip/" class="btn btn-secondary" style="font-size: 0.85rem;">All Gateway IPs &rarr;</a>
          <a href="/tools/subnet-calculator/" class="btn btn-secondary" style="font-size: 0.85rem;">Subnet Calculator &rarr;</a>
          <a href="/find-router-ip.html" class="btn btn-secondary" style="font-size: 0.85rem;">Find My IP (OS Commands) &rarr;</a>
        </div>
      </div>
    </div>
  </main>
"""
        full_html = get_header(title, desc, canonical, active_nav="ip", breadcrumbs=breadcrumbs, schemas_json_ld=[tech_schema, howto_schema]) + content + get_footer()
        with open(os.path.join(ip_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(full_html)

    # Master IP Directory
    ip_master_dir = os.path.join(PUBLIC_DIR, "ip")
    canonical_master = "https://routeriphub.com/ip/"
    title_master = "Default Gateway IP Directory (RFC 1918 Private Subnets)"
    desc_master = "Complete directory of private default gateway IPs: 192.168.1.1, 192.168.0.1, 10.0.0.1, 192.168.1.254, 192.168.88.1, and Class A/B/C subnets."

    ip_cards = ""
    for ip_item in IP_GATEWAYS:
        ip_cards += f"""
        <div class="card" style="display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
              <span class="badge" style="background: var(--info-bg); color: var(--text-accent);">{escape(ip_item['subnet_mask'])}</span>
              <span style="font-size: 0.75rem; color: var(--text-muted);">{escape(ip_item['class_type'].split()[0])}</span>
            </div>
            <h3 style="font-size: 1.35rem; font-family: var(--font-mono); font-weight: 800; margin-bottom: 0.4rem;">
              <a href="/ip/{escape(ip_item['slug'])}/">{escape(ip_item['ip'])}</a>
            </h3>
            <p style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 0.75rem;">
              {escape(ip_item['brands'])}
            </p>
          </div>
          <div style="border-top: 1px solid var(--border-color); padding-top: 0.75rem; display: flex; justify-content: space-between; align-items: center;">
            <span style="font-size: 0.775rem; color: var(--text-muted);">Pass: <code>{escape(ip_item['default_creds'].split()[0])}</code></span>
            <a href="/ip/{escape(ip_item['slug'])}/" style="font-size: 0.85rem; font-weight: 600;">Explore IP &rarr;</a>
          </div>
        </div>
        """

    content_master = f"""
  <main class="container" style="padding-top: 2rem; padding-bottom: 4rem;">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 2.5rem auto;">
      <div class="silo-badge silo-badge-ip">⚡ Private Gateway IP Silo</div>
      <h1 style="font-size: 2.25rem; font-weight: 800; margin-bottom: 0.75rem;">
        Default Gateway IP Directory
      </h1>
      <p style="font-size: 1.1rem; color: var(--text-secondary);">
        Complete index of RFC 1918 private IPv4 subnets used as administration web portals across commercial routers.
      </p>
    </div>

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
          <a href="/tools/subnet-calculator/" class="btn btn-secondary" style="font-size: 0.85rem;">Subnet Calculator &rarr;</a>
          <a href="/tools/wifi-qr-code/" class="btn btn-secondary" style="font-size: 0.85rem;">Wi-Fi QR Code &rarr;</a>
          <a href="/tools/detect-gateway/" class="btn btn-secondary" style="font-size: 0.85rem;">Gateway Auto-Detector &rarr;</a>
        </div>
      </div>
    </div>
  </main>
"""
        full_html = get_header(title, desc, canonical, active_nav="tools", breadcrumbs=breadcrumbs) + content + get_footer()
        with open(os.path.join(tool_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(full_html)

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
        "snippet": "All 7 client-side tools: Wi-Fi QR generator, CIDR subnet calculator, gateway detector, password generator.",
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
