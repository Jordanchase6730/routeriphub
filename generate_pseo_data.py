# -*- coding: utf-8 -*-
"""
Data definitions for RouterIPHub Programmatic SEO (pSEO) Platform
"""

from generate_expanded_models import create_models_catalog

ROUTER_MODELS = create_models_catalog()

ISP_GATEWAYS = [
    {
        "slug": "xfinity-xfi",
        "isp_name": "Xfinity (Comcast)",
        "gateway_name": "xFi Advanced Gateway (XB6, XB7, XB8)",
        "default_ip": "10.0.0.1",
        "web_address": "http://10.0.0.1",
        "default_username": "admin",
        "default_password": "password",
        "sticker_note": "If default 'password' does not work, log into the Xfinity App or check the barcode sticker on the bottom of the gateway.",
        "bridge_mode_guide": "Log into http://10.0.0.1 > Go to Gateway > At a Glance > Locate 'Bridge Mode' > Click 'Enable'. The gateway's Wi-Fi radios will shut down, and Port 1 / Port 4 will pass the public WAN IP directly to your personal router.",
        "app_name": "Xfinity App",
        "app_url": "https://apps.apple.com/app/xfinity/id1178765645",
        "reset_procedure": "Press and hold the WPS button on the rear panel for 30-45 seconds until the top status light begins flashing white/amber. Wait 5 minutes for reboot.",
        "notes": "Xfinity's primary default subnet is 10.0.0.1/24. Modern XB7 and XB8 gateways support Wi-Fi 6 and Wi-Fi 6E."
    },
    {
        "slug": "att-bgw320",
        "isp_name": "AT&T Fiber",
        "gateway_name": "AT&T Fiber BGW320 / BGW210 Gateway",
        "default_ip": "192.168.1.254",
        "web_address": "http://192.168.1.254",
        "default_username": "admin",
        "default_password": "Printed Device Access Code (DAC)",
        "sticker_note": "AT&T does not use a generic password. You MUST locate the 10-digit 'Device Access Code' printed in bold on the yellow/white sticker on the back or base of the BGW320.",
        "bridge_mode_guide": "AT&T modems do not offer true bridge mode; use 'IP Passthrough': Navigate to http://192.168.1.254 > Firewall > IP Passthrough. Set Allocation Mode to 'Passthrough', Passthrough Mode to 'DHCPS-fixed', and select your router's MAC address from the Device List.",
        "app_name": "myAT&T / Smart Home Manager",
        "app_url": "https://apps.apple.com/app/att-smart-home-manager/id1200720448",
        "reset_procedure": "Press and hold the red Reset button on the rear for 20 seconds. The front status light will flash fast green, signaling a factory reset.",
        "notes": "Direct integrated optical SFP port for AT&T Fiber. Gateway IP is strictly 192.168.1.254."
    },
    {
        "slug": "verizon-cr1000a",
        "isp_name": "Verizon Fios",
        "gateway_name": "Fios Router CR1000A / Fios Home Router G3100",
        "default_ip": "192.168.1.1",
        "web_address": "http://192.168.1.1",
        "default_username": "admin",
        "default_password": "Printed on router base label",
        "sticker_note": "Unique randomized admin password printed on the back label under 'Admin Password'. Do not confuse with the Wi-Fi password.",
        "bridge_mode_guide": "For Fios Gigabit: If using your own router, you can disconnect the Fios router entirely and plug your personal router's WAN port directly into the Verizon ONT Ethernet jack. If keeping CR1000A for Fios TV Guide: disable Wi-Fi in the CR1000A web interface and place your personal router into DMZ Host.",
        "app_name": "My Fios / My Verizon",
        "app_url": "https://apps.apple.com/app/my-fios/id381878950",
        "reset_procedure": "Locate the red Reset pinhole button on the back. Hold for 15 seconds with a paperclip until the front status ring turns solid red.",
        "notes": "Supports Wi-Fi 6E with 2.5G WAN and 10G LAN ports. Self-Organizing Network (SON) enabled by default."
    },
    {
        "slug": "spectrum-sac2v1k",
        "isp_name": "Spectrum (Charter)",
        "gateway_name": "Spectrum Wi-Fi 6 Router (SAC2V1K, SAX1V1K)",
        "default_ip": "192.168.1.1",
        "web_address": "http://192.168.1.1",
        "default_username": "admin",
        "default_password": "admin (or managed via My Spectrum App)",
        "sticker_note": "Modern Spectrum Wi-Fi 6 routers restrict advanced web GUI settings and instruct users to configure Wi-Fi and port forwards via the My Spectrum mobile application.",
        "bridge_mode_guide": "Spectrum provides a standalone cable modem (e.g. E31T2V1) and a separate router (SAX1V1K). To use your own router: simply unplug and return the Spectrum router, and connect your own router's WAN port directly to the Spectrum modem.",
        "app_name": "My Spectrum App",
        "app_url": "https://apps.apple.com/app/my-spectrum/id942608209",
        "reset_procedure": "Press and hold the Reset button on the back panel for 10-15 seconds. The front LED will turn red, then cycle through blue and green.",
        "notes": "Delivered with standalone DOCSIS 3.1 cable modems across Charter, Time Warner, and Bright House service territories."
    },
    {
        "slug": "t-mobile-kvd21",
        "isp_name": "T-Mobile Home Internet",
        "gateway_name": "T-Mobile 5G Gateway (KVD21, Arcadyan, G4SE)",
        "default_ip": "192.168.12.1",
        "web_address": "http://192.168.12.1",
        "default_username": "admin",
        "default_password": "Admin password printed on bottom sticker",
        "sticker_note": "The gateway has a dedicated LCD color screen on the front. Swipe through the screens to view default Wi-Fi credentials and admin access codes.",
        "bridge_mode_guide": "T-Mobile 5G Gateways do NOT offer bridge mode or IP passthrough due to Carrier-Grade NAT (CGNAT). To use an external router: connect your router's WAN port to LAN Port 1 on the T-Mobile gateway, and use Access Point (AP) mode on your router to avoid Double NAT.",
        "app_name": "T-Life (formerly T-Mobile Internet)",
        "app_url": "https://apps.apple.com/app/t-life/id1527372483",
        "reset_procedure": "With the unit powered on, insert a paperclip into the Reset hole on the rear. Hold for 30 seconds until the front LCD display reads 'Factory Resetting'.",
        "notes": "Uses unique 192.168.12.1 subnet. Connects via 5G Ultra Capacity (n41/n71) cellular networks."
    },
    {
        "slug": "centurylink-c4000",
        "isp_name": "CenturyLink / Quantum Fiber",
        "gateway_name": "CenturyLink C4000LG / C4000XG Wi-Fi 6 Router",
        "default_ip": "192.168.0.1",
        "web_address": "http://192.168.0.1",
        "default_username": "admin",
        "default_password": "Admin / Configuration password on sticker",
        "sticker_note": "The default login is 'admin' and the password is the unique 'Admin Password' on the side label.",
        "bridge_mode_guide": "Navigate to http://192.168.0.1 > Advanced Setup > WAN Settings > Select 'Transparent Bridging'. If on CenturyLink Fiber, configure your 3rd-party router with VLAN ID 201 on the WAN port and enter your PPPoE credentials.",
        "app_name": "CenturyLink App / Quantum Fiber App",
        "app_url": "https://apps.apple.com/app/centurylink/id1396263595",
        "reset_procedure": "Press and hold the Reset button on the side for 15 seconds until the status ring flashes amber.",
        "notes": "Commonly deployed across CenturyLink DSL and Quantum Fiber gigabit installations."
    },
    {
        "slug": "bt-smart-hub",
        "isp_name": "BT (British Telecom)",
        "gateway_name": "BT Smart Hub 2 (Home Hub 6)",
        "default_ip": "192.168.1.254",
        "web_address": "http://192.168.1.254",
        "default_username": "admin",
        "default_password": "Admin password on removable plastic card",
        "sticker_note": "BT includes a slide-out plastic card located on the top/back of the Hub containing your unique Hub Admin Password and Wi-Fi Key.",
        "bridge_mode_guide": "The BT Smart Hub 2 cannot be switched into bridge mode. To use a custom router: disable Smart Hub Wi-Fi, assign your personal router a static IP (e.g. 192.168.1.100), and add it to the DMZ in the Smart Hub firewall settings.",
        "app_name": "My BT App",
        "app_url": "https://apps.apple.com/app/my-bt/id590211756",
        "reset_procedure": "Push a paperclip into the pinhole Reset button on the back for 20 seconds. The front light will flash green, then solid blue when ready.",
        "notes": "Dominant UK home broadband router. Operates exclusively on 192.168.1.254."
    },
    {
        "slug": "virgin-media-hub",
        "isp_name": "Virgin Media (UK)",
        "gateway_name": "Virgin Media Hub 3, Hub 4, Hub 5",
        "default_ip": "192.168.0.1",
        "web_address": "http://192.168.0.1",
        "default_username": "admin",
        "default_password": "Settings password on bottom sticker",
        "sticker_note": "Look at the sticker under the base of the Hub for the 'Settings Password'.",
        "bridge_mode_guide": "Virgin Media offers an official 'Modem Mode': Go to http://192.168.0.1 > Modem Mode > Select 'Enable Modem Mode'. Click Apply. The Hub reboots, turns its base light magenta/magenta-purple, and its web interface moves to 192.168.100.1 with port 1 active.",
        "app_name": "Virgin Media Connect App",
        "app_url": "https://apps.apple.com/app/virgin-media-connect/id1438965610",
        "reset_procedure": "Press and hold the pinhole Reset button on the rear for 60 seconds. Release and wait 5 minutes.",
        "notes": "Fastest UK cable broadband. In Modem Mode, IP shifts from 192.168.0.1 to 192.168.100.1."
    },
    {
        "slug": "sky-broadband",
        "isp_name": "Sky Broadband (UK)",
        "gateway_name": "Sky Broadband Hub (SR203)",
        "default_ip": "192.168.0.1",
        "web_address": "http://192.168.0.1",
        "default_username": "admin",
        "default_password": "sky (or Wi-Fi password in lowercase)",
        "sticker_note": "Default username is 'admin' and password is 'sky' on older models; newer firmware uses the default Wi-Fi password printed on the barcode label.",
        "bridge_mode_guide": "Sky does not support bridge mode. To use a third-party router directly with Sky FTTP: ensure your router supports DHCP Option 61 (Client Identifier) or DHCP Option 60/mer (MER authentication).",
        "app_name": "My Sky App",
        "app_url": "https://apps.apple.com/app/my-sky/id1112447990",
        "reset_procedure": "Press and hold the Reset button on the back for 12 seconds until the power light flashes.",
        "notes": "Standard UK DSL/Fiber gateway configured on 192.168.0.1."
    },
    {
        "slug": "telstra-smart-modem",
        "isp_name": "Telstra (Australia)",
        "gateway_name": "Telstra Smart Modem Gen 2 / Gen 3 (Technicolor/Arcadyan)",
        "default_ip": "192.168.0.1",
        "web_address": "http://192.168.0.1",
        "default_username": "admin",
        "default_password": "admin (or Telstra printed password)",
        "sticker_note": "Older units resolve to http://10.0.0.138. Newer Gen 2/3 modems resolve to http://192.168.0.1 or http://mygateway.telstra.com.",
        "bridge_mode_guide": "Navigate to Advanced > Broadband > Disable PPPoE / Enable Bridge Mode. Note: Bridging will disable the built-in 4G cellular backup SIM card.",
        "app_name": "My Telstra App",
        "app_url": "https://apps.apple.com/app/my-telstra/id1453229871",
        "reset_procedure": "Hold the Reset button on the back for 15 seconds until all front lights illuminate green, then release.",
        "notes": "Includes integrated 4G mobile backup fallback. Default Australian gateway IP."
    }
]

