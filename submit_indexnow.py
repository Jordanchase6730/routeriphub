# -*- coding: utf-8 -*-
"""
RouterIPHub - IndexNow Automated Submitter
Notifies Bing, Yandex, Naver, and Seznam instantly when URLs are published or updated.
Spec: https://www.indexnow.org/documentation
"""

import os
import json
import urllib.request
import xml.etree.ElementTree as ET

HOST = "routeriphub.com"
KEY = "8ca24a1b5a684ded9cbeb9910e7bf389"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"
PUBLIC_DIR = os.path.join(os.path.dirname(__file__), "public")
SITEMAP_INDEX = os.path.join(PUBLIC_DIR, "sitemap.xml")

def collect_all_urls():
    urls = []
    # If sitemap index exists, read all sub-sitemaps
    if os.path.exists(SITEMAP_INDEX):
        try:
            tree = ET.parse(SITEMAP_INDEX)
            root = tree.getroot()
            ns = {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            for sm in root.findall("ns:sitemap", ns):
                loc = sm.find("ns:loc", ns).text
                sub_name = loc.split("/")[-1]
                sub_path = os.path.join(PUBLIC_DIR, "sitemaps", sub_name)
                if os.path.exists(sub_path):
                    sub_tree = ET.parse(sub_path)
                    sub_root = sub_tree.getroot()
                    for u in sub_root.findall("ns:url", ns):
                        u_loc = u.find("ns:loc", ns).text
                        if u_loc and u_loc not in urls:
                            urls.append(u_loc)
        except Exception as e:
            print(f"Error parsing sitemaps: {e}")

    # Ensure key URLs are definitely included
    priority_urls = [
        "https://routeriphub.com/",
        "https://routeriphub.com/extenders/",
        "https://routeriphub.com/extenders/mywifiext-net/",
        "https://routeriphub.com/extenders/tplinkrepeater-net/",
        "https://routeriphub.com/extenders/extender-linksys-com/",
        "https://routeriphub.com/extenders/dlinkap-local/",
        "https://routeriphub.com/extenders/myrepeater-net/",
        "https://routeriphub.com/extenders/ap-setup/",
        "https://routeriphub.com/extenders/topvision-extender/",
        "https://routeriphub.com/extenders/sewot-sw-01/",
        "https://routeriphub.com/extenders/rangextd-extender/",
        "https://routeriphub.com/ip/192-168-1-250/",
        "https://routeriphub.com/ip/192-168-1-1/",
        "https://routeriphub.com/ip/192-168-0-1/",
        "https://routeriphub.com/ip/10-0-0-1/",
        "https://routeriphub.com/ip/192-168-1-254/",
        "https://routeriphub.com/tools/",
        "https://routeriphub.com/howto/",
        "https://routeriphub.com/find-router-ip/",
        "https://routeriphub.com/developers/"
    ]
    for pu in priority_urls:
        if pu not in urls:
            urls.append(pu)

    return urls

def submit_to_indexnow(urls):
    print(f"Found {len(urls)} URLs to submit to IndexNow...")
    endpoints = [
        "https://api.indexnow.org/indexnow",
        "https://www.bing.com/indexnow"
    ]

    # IndexNow accepts up to 10,000 URLs per batch
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls[:1000]
    }
    data = json.dumps(payload).encode("utf-8")

    for ep in endpoints:
        print(f"Submitting {len(payload['urlList'])} URLs to {ep}...")
        req = urllib.request.Request(
            ep,
            data=data,
            headers={
                "Content-Type": "application/json; charset=utf-8",
                "User-Agent": "RouterIPHub-IndexNow/1.0"
            },
            method="POST"
        )
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                status = resp.getcode()
                print(f"  -> Response: HTTP {status} (Success / Accepted by search engine)")
        except urllib.error.HTTPError as e:
            print(f"  -> HTTP Error {e.code}: {e.read().decode('utf-8', errors='ignore')}")
        except Exception as e:
            print(f"  -> Connection error: {e}")

if __name__ == "__main__":
    all_urls = collect_all_urls()
    submit_to_indexnow(all_urls)
