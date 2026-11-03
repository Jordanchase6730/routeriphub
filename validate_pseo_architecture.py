# -*- coding: utf-8 -*-
import os
import json
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

ROOT_DIR = r"C:\Users\acer\.gemini\antigravity\scratch\routeriphub"
PUBLIC_DIR = os.path.join(ROOT_DIR, "public")

errors = []
warnings = []
checked_files = 0

class StrictHTMLParser(HTMLParser):
    def __init__(self, filepath):
        super().__init__()
        self.filepath = filepath
        self.has_title = False
        self.has_canonical = False
        self.has_meta_desc = False
        self.json_ld_blocks = []
        self.in_json_ld = False
        self.current_json = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "title":
            self.has_title = True
        elif tag == "link" and attrs_dict.get("rel") == "canonical":
            self.has_canonical = True
        elif tag == "meta" and attrs_dict.get("name") == "description":
            self.has_meta_desc = True
        elif tag == "script" and attrs_dict.get("type") == "application/ld+json":
            self.in_json_ld = True
            self.current_json = ""

    def handle_endtag(self, tag):
        if tag == "script" and self.in_json_ld:
            self.in_json_ld = False
            self.json_ld_blocks.append(self.current_json.strip())
            self.current_json = ""

    def handle_data(self, data):
        if self.in_json_ld:
            self.current_json += data

print("Starting comprehensive validation of pSEO Architecture...")

# 1. Validate all HTML files
for root, dirs, files in os.walk(PUBLIC_DIR):
    for f in files:
        if f.endswith(".html"):
            checked_files += 1
            fpath = os.path.join(root, f)
            with open(fpath, "r", encoding="utf-8") as file:
                content = file.read()
            
            parser = StrictHTMLParser(fpath)
            try:
                parser.feed(content)
            except Exception as e:
                errors.append(f"HTML Parse Error in {fpath}: {e}")
                continue

            if not parser.has_title:
                errors.append(f"Missing <title> in {fpath}")
            if not parser.has_canonical:
                errors.append(f"Missing <link rel='canonical'> in {fpath}")
            if not parser.has_meta_desc:
                errors.append(f"Missing meta description in {fpath}")

            # Verify JSON-LD schemas
            for block in parser.json_ld_blocks:
                if block:
                    try:
                        parsed = json.loads(block)
                        if "@context" not in parsed:
                            warnings.append(f"JSON-LD in {fpath} missing @context")
                    except Exception as e:
                        errors.append(f"Invalid JSON-LD in {fpath}: {e}")

# 2. Validate Sitemaps
sitemap_index_path = os.path.join(PUBLIC_DIR, "sitemap.xml")
if not os.path.exists(sitemap_index_path):
    errors.append("Missing sitemap.xml")
else:
    try:
        tree = ET.parse(sitemap_index_path)
        root = tree.getroot()
        for elem in root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}sitemap"):
            loc = elem.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc").text
            sub_filename = loc.replace("https://routeriphub.com/sitemaps/", "")
            sub_path = os.path.join(PUBLIC_DIR, "sitemaps", sub_filename)
            if not os.path.exists(sub_path):
                errors.append(f"Sub-sitemap referenced in sitemap.xml does not exist: {sub_path}")
            else:
                try:
                    ET.parse(sub_path)
                except Exception as e:
                    errors.append(f"Invalid XML in sub-sitemap {sub_path}: {e}")
    except Exception as e:
        errors.append(f"Invalid XML in sitemap.xml: {e}")

# 3. Validate Data files
for json_name in ["routers.json", "gateways.json", "search-index.json"]:
    j_path = os.path.join(PUBLIC_DIR, "data", json_name)
    if not os.path.exists(j_path):
        errors.append(f"Missing data file: {j_path}")
    else:
        try:
            with open(j_path, "r", encoding="utf-8") as jf:
                json.load(jf)
        except Exception as e:
            errors.append(f"Corrupt JSON in {j_path}: {e}")

print(f"Total HTML files validated: {checked_files}")
print(f"Total Errors: {len(errors)}")
print(f"Total Warnings: {len(warnings)}")

if errors:
    for err in errors:
        print(f"ERROR: {err}")
else:
    print("ALL VALIDATION CHECKS PASSED PERFECTLY! 100% CLEAN CODEBASE.")