BRAND_PROFILES = [
    {
        "slug": "draytek",
        "name": "DrayTek",
        "hq": "Hsinchu, Taiwan",
        "default_ips": ["192.168.1.1"],
        "default_creds": "admin / admin",
        "web_domains": ["192.168.1.1"],
        "app_name": "DrayTek Wireless App",
        "app_url": "https://www.draytek.com",
        "support_domain": "https://www.draytek.com/support/guides/",
        "models_count": 8,
        "description": "Enterprise and business networking manufacturer renowned for Vigor multi-WAN routers, rock-solid hardware firewalls, and robust VPN concentrators."
    },
    {
        "slug": "motorola",
        "name": "Motorola",
        "hq": "Chicago, Illinois, USA",
        "default_ips": ["192.168.0.1", "192.168.1.1"],
        "default_creds": "admin / motorola",
        "web_domains": ["192.168.0.1"],
        "app_name": "motosync App",
        "app_url": "https://apps.apple.com/app/motosync/id1527814408",
        "support_domain": "https://help.motorolanetwork.com",
        "models_count": 6,
        "description": "Pioneering communications brand producing popular DOCSIS 3.1 and 3.0 cable modem routers including MG8702 and MG7700 series."
    },

    {
        "slug": "netgear",
        "name": "Netgear",
        "hq": "San Jose, California, USA",
        "default_ips": ["192.168.1.1", "192.168.0.1"],
        "default_creds": "admin / password",
        "web_domains": ["routerlogin.net", "routerlogin.com", "orbilogin.com"],
        "app_name": "Netgear Nighthawk & Orbi App",
        "app_url": "https://apps.apple.com/app/netgear-nighthawk/id1350284457",
        "support_domain": "https://kb.netgear.com",
        "models_count": 18,
        "description": "Netgear is one of the world's most ubiquitous networking equipment brands, renowned for its Nighthawk gaming routers and Orbi whole-home mesh systems."
    },
    {
        "slug": "tp-link",
        "name": "TP-Link",
        "hq": "Irvine, California / Singapore",
        "default_ips": ["192.168.0.1", "192.168.1.1", "192.168.68.1"],
        "default_creds": "admin / admin (or created on first setup)",
        "web_domains": ["tplinkwifi.net", "tplinkdeco.net", "tplogin.cn"],
        "app_name": "TP-Link Tether & Deco App",
        "app_url": "https://apps.apple.com/app/tp-link-tether/id599496594",
        "support_domain": "https://www.tp-link.com/support/",
        "models_count": 24,
        "description": "TP-Link manufactures the high-value Archer series and Deco mesh networks, utilizing 192.168.0.1 and 192.168.68.1 subnets."
    },
    {
        "slug": "asus",
        "name": "ASUS",
        "hq": "Taipei, Taiwan",
        "default_ips": ["192.168.1.1", "192.168.50.1"],
        "default_creds": "admin / admin",
        "web_domains": ["router.asus.com", "asusrouter.com"],
        "app_name": "ASUS Router App",
        "app_url": "https://apps.apple.com/app/asus-router/id1033764074",
        "support_domain": "https://www.asus.com/support/",
        "models_count": 16,
        "description": "ASUS delivers gaming-oriented routers powered by AsusWRT, featuring ROG Rapture and RT series with Merlin community firmware support."
    },
    {
        "slug": "linksys",
        "name": "Linksys",
        "hq": "Irvine, California, USA",
        "default_ips": ["192.168.1.1", "192.168.0.1"],
        "default_creds": "admin / admin",
        "web_domains": ["myrouter.local"],
        "app_name": "Linksys App",
        "app_url": "https://apps.apple.com/app/linksys/id633514718",
        "support_domain": "https://www.linksys.com/support/",
        "models_count": 14,
        "description": "Creator of the iconic WRT54G, Linksys produces Velop mesh systems and Max-Stream routers with standard 192.168.1.1 gateways."
    },
    {
        "slug": "ubiquiti",
        "name": "Ubiquiti",
        "hq": "New York City, New York, USA",
        "default_ips": ["192.168.1.1"],
        "default_creds": "UI Account / root",
        "web_domains": ["unifi.ui.com", "amplifi.lan"],
        "app_name": "UniFi Network App",
        "app_url": "https://apps.apple.com/app/unifi-network/id1057750338",
        "support_domain": "https://help.ui.com",
        "models_count": 12,
        "description": "Enterprise-grade prosumer SDN platform spanning UniFi Dream Machines, Cloud Gateways, and AmpliFi mesh routers."
    },
    {
        "slug": "cisco",
        "name": "Cisco",
        "hq": "San Jose, California, USA",
        "default_ips": ["192.168.1.1", "192.168.1.254", "10.0.0.1"],
        "default_creds": "cisco / cisco (or admin / admin)",
        "web_domains": ["N/A (IP access or Cisco Business Dashboard)"],
        "app_name": "Cisco Business App",
        "app_url": "https://apps.apple.com/app/cisco-business-dashboard/id1453229871",
        "support_domain": "https://www.cisco.com/c/en/us/support/",
        "models_count": 15,
        "description": "The global standard for enterprise routing and switching, including Cisco RV Small Business series and Catalyst managed switches."
    },
    {
        "slug": "mikrotik",
        "name": "MikroTik",
        "hq": "Riga, Latvia",
        "default_ips": ["192.168.88.1"],
        "default_creds": "admin / [empty]",
        "web_domains": ["router.lan"],
        "app_name": "MikroTik App (WinBox)",
        "app_url": "https://apps.apple.com/app/mikrotik/id1323064830",
        "support_domain": "https://help.mikrotik.com",
        "models_count": 12,
        "description": "Latvian networking powerhouse running RouterOS, beloved by network engineers for WireGuard, BGP, and VLAN flexibility on 192.168.88.1."
    },
    {
        "slug": "arris",
        "name": "Arris",
        "hq": "Suwanee, Georgia, USA",
        "default_ips": ["192.168.0.1", "192.168.100.1"],
        "default_creds": "admin / password",
        "web_domains": ["N/A (Direct IP)"],
        "app_name": "SURFboard Central App",
        "app_url": "https://apps.apple.com/app/surfboard-central/id1454519659",
        "support_domain": "https://www.surfboard.com/support/",
        "models_count": 10,
        "description": "Dominant DOCSIS cable modem and gateway manufacturer behind the SURFboard SB8200 and G36 series."
    },
    {
        "slug": "xfinity",
        "name": "Xfinity",
        "hq": "Philadelphia, Pennsylvania, USA",
        "default_ips": ["10.0.0.1"],
        "default_creds": "admin / password",
        "web_domains": ["internet.xfinity.com"],
        "app_name": "Xfinity App",
        "app_url": "https://apps.apple.com/app/xfinity/id1178765645",
        "support_domain": "https://www.xfinity.com/support/",
        "models_count": 8,
        "description": "Comcast's consumer broadband brand deploying the xFi gateway series configured on private Class A 10.0.0.1 subnets."
    },
    {
        "slug": "d-link",
        "name": "D-Link",
        "hq": "Taipei, Taiwan",
        "default_ips": ["192.168.0.1", "192.168.1.1"],
        "default_creds": "Admin / [empty or password]",
        "web_domains": ["dlinkrouter.local"],
        "app_name": "D-Link Wi-Fi App",
        "app_url": "https://apps.apple.com/app/d-link-wi-fi/id1438965610",
        "support_domain": "https://support.dlink.com",
        "models_count": 10,
        "description": "Longstanding Taiwanese brand offering EXO and EAGLE PRO AI series routers utilizing standard 192.168.0.1 portals."
    },
    {
        "slug": "huawei",
        "name": "Huawei",
        "hq": "Shenzhen, China",
        "default_ips": ["192.168.8.1", "192.168.100.1", "192.168.3.1"],
        "default_creds": "admin / admin (or printed on label)",
        "web_domains": ["N/A (Direct IP)"],
        "app_name": "Huawei AI Life",
        "app_url": "https://consumer.huawei.com/en/mobileservices/ai-life/",
        "support_domain": "https://consumer.huawei.com/en/support/",
        "models_count": 12,
        "description": "Leading global telecommunications supplier famous for 4G/5G mobile pocket hotspots (192.168.8.1) and fiber GPON ONTs (192.168.100.1)."
    },
    {
        "slug": "avm-fritzbox",
        "name": "AVM FRITZ!Box",
        "hq": "Berlin, Germany",
        "default_ips": ["192.168.178.1"],
        "default_creds": "admin / sticker password",
        "web_domains": ["fritz.box"],
        "app_name": "MyFRITZ!App",
        "app_url": "https://apps.apple.com/app/myfritz-app/id451230680",
        "support_domain": "https://avm.de/service/",
        "models_count": 8,
        "description": "Germany's top broadband gateway manufacturer, standardized on the distinctive 192.168.178.1 subnet and FRITZ!OS."
    },
    {
        "slug": "synology",
        "name": "Synology",
        "hq": "New Taipei City, Taiwan",
        "default_ips": ["192.168.1.1"],
        "default_creds": "admin / set on setup",
        "web_domains": ["router.synology.com"],
        "app_name": "DS router App",
        "app_url": "https://apps.apple.com/app/ds-router/id854964653",
        "support_domain": "https://www.synology.com/support",
        "models_count": 5,
        "description": "Makers of the acclaimed SRM operating system, delivering enterprise security, VLAN isolation, and traffic analysis for homes."
    },
    {
        "slug": "gl-inet",
        "name": "GL.iNet",
        "hq": "Hong Kong / Shenzhen",
        "default_ips": ["192.168.8.1"],
        "default_creds": "root / admin (or set on setup)",
        "web_domains": ["N/A (Direct IP)"],
        "app_name": "GL.iNet App",
        "app_url": "https://apps.apple.com/app/gl-inet/id1459424849",
        "support_domain": "https://docs.gl-inet.com",
        "models_count": 8,
        "description": "Pocket travel routers and IoT gateways running OpenWrt with native VPN kill-switches and Tor integration on 192.168.8.1."
    },
    {
        "slug": "eero",
        "name": "Amazon Eero",
        "hq": "San Francisco, California, USA",
        "default_ips": ["192.168.4.1", "192.168.7.1"],
        "default_creds": "Managed via Amazon App",
        "web_domains": ["N/A (App only)"],
        "app_name": "eero App",
        "app_url": "https://apps.apple.com/app/eero/id999605804",
        "support_domain": "https://support.eero.com",
        "models_count": 6,
        "description": "Amazon's user-friendly mesh networking family running TrueMesh routing on 192.168.4.1 subnets."
    },
    {
        "slug": "google-nest",
        "name": "Google Nest",
        "hq": "Mountain View, California, USA",
        "default_ips": ["192.168.86.1"],
        "default_creds": "Managed via Google Home App",
        "web_domains": ["N/A (App only)"],
        "app_name": "Google Home App",
        "app_url": "https://apps.apple.com/app/google-home/id857864704",
        "support_domain": "https://support.google.com/googlenest",
        "models_count": 5,
        "description": "Google's smart mesh system integrated with Google Home, Matter smart devices, and automated 192.168.86.1 subnet allocation."
    }
]

IP_GATEWAYS = [
    {
        "ip": "192.168.1.1",
        "slug": "192-168-1-1",
        "class_type": "Class C Private (192.168.0.0/16)",
        "brands": "Netgear, ASUS, Linksys, Cisco, Verizon Fios, Ubiquiti",
        "default_creds": "admin / admin or admin / password",
        "subnet_mask": "255.255.255.0 (/24)",
        "usable_range": "192.168.1.2 - 192.168.1.254",
        "summary": "192.168.1.1 is the world's most widely assigned default gateway IP, managing home and small business local area networks."
    },
    {
        "ip": "192.168.0.1",
        "slug": "192-168-0-1",
        "class_type": "Class C Private (192.168.0.0/16)",
        "brands": "TP-Link, D-Link, Arris, Sky Broadband, Virgin Media",
        "default_creds": "admin / admin (or created on first boot)",
        "subnet_mask": "255.255.255.0 (/24)",
        "usable_range": "192.168.0.2 - 192.168.0.254",
        "summary": "192.168.0.1 is the #2 most popular default gateway address, standard across TP-Link, D-Link, and major UK/EU cable routers."
    },
    {
        "ip": "10.0.0.1",
        "slug": "10-0-0-1",
        "class_type": "Class A Private (10.0.0.0/8)",
        "brands": "Xfinity (Comcast), Apple AirPort, Cisco, Spectrum",
        "default_creds": "admin / password",
        "subnet_mask": "255.255.255.0 (/24 standard local allocation)",
        "usable_range": "10.0.0.2 - 10.0.0.254",
        "summary": "10.0.0.1 is the default gateway for Comcast Xfinity xFi gateways and enterprise networks utilizing Class A IP addressing."
    },
    {
        "ip": "192.168.1.254",
        "slug": "192-168-1-254",
        "class_type": "Class C Private (192.168.0.0/16)",
        "brands": "AT&T Fiber (BGW320), BT Smart Hub (UK), Plusnet, 2Wire",
        "default_creds": "admin / Printed Access Code",
        "subnet_mask": "255.255.255.0 (/24)",
        "usable_range": "192.168.1.1 - 192.168.1.253",
        "summary": "192.168.1.254 occupies the highest usable host IP in the 192.168.1.0/24 subnet, standard for AT&T Fiber and BT Smart Hub 2."
    },
    {
        "ip": "192.168.2.1",
        "slug": "192-168-2-1",
        "class_type": "Class C Private (192.168.0.0/16)",
        "brands": "Belkin, SMC, Bell Home Hub (Canada), Philips Hue Bridge",
        "default_creds": "admin / [empty] or admin / admin",
        "subnet_mask": "255.255.255.0 (/24)",
        "usable_range": "192.168.2.2 - 192.168.2.254",
        "summary": "192.168.2.1 is common across Belkin routers and Bell Canada Home Hub gateways to avoid conflicts with 192.168.1.1 modems."
    },
    {
        "ip": "192.168.8.1",
        "slug": "192-168-8-1",
        "class_type": "Class C Private (192.168.0.0/16)",
        "brands": "Huawei, GL.iNet Travel Routers, 4G/5G Mobile Hotspots",
        "default_creds": "admin / admin",
        "subnet_mask": "255.255.255.0 (/24)",
        "usable_range": "192.168.8.2 - 192.168.8.254",
        "summary": "Standard gateway IP for portable travel routers, OpenWrt pocket gateways, and cellular LTE/5G USB dongles."
    },
    {
        "ip": "192.168.10.1",
        "slug": "192-168-10-1",
        "class_type": "Class C Private (192.168.0.0/16)",
        "brands": "Trendnet, ZyXEL, Motorola Gateway combos",
        "default_creds": "admin / admin",
        "subnet_mask": "255.255.255.0 (/24)",
        "usable_range": "192.168.10.2 - 192.168.10.254",
        "summary": "192.168.10.1 is standard on commercial Trendnet and ZyXEL networking gear and multi-WAN balancing setups."
    },
    {
        "ip": "192.168.11.1",
        "slug": "192-168-11-1",
        "class_type": "Class C Private (192.168.0.0/16)",
        "brands": "Buffalo AirStation, DD-WRT Japanese releases",
        "default_creds": "root / [empty] or admin / password",
        "subnet_mask": "255.255.255.0 (/24)",
        "usable_range": "192.168.11.2 - 192.168.11.254",
        "summary": "Default management IP for Buffalo AirStation routers and specialized Japanese enterprise equipment."
    },
    {
        "ip": "192.168.12.1",
        "slug": "192-168-12-1",
        "class_type": "Class C Private (192.168.0.0/16)",
        "brands": "T-Mobile 5G Home Internet (KVD21, Arcadyan, Sagemcom)",
        "default_creds": "admin / sticker password",
        "subnet_mask": "255.255.255.0 (/24)",
        "usable_range": "192.168.12.2 - 192.168.12.254",
        "summary": "The unique default subnet for all T-Mobile 5G Home Internet Wi-Fi gateways across the United States."
    },
    {
        "ip": "192.168.31.1",
        "slug": "192-168-31-1",
        "class_type": "Class C Private (192.168.0.0/16)",
        "brands": "Xiaomi Mi WiFi, Redmi Routers",
        "default_creds": "admin / set on first boot via miwifi.com",
        "subnet_mask": "255.255.255.0 (/24)",
        "usable_range": "192.168.31.2 - 192.168.31.254",
        "summary": "192.168.31.1 is the standard gateway IP across all Xiaomi and Redmi Wi-Fi routers (miwifi.com)."
    },
    {
        "ip": "192.168.68.1",
        "slug": "192-168-68-1",
        "class_type": "Class C Private (192.168.0.0/16)",
        "brands": "TP-Link Deco Whole Home Mesh Series (X55, XE75, BE85)",
        "default_creds": "Managed via TP-Link Deco App",
        "subnet_mask": "255.255.255.0 (/24)",
        "usable_range": "192.168.68.2 - 192.168.68.254",
        "summary": "The dedicated default subnet for TP-Link Deco mesh systems, selected by TP-Link to eliminate IP conflicts with upstream ISP modems."
    },
    {
        "ip": "192.168.88.1",
        "slug": "192-168-88-1",
        "class_type": "Class C Private (192.168.0.0/16)",
        "brands": "MikroTik RouterBOARD & RouterOS (hAP, RB series)",
        "default_creds": "admin / [empty]",
        "subnet_mask": "255.255.255.0 (/24)",
        "usable_range": "192.168.88.2 - 192.168.88.254",
        "summary": "The factory default gateway across every MikroTik RouterOS device, managed via WinBox or web interface (router.lan)."
    },
    {
        "ip": "192.168.100.1",
        "slug": "192-168-100-1",
        "class_type": "Class C Private (192.168.0.0/16)",
        "brands": "Huawei ONT, Motorola & Arris Cable Modems, Virgin Media Modem Mode",
        "default_creds": "admin / admin (or TelecomAdmin)",
        "subnet_mask": "255.255.255.0 (/24)",
        "usable_range": "192.168.100.2 - 192.168.100.254",
        "summary": "Standard diagnostic IP for DOCSIS cable modems and fiber optical network terminals (ONTs) in bridge/passthrough mode."
    },
    {
        "ip": "192.168.178.1",
        "slug": "192-168-178-1",
        "class_type": "Class C Private (192.168.0.0/16)",
        "brands": "AVM FRITZ!Box (7590 AX, 6660 Cable, 5590 Fiber)",
        "default_creds": "admin / sticker password",
        "subnet_mask": "255.255.255.0 (/24)",
        "usable_range": "192.168.178.2 - 192.168.178.254",
        "summary": "The universal European gateway IP for all AVM FRITZ!Box models (accessible locally via fritz.box)."
    },
    {
        "ip": "10.0.1.1",
        "slug": "10-0-1-1",
        "class_type": "Class A Private (10.0.0.0/8)",
        "brands": "Apple AirPort Extreme, AirPort Time Capsule, Cisco",
        "default_creds": "admin / admin (or configured via AirPort Utility)",
        "subnet_mask": "255.255.255.0 (/24)",
        "usable_range": "10.0.1.2 - 10.0.1.254",
        "summary": "Standard gateway for legacy Apple AirPort hardware and secondary corporate VLAN subnets."
    },
    {
        "ip": "10.0.0.138",
        "slug": "10-0-0-138",
        "class_type": "Class A Private (10.0.0.0/8)",
        "brands": "Telstra (Australia), Thomson / SpeedTouch, Technicolor",
        "default_creds": "admin / admin",
        "subnet_mask": "255.255.255.0 (/24)",
        "usable_range": "10.0.0.1 - 10.0.0.137, 10.0.0.139 - 10.0.0.254",
        "summary": "Historic default IP used across Australian Telstra gateways and European Technicolor modems."
    },
    {
        "ip": "192.168.1.2",
        "slug": "192-168-1-2",
        "class_type": "Class C Private (192.168.0.0/16)",
        "brands": "Wi-Fi Range Extenders, Secondary Access Points, Repeater Hubs",
        "default_creds": "admin / admin",
        "subnet_mask": "255.255.255.0 (/24)",
        "usable_range": "192.168.1.3 - 192.168.1.254",
        "summary": "Standard IP assigned to secondary access points, mesh satellites, and Wi-Fi repeaters chained off 192.168.1.1."
    }
]

TOOL_PAGES = [
    {
        "slug": "subnet-calculator",
        "title": "IPv4 CIDR Subnet Calculator",
        "short_title": "Subnet Calculator",
        "desc": "Calculate network ID, broadcast address, CIDR prefix (/8 to /30), usable host range, and binary subnet masks in real time.",
        "icon": "calculator"
    },
    {
        "slug": "wifi-qr-code",
        "title": "Wi-Fi QR Code Generator & Printable Card",
        "short_title": "Wi-Fi QR Generator",
        "desc": "Create encrypted WPA2/WPA3 QR codes for seamless smartphone guest network logins. Download high-resolution PNG or printable sign.",
        "icon": "qr"
    },
    {
        "slug": "detect-gateway",
        "title": "Local Router Gateway Auto-Detector",
        "short_title": "Gateway Auto-Detector",
        "desc": "Browser-based WebRTC and local probe utility that detects your active gateway subnet (192.168.1.1, 192.168.0.1, or 10.0.0.1).",
        "icon": "radar"
    },
    {
        "slug": "router-password-generator",
        "title": "WPA3 Secure Router Password Generator",
        "short_title": "Password Generator",
        "desc": "Generate cryptographically secure 16-to-32 character passwords compliant with WPA3, Wi-Fi 6, and router admin authentication standards.",
        "icon": "lock"
    },
    {
        "slug": "port-checker",
        "title": "Port Forwarding Directory & Latency Probe",
        "short_title": "Port Directory",
        "desc": "Quick lookup directory for common networking and gaming ports (Plex, Minecraft, SSH, HTTP) with port forwarding instructions.",
        "icon": "server"
    },
    {
        "slug": "cidr-cheat-sheet",
        "title": "CIDR Subnet Cheat-Sheet & CSV Exporter",
        "short_title": "CIDR Cheat-Sheet",
        "desc": "Complete reference table for IPv4 prefix lengths (/0 to /32) with total IPs, usable hosts, and wildcard masks with CSV download.",
        "icon": "table"
    },
    {
        "slug": "ip-address-checker",
        "title": "Public IP Address & Geolocation Lookup",
        "short_title": "IP Address Checker",
        "desc": "Inspect your public IPv4 and IPv6 address, ISP provider, Autonomous System Number (ASN), reverse DNS, and geolocation details.",
        "icon": "globe"
    },
    {
        "slug": "dns-propagation",
        "title": "Global DNS Propagation Checker",
        "short_title": "DNS Propagation",
        "desc": "Check real-time DNS record propagation (A, AAAA, CNAME, MX, TXT, NS, SOA) across multiple worldwide recursive DNS servers via DNS-over-HTTPS.",
        "icon": "satellite"
    }
]
