# -*- coding: utf-8 -*-
"""
Full Programmatic Dataset Generator: 251 Router Models with rich pSEO specifications.
"""

def create_models_catalog():
    models = []

    # --------------------------------------------------------------------------
    # 1. NETGEAR (25 Models)
    # --------------------------------------------------------------------------
    netgear_specs = [
        ("netgear-nighthawk-rax50", "Nighthawk AX6 (RAX50)", "Wi-Fi 6 Router", "192.168.1.1", "http://routerlogin.net", "192.168.0.1", "admin", "password", False, "NETGEAR-XX / NETGEAR-XX-5G", "Wi-Fi 6 (802.11ax AX5400)", 10, "5.4 Gbps 6-stream Wi-Fi 6 router with 5 Gigabit ports and USB 3.0."),
        ("netgear-nighthawk-rax120", "Nighthawk AX12 (RAX120)", "Wi-Fi 6 Flagship Router", "192.168.1.1", "http://routerlogin.net", "192.168.0.1", "admin", "password", False, "NETGEAR-XX / NETGEAR-XX-5G", "Wi-Fi 6 (12-Stream AX6000)", 10, "Includes 5G/2.5G Multi-Gig Ethernet port for high-speed fiber broadband."),
        ("netgear-nighthawk-xr1000", "Nighthawk Pro Gaming XR1000", "Gaming Wi-Fi 6 Router", "192.168.1.1", "http://routerlogin.net", "192.168.0.1", "admin", "password", False, "NETGEAR-XX / NETGEAR-XX-5G", "Wi-Fi 6 (AX5400 DumaOS 3.0)", 10, "Powered by DumaOS 3.0 featuring Geo-Fence, Ping Heatmap, and QoS allocation."),
        ("netgear-nighthawk-xr500", "Nighthawk Pro Gaming XR500", "Gaming Wi-Fi Router", "192.168.1.1", "http://routerlogin.net", "192.168.0.1", "admin", "password", False, "NETGEAR-XX", "Wi-Fi 5 (AC2600 DumaOS)", 10, "Dual-band AC2600 with 1.7GHz dual core processor and 4 external antennas."),
        ("netgear-nighthawk-xr700", "Nighthawk Pro Gaming XR700", "10G Flagship Gaming Router", "192.168.1.1", "http://routerlogin.net", "192.168.0.1", "admin", "password", False, "NETGEAR-XX", "Wi-Fi 5 (AD7200 60GHz + AC)", 10, "Includes 10G SFP+ LAN port for high-speed NAS connectivity and quad-core CPU."),
        ("netgear-nighthawk-xr300", "Nighthawk Pro Gaming XR300", "Entry Gaming Router", "192.168.1.1", "http://routerlogin.net", "192.168.0.1", "admin", "password", False, "NETGEAR-XX", "Wi-Fi 5 (AC1750 DumaOS)", 10, "Budget-friendly DumaOS gaming router with bandwidth prioritization."),
        ("netgear-nighthawk-rax40", "Nighthawk AX4 (RAX40)", "Wi-Fi 6 Router", "192.168.1.1", "http://routerlogin.net", "192.168.0.1", "admin", "password", False, "NETGEAR-XX", "Wi-Fi 6 (AX3000 Dual-Band)", 10, "4-stream Wi-Fi 6 router powered by Intel dual-core technology."),
        ("netgear-nighthawk-rax43", "Nighthawk AX5 (RAX43)", "Wi-Fi 6 Router", "192.168.1.1", "http://routerlogin.net", "192.168.0.1", "admin", "password", False, "NETGEAR-XX", "Wi-Fi 6 (AX4200 5-Stream)", 10, "5-stream Wi-Fi 6 router offering 4.2 Gbps combined wireless throughput."),
        ("netgear-nighthawk-rax80", "Nighthawk AX8 (RAX80)", "Wi-Fi 6 Router", "192.168.1.1", "http://routerlogin.net", "192.168.0.1", "admin", "password", False, "NETGEAR-XX", "Wi-Fi 6 (AX6000 8-Stream)", 10, "Iconic wing antenna design with 8 Wi-Fi streams and dual Gigabit port aggregation."),
        ("netgear-nighthawk-rax200", "Nighthawk Tri-Band AX12 (RAX200)", "Tri-Band Wi-Fi 6 Flagship", "192.168.1.1", "http://routerlogin.net", "192.168.0.1", "admin", "password", False, "NETGEAR-XX", "Wi-Fi 6 (AX11000 Tri-Band)", 10, "12-stream tri-band router capable of 10.8 Gbps aggregate throughput."),
        ("netgear-nighthawk-rs700s", "Nighthawk RS700S", "Wi-Fi 7 Multi-Gig Router", "192.168.1.1", "http://routerlogin.net", "192.168.0.1", "admin", "password", True, "NETGEAR-XX", "Wi-Fi 7 (BE19000 Tri-Band)", 10, "Next-generation Wi-Fi 7 router with 10Gbps WAN and 10Gbps LAN ports."),
        ("netgear-nighthawk-rs300", "Nighthawk RS300", "Wi-Fi 7 Router", "192.168.1.1", "http://routerlogin.net", "192.168.0.1", "admin", "password", True, "NETGEAR-XX", "Wi-Fi 7 (BE9300 Tri-Band)", 10, "Compact Wi-Fi 7 router supporting 320MHz ultra-wide channels and 2.5G ports."),
        ("netgear-nighthawk-r7000", "Nighthawk AC1900 (R7000)", "Smart Wi-Fi Router", "192.168.1.1", "http://routerlogin.net", "192.168.0.1", "admin", "password", False, "NETGEAR-XX", "Wi-Fi 5 (AC1900 Dual-Band)", 10, "The classic open-source friendly router, compatible with DD-WRT and Tomato."),
        ("netgear-nighthawk-r6700", "Nighthawk AC1750 (R6700)", "Smart Wi-Fi Router", "192.168.1.1", "http://routerlogin.net", "192.168.0.1", "admin", "password", False, "NETGEAR-XX", "Wi-Fi 5 (AC1750 Dual-Band)", 10, "Best-selling home gigabit router with Beamforming+ and high-power amplifiers."),
        ("netgear-nighthawk-r8000", "Nighthawk X6 AC3200 (R8000)", "Tri-Band Gigabit Router", "192.168.1.1", "http://routerlogin.net", "192.168.0.1", "admin", "password", False, "NETGEAR-XX", "Wi-Fi 5 (AC3200 Tri-Band)", 10, "Tri-Band technology with 6 retractable antennas and Smart Connect."),
        ("netgear-nighthawk-r8500", "Nighthawk X8 AC5300 (R8500)", "Tri-Band Quad-Stream Router", "192.168.1.1", "http://routerlogin.net", "192.168.0.1", "admin", "password", False, "NETGEAR-XX", "Wi-Fi 5 (AC5300 Tri-Band)", 10, "Features 4 active patent-pending antennas and 6 Gigabit Ethernet ports."),
        ("netgear-nighthawk-r9000", "Nighthawk X10 AD7200 (R9000)", "Smart Wi-Fi Router with 10G", "192.168.1.1", "http://routerlogin.net", "192.168.0.1", "admin", "password", False, "NETGEAR-XX", "Wi-Fi 5 / 802.11ad (AD7200)", 10, "1.7GHz quad-core processor with Plex Media Server and 10G SFP+ interface."),
        ("netgear-nighthawk-r7000p", "Nighthawk AC2300 (R7000P)", "Smart Wi-Fi Router", "192.168.1.1", "http://routerlogin.net", "192.168.0.1", "admin", "password", False, "NETGEAR-XX", "Wi-Fi 5 (AC2300 MU-MIMO)", 10, "Updated R7000 with MU-MIMO support and Netgear Armor cyber security."),
        ("netgear-nighthawk-rax35", "Nighthawk AX3000 (RAX35)", "Wi-Fi 6 Router", "192.168.1.1", "http://routerlogin.net", "192.168.0.1", "admin", "password", False, "NETGEAR-XX", "Wi-Fi 6 (AX3000 4-Stream)", 10, "Walmart-exclusive RAX40 variant offering 4-stream Wi-Fi 6 throughput."),
        ("netgear-orbi-rbk752", "Orbi Tri-Band WiFi 6 (RBK752)", "Whole Home Mesh System", "192.168.1.1", "http://orbilogin.com", "192.168.0.1", "admin", "password", True, "ORBI-XX", "Wi-Fi 6 (AX4200 Tri-Band Mesh)", 15, "Tri-band mesh with dedicated 5GHz wireless backhaul covering up to 5,000 sq ft."),
        ("netgear-orbi-rbk852", "Orbi WiFi 6 (RBK852)", "Flagship Mesh Wi-Fi 6", "192.168.1.1", "http://orbilogin.com", "192.168.0.1", "admin", "password", True, "ORBI-XX", "Wi-Fi 6 (AX6000 12-Stream)", 15, "High-performance mesh system with 2.5G WAN port and 4 Gigabit ports per node."),
        ("netgear-orbi-rbke963", "Orbi Quad-Band WiFi 6E (RBKE963)", "Quad-Band Mesh System", "192.168.1.1", "http://orbilogin.com", "192.168.0.1", "admin", "password", True, "ORBI-XX", "Wi-Fi 6E (AXE11000 Quad-Band)", 15, "World's first quad-band Wi-Fi 6E mesh featuring a dedicated 6GHz backhaul and 10G WAN."),
        ("netgear-orbi-rbe973", "Orbi WiFi 7 (RBE973)", "Quad-Band Wi-Fi 7 Mesh", "192.168.1.1", "http://orbilogin.com", "192.168.0.1", "admin", "password", True, "ORBI-XX", "Wi-Fi 7 (BE27000 Quad-Band)", 15, "Flagship Wi-Fi 7 mesh with 10Gbps Ethernet WAN and dual 10Gbps LAN ports."),
        ("netgear-orbi-lbr20", "Orbi 4G LTE WiFi Router (LBR20)", "Cellular Broadband Router", "192.168.1.1", "http://orbilogin.com", "192.168.0.1", "admin", "password", True, "ORBI-XX", "Wi-Fi 5 (AC2200 LTE Cat18)", 10, "Integrated LTE Cat 18 cellular modem offering up to 1.2Gbps failover broadband."),
        ("netgear-r6220", "Netgear AC1200 (R6220)", "Smart Wi-Fi Gigabit Router", "192.168.1.1", "http://routerlogin.net", "192.168.0.1", "admin", "password", False, "NETGEAR-XX", "Wi-Fi 5 (AC1200 Dual-Band)", 10, "High-reliability dual-band AC1200 router with 5 Gigabit ports and USB 2.0.")
    ]

    for item in netgear_specs:
        slug, name, hw_type, def_ip, web, fallback, user, pwd, sticker, ssid, standard, reset_sec, note = item
        models.append({
            "slug": slug,
            "brand": "Netgear",
            "brand_slug": "netgear",
            "model_name": name,
            "hardware_type": hw_type,
            "default_ip": def_ip,
            "web_domain": web,
            "fallback_ip": fallback,
            "default_username": user,
            "default_password": pwd,
            "password_on_sticker": sticker,
            "default_ssid_pattern": ssid,
            "wifi_standard": standard,
            "reset_instructions": f"With the router powered ON, press and hold the recessed Reset pinhole on the rear panel with a paperclip for {reset_sec} seconds until the Power LED starts blinking amber. Release and wait 2-3 minutes for the factory restart.",
            "led_indicators": [
                {"name": "Power", "normal": "Solid White", "error": "Blinking Amber (Resetting/Firmware Recovery)", "desc": "Hardware operational status."},
                {"name": "Internet / WAN", "normal": "Solid White", "error": "Solid Amber (Physical link OK, no IP) / Off", "desc": "Ethernet link to upstream modem or ONT."},
                {"name": "2.4 GHz Wi-Fi", "normal": "Solid White", "error": "Off (Radio disabled)", "desc": "2.4 GHz band broadcast."},
                {"name": "5 GHz Wi-Fi", "normal": "Solid White", "error": "Off (Radio disabled or DFS radar scan)", "desc": "5 GHz high-speed band status."},
                {"name": "LAN 1-4", "normal": "Solid White (1G) / Amber (100M)", "error": "Off (No cable connected)", "desc": "Local switch Ethernet ports."}
            ],
            "mobile_app": "Netgear Nighthawk App",
            "companion_app_store_url": "https://apps.apple.com/app/netgear-nighthawk/id1350284457",
            "official_manual_url": f"https://www.netgear.com/support/product/{slug.split('-')[-1].upper()}.aspx",
            "notes": note
        })

    # --------------------------------------------------------------------------
    # 2. TP-LINK (30 Models)
    # --------------------------------------------------------------------------
    tplink_specs = [
        ("tp-link-archer-ax55", "Archer AX55 (AX3000)", "Dual-Band Wi-Fi 6 Router", "192.168.0.1", "http://tplinkwifi.net", "192.168.1.1", "admin (created on setup)", "admin (created on setup)", False, "TP-Link_XXXX / TP-Link_XXXX_5G", "Wi-Fi 6 (AX3000)", 10, "Qualcomm dual-core CPU with 160MHz channel support and HomeShield security."),
        ("tp-link-archer-ax73", "Archer AX73 (AX5400)", "6-Stream Wi-Fi 6 Router", "192.168.0.1", "http://tplinkwifi.net", "192.168.1.1", "admin (created on setup)", "admin (created on setup)", False, "TP-Link_XXXX / TP-Link_XXXX_5G", "Wi-Fi 6 (AX5400)", 10, "6 high-gain antennas with 4T4R architecture and USB 3.0 sharing."),
        ("tp-link-archer-ax21", "Archer AX21 (AX1800)", "Dual-Band Wi-Fi 6 Router", "192.168.0.1", "http://tplinkwifi.net", "192.168.1.1", "admin (created on setup)", "admin (created on setup)", False, "TP-Link_XXXX", "Wi-Fi 6 (AX1800)", 10, "Quad-core 1.5GHz processor with OneMesh support and 4 Gigabit LAN ports."),
        ("tp-link-archer-ax10", "Archer AX10 (AX1500)", "Wi-Fi 6 Gigabit Router", "192.168.0.1", "http://tplinkwifi.net", "192.168.1.1", "admin", "admin", False, "TP-Link_XXXX", "Wi-Fi 6 (AX1500)", 10, "Affordable entry into Wi-Fi 6 with triple-core 1.5GHz CPU."),
        ("tp-link-archer-ax20", "Archer AX20 (AX1800)", "Dual-Band Wi-Fi 6 Router", "192.168.0.1", "http://tplinkwifi.net", "192.168.1.1", "admin", "admin", False, "TP-Link_XXXX", "Wi-Fi 6 (AX1800)", 10, "Equipped with quad-core processing and USB port for media servers."),
        ("tp-link-archer-ax50", "Archer AX50 (AX3000)", "Wi-Fi 6 Gigabit Router", "192.168.0.1", "http://tplinkwifi.net", "192.168.1.1", "admin", "admin", False, "TP-Link_XXXX", "Wi-Fi 6 (AX3000)", 10, "Intel Home Wi-Fi WAV654 chipset delivering ultra-low latency gaming."),
        ("tp-link-archer-ax72", "Archer AX72 (AX5400)", "Wi-Fi 6 Gigabit Router", "192.168.0.1", "http://tplinkwifi.net", "192.168.1.1", "admin", "admin", False, "TP-Link_XXXX", "Wi-Fi 6 (AX5400)", 10, "Contemporary slanted geometric grille for enhanced cooling and 6 antennas."),
        ("tp-link-archer-ax90", "Archer AX90 (AX6600)", "Tri-Band Wi-Fi 6 Router", "192.168.0.1", "http://tplinkwifi.net", "192.168.1.1", "admin", "admin", False, "TP-Link_XXXX", "Wi-Fi 6 (AX6600 Tri-Band)", 10, "Features a 2.5Gbps WAN/LAN port and 8 high-performance antennas."),
        ("tp-link-archer-ax11000", "Archer AX11000", "Tri-Band Gaming Wi-Fi 6", "192.168.0.1", "http://tplinkwifi.net", "192.168.1.1", "admin", "admin", False, "TP-Link_XXXX", "Wi-Fi 6 (AX11000 Tri-Band)", 10, "1.8GHz 64-bit quad-core CPU, 2.5G WAN port, 8 Gigabit LAN ports, and Game Accelerator."),
        ("tp-link-archer-gx90", "Archer GX90 (AX6600)", "Tri-Band Gaming Router", "192.168.0.1", "http://tplinkwifi.net", "192.168.1.1", "admin", "admin", False, "TP-Link_XXXX", "Wi-Fi 6 (AX6600 Gaming)", 10, "Dedicated 4.8Gbps Game Band with Game Center UI and 2.5G port."),
        ("tp-link-archer-be550", "Archer BE550 (BE9300)", "Tri-Band Wi-Fi 7 Router", "192.168.0.1", "http://tplinkwifi.net", "192.168.1.1", "admin", "admin", True, "TP-Link_XXXX", "Wi-Fi 7 (BE9300 Tri-Band)", 10, "Five 2.5G Ethernet ports with Multi-Link Operation (MLO) and 320MHz channels."),
        ("tp-link-archer-be800", "Archer BE800 (BE19000)", "Tri-Band Wi-Fi 7 Router", "192.168.0.1", "http://tplinkwifi.net", "192.168.1.1", "admin", "admin", True, "TP-Link_XXXX", "Wi-Fi 7 (BE19000)", 10, "Dual 10G ports (1x 10G SFP+ / RJ45 combo + 1x 10G RJ45) and LED screen."),
        ("tp-link-archer-be900", "Archer BE900 (BE24000)", "Quad-Band Wi-Fi 7 Router", "192.168.0.1", "http://tplinkwifi.net", "192.168.1.1", "admin", "admin", True, "TP-Link_XXXX", "Wi-Fi 7 (BE24000 Quad-Band)", 10, "16-stream quad-band router with customizable interactive touchscreen."),
        ("tp-link-archer-c7", "Archer C7 (AC1750)", "Dual-Band Gigabit Router", "192.168.0.1", "http://tplinkwifi.net", "192.168.1.1", "admin", "admin", False, "TP-Link_XXXX", "Wi-Fi 5 (AC1750 Dual-Band)", 8, "Legendary budget router with 3 external dual-band antennas and Qualcomm chipset."),
        ("tp-link-archer-a7", "Archer A7 (AC1750)", "Dual-Band Gigabit Router", "192.168.0.1", "http://tplinkwifi.net", "192.168.1.1", "admin", "admin", False, "TP-Link_XXXX", "Wi-Fi 5 (AC1750 Dual-Band)", 8, "Amazon Choice router with Alexa voice control and OneMesh compatibility."),
        ("tp-link-archer-c6", "Archer C6 (AC1200)", "MU-MIMO Gigabit Router", "192.168.0.1", "http://tplinkwifi.net", "192.168.1.1", "admin", "admin", False, "TP-Link_XXXX", "Wi-Fi 5 (AC1200)", 8, "Compact dual-band router with 4 external antennas and Access Point mode."),
        ("tp-link-archer-a6", "Archer A6 (AC1200)", "MU-MIMO Gigabit Router", "192.168.0.1", "http://tplinkwifi.net", "192.168.1.1", "admin", "admin", False, "TP-Link_XXXX", "Wi-Fi 5 (AC1200)", 8, "Cost-effective gigabit router supporting simultaneous 2.4GHz 300Mbps + 5GHz 867Mbps."),
        ("tp-link-archer-c80", "Archer C80 (AC1900)", "MU-MIMO Wi-Fi Router", "192.168.0.1", "http://tplinkwifi.net", "192.168.1.1", "admin", "admin", False, "TP-Link_XXXX", "Wi-Fi 5 (AC1900 3x3 MIMO)", 8, "3x3 MIMO technology allows transmitting and receiving data across three streams."),
        ("tp-link-archer-c2300", "Archer C2300 (AC2300)", "MU-MIMO Gigabit Router", "192.168.0.1", "http://tplinkwifi.net", "192.168.1.1", "admin", "admin", False, "TP-Link_XXXX", "Wi-Fi 5 (AC2300)", 8, "Broadcom 1.8GHz dual-core 64-bit CPU with RangeBoost and Smart Connect."),
        ("tp-link-archer-c5400x", "Archer C5400X", "Tri-Band Gaming Router", "192.168.0.1", "http://tplinkwifi.net", "192.168.1.1", "admin", "admin", False, "TP-Link_XXXX", "Wi-Fi 5 (AC5400 Tri-Band)", 8, "Aggressive red-and-black 8-antenna chassis with 8 Gigabit LAN ports."),
        ("tp-link-deco-x20", "Deco X20 (AX1800)", "Mesh Wi-Fi 6 System", "192.168.68.1", "http://tplinkdeco.net", "192.168.0.1", "TP-Link ID", "TP-Link ID", True, "Deco_XXXX", "Wi-Fi 6 (AX1800 Mesh)", 10, "Clean cylindrical mesh units with seamless AI-driven roaming."),
        ("tp-link-deco-x50", "Deco X50 (AX3000)", "Mesh Wi-Fi 6 System", "192.168.68.1", "http://tplinkdeco.net", "192.168.0.1", "TP-Link ID", "TP-Link ID", True, "Deco_XXXX", "Wi-Fi 6 (AX3000 Mesh)", 10, "3 Gigabit Ethernet ports per unit with wired Ethernet backhaul support."),
        ("tp-link-deco-x55", "Deco X55 (AX3000)", "Mesh Wi-Fi 6 System", "192.168.68.1", "http://tplinkdeco.net", "192.168.0.1", "TP-Link ID", "TP-Link ID", True, "Deco_XXXX", "Wi-Fi 6 (AX3000 Mesh)", 10, "Best-selling whole-home mesh pack with 160MHz channels and AI roaming."),
        ("tp-link-deco-x60", "Deco X60 (AX5400)", "Mesh Wi-Fi 6 System", "192.168.68.1", "http://tplinkdeco.net", "192.168.0.1", "TP-Link ID", "TP-Link ID", True, "Deco_XXXX", "Wi-Fi 6 (AX5400 6-Stream)", 10, "High-capacity mesh supporting up to 150 connected devices without congestion."),
        ("tp-link-deco-xe75", "Deco XE75 (AXE5400)", "Tri-Band Mesh Wi-Fi 6E", "192.168.68.1", "http://tplinkdeco.net", "192.168.0.1", "TP-Link ID", "TP-Link ID", True, "Deco_XXXX", "Wi-Fi 6E (AXE5400 Tri-Band)", 10, "Utilizes the uncluttered 6GHz spectrum for high-speed inter-node backhaul."),
        ("tp-link-deco-xe75-pro", "Deco XE75 Pro (AXE5400)", "Tri-Band Mesh with 2.5G", "192.168.68.1", "http://tplinkdeco.net", "192.168.0.1", "TP-Link ID", "TP-Link ID", True, "Deco_XXXX", "Wi-Fi 6E (AXE5400 with 2.5G)", 10, "Includes a 2.5Gbps WAN/LAN port on each node for multi-gigabit fiber connections."),
        ("tp-link-deco-be85", "Deco BE85 (BE22000)", "Tri-Band Mesh Wi-Fi 7", "192.168.68.1", "http://tplinkdeco.net", "192.168.0.1", "TP-Link ID", "TP-Link ID", True, "Deco_XXXX", "Wi-Fi 7 (BE22000 Mesh)", 10, "Flagship Wi-Fi 7 mesh with dual 10G ports and dual 2.5G ports."),
        ("tp-link-deco-m4", "Deco M4 (AC1200)", "Whole Home Mesh Wi-Fi", "192.168.68.1", "http://tplinkdeco.net", "192.168.0.1", "TP-Link ID", "TP-Link ID", True, "Deco_XXXX", "Wi-Fi 5 (AC1200)", 10, "Cost-effective AC1200 mesh system covering up to 4,000 square feet."),
        ("tp-link-deco-m5", "Deco M5 (AC1300)", "Whole Home Mesh Wi-Fi", "192.168.68.1", "http://tplinkdeco.net", "192.168.0.1", "TP-Link ID", "TP-Link ID", True, "Deco_XXXX", "Wi-Fi 5 (AC1300)", 10, "Low-profile puck design with built-in Trend Micro antivirus protection."),
        ("tp-link-omada-er605", "Omada ER605 (TL-R605)", "Multi-WAN VPN Router", "192.168.0.1", "N/A (Web GUI)", "192.168.1.1", "admin", "admin", False, "N/A (Wired)", "Gigabit Wired VPN Router", 10, "Enterprise Multi-WAN router supporting up to 3 WAN ports with IPsec/OpenVPN/WireGuard.")
    ]

    for item in tplink_specs:
        slug, name, hw_type, def_ip, web, fallback, user, pwd, sticker, ssid, standard, reset_sec, note = item
        models.append({
            "slug": slug,
            "brand": "TP-Link",
            "brand_slug": "tp-link",
            "model_name": name,
            "hardware_type": hw_type,
            "default_ip": def_ip,
            "web_domain": web,
            "fallback_ip": fallback,
            "default_username": user,
            "default_password": pwd,
            "password_on_sticker": sticker,
            "default_ssid_pattern": ssid,
            "wifi_standard": standard,
            "reset_instructions": f"With the unit powered ON, use a pin to press and hold the Reset button on the bottom/rear panel for {reset_sec} seconds until the System LED blinks rapidly. Release and wait 90 seconds for reboot.",
            "led_indicators": [
                {"name": "Power / Status", "normal": "Solid Green/White", "error": "Blinking Amber (Resetting/Booting) / Off", "desc": "Device power and initialization."},
                {"name": "Internet", "normal": "Solid Green", "error": "Solid Amber (No WAN IP) / Off (No physical link)", "desc": "Ethernet link to Internet modem."},
                {"name": "2.4 GHz", "normal": "Solid Green", "error": "Off (Radio disabled)", "desc": "2.4 GHz wireless broadcast."},
                {"name": "5 GHz", "normal": "Solid Green", "error": "Off (Radio disabled)", "desc": "5 GHz wireless broadcast."},
                {"name": "WPS", "normal": "Flashing slowly (Negotiating)", "error": "Solid Amber (Session timeout)", "desc": "Wi-Fi Protected Setup."}
            ],
            "mobile_app": "TP-Link Tether & Deco App",
            "companion_app_store_url": "https://apps.apple.com/app/tp-link-tether/id599496594",
            "official_manual_url": f"https://www.tp-link.com/support/download/{slug.replace('tp-link-', '')}/",
            "notes": note
        })

    # --------------------------------------------------------------------------
    # 3. ASUS (28 Models)
    # --------------------------------------------------------------------------
    asus_specs = [
        ("asus-rt-ax88u", "RT-AX88U (AX6000)", "Dual-Band Wi-Fi 6 Router", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "ASUS_XX / ASUS_XX_5G", "Wi-Fi 6 (AX6000 8-Port)", 10, "Equipped with 8 Gigabit LAN ports, 1.8GHz quad-core CPU, and AsusWRT-Merlin support."),
        ("asus-rt-ax86u", "RT-AX86U (AX5700)", "Dual-Band Wi-Fi 6 Gaming", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "ASUS_XX", "Wi-Fi 6 (AX5700 Gaming)", 10, "Dedicated 2.5G gaming port with Mobile Game Mode and AiProtection Pro."),
        ("asus-rt-ax86u-pro", "RT-AX86U Pro (AX5700)", "Dual-Band Wi-Fi 6 Gaming", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "ASUS_XX", "Wi-Fi 6 (AX5700 2.0GHz Quad-Core)", 10, "Upgraded 2.0GHz 64-bit quad-core CPU with RangeBoost+ technology."),
        ("asus-rt-ax88u-pro", "RT-AX88U Pro (AX6000)", "Dual-Band Wi-Fi 6 Router", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "ASUS_XX", "Wi-Fi 6 (Dual 2.5G AX6000)", 10, "Features dual 2.5G ports (WAN/LAN) and 2.0GHz quad-core processing power."),
        ("asus-rt-ax58u", "RT-AX58U (AX3000)", "Dual-Band Wi-Fi 6 Router", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "ASUS_XX", "Wi-Fi 6 (AX3000 AiMesh)", 10, "High-efficiency 160MHz channels with Trend Micro AiProtection lifetime subscription."),
        ("asus-rt-ax55", "RT-AX55 (AX1800)", "Dual-Band Wi-Fi 6 Router", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "ASUS_XX", "Wi-Fi 6 (AX1800 AiMesh)", 10, "Reliable Wi-Fi 6 entry point supporting AiMesh whole-home roaming."),
        ("asus-rt-ax53u", "RT-AX53U (AX1800)", "Wi-Fi 6 Router with USB", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "ASUS_XX", "Wi-Fi 6 (AX1800)", 10, "Includes USB port for 3G/4G cellular dongle backup connectivity."),
        ("asus-rt-ax68u", "RT-AX68U (AX2700)", "Dual-Band Wi-Fi 6 Router", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "ASUS_XX", "Wi-Fi 6 (AX2700 3x3)", 10, "Vertical upright styling with 3x3 MIMO spatial streams and VPN Fusion."),
        ("asus-rt-ax82u", "RT-AX82U (AX5400)", "Dual-Band Wi-Fi 6 Gaming", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "ASUS_XX", "Wi-Fi 6 (AX5400 Aura RGB)", 10, "Futuristic spaceship chassis with customizable ASUS Aura RGB lighting."),
        ("asus-rt-ax89x", "RT-AX89X (AX6000)", "Dual-Band Wi-Fi 6 Dual 10G", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "ASUS_XX", "Wi-Fi 6 (Dual 10G SFP+/Base-T)", 10, "Spider-like 8-antenna monster with dual 10G ports and 8 Gigabit LAN ports."),
        ("asus-rt-ax92u", "RT-AX92U (AX6100)", "Tri-Band Wi-Fi 6 AiMesh", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "ASUS_XX", "Wi-Fi 6 (AX6100 Tri-Band)", 10, "Tri-Band mesh router utilizing 4.8Gbps Wi-Fi 6 backhaul between nodes."),
        ("asus-rog-rapture-gt-ax11000", "ROG Rapture GT-AX11000", "Tri-Band Gaming Router", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "ROG_XX", "Wi-Fi 6 (AX11000 Tri-Band)", 10, "Triple-level game acceleration, 2.5G gaming port, and Game Radar ping diagnostic."),
        ("asus-rog-rapture-gt-ax11000-pro", "ROG Rapture GT-AX11000 Pro", "Tri-Band Gaming Flagship", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "ROG_XX", "Wi-Fi 6 (AX11000 10G Gaming)", 10, "Includes 10Gbps Ethernet port and 2.5Gbps port with 2.0GHz quad-core CPU."),
        ("asus-rog-rapture-gt-ax6000", "ROG Rapture GT-AX6000", "Dual-Band Wi-Fi 6 Gaming", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "ROG_XX", "Wi-Fi 6 (Dual 2.5G Gaming)", 10, "Iconic red-antenna gaming aesthetic with dual 2.5Gbps Ethernet interfaces."),
        ("asus-rog-rapture-gt-axe11000", "ROG Rapture GT-AXE11000", "Tri-Band Wi-Fi 6E Gaming", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "ROG_XX", "Wi-Fi 6E (AXE11000 6GHz)", 10, "World's first Wi-Fi 6E gaming router introducing the interference-free 6GHz band."),
        ("asus-rog-rapture-gt-axe16000", "ROG Rapture GT-AXE16000", "Quad-Band Wi-Fi 6E Gaming", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "ROG_XX", "Wi-Fi 6E (Quad-Band Dual 10G)", 10, "World's first quad-band Wi-Fi 6E router with dual 10G ports and mirrored top plate."),
        ("asus-rog-rapture-gt-be98", "ROG Rapture GT-BE98", "Quad-Band Wi-Fi 7 Gaming", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "ROG_XX", "Wi-Fi 7 (BE25000 Quad-Band)", 10, "Next-gen Wi-Fi 7 with dual 10G ports, four 2.5G ports, and 320MHz bandwidth."),
        ("asus-rog-rapture-gt6", "ROG Rapture GT6", "Tri-Band Mesh Gaming System", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "ROG_XX", "Wi-Fi 6 (AX10000 Mesh)", 10, "Dedicated mesh system tailored for latency-sensitive esports gaming."),
        ("asus-tuf-gaming-ax3000", "TUF Gaming AX3000", "Dual-Band Wi-Fi 6 Gaming", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "TUF_XX", "Wi-Fi 6 (AX3000 Gaming)", 10, "Military-grade durability certification with dedicated Gaming Port priority."),
        ("asus-tuf-gaming-ax4200", "TUF Gaming AX4200", "Dual-Band Wi-Fi 6 Gaming", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "TUF_XX", "Wi-Fi 6 (AX4200 2.5G)", 10, "Features 2.5Gbps WAN port and OpenNAT simple 3-step port forwarding."),
        ("asus-tuf-gaming-ax5400", "TUF Gaming AX5400", "Dual-Band Wi-Fi 6 Gaming", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "TUF_XX", "Wi-Fi 6 (AX5400 Gaming)", 10, "6-antenna configuration with link aggregation for WAN and LAN connections."),
        ("asus-zenwifi-xt8", "ZenWiFi XT8 (AX6600)", "Tri-Band Whole-Home Mesh", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "ASUS_XX", "Wi-Fi 6 (AX6600 Tri-Band Mesh)", 10, "Elegant white/charcoal pillars with 2.5G WAN and dedicated 4.8G backhaul."),
        ("asus-zenwifi-xt9", "ZenWiFi XT9 (AX7800)", "Tri-Band Whole-Home Mesh", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "ASUS_XX", "Wi-Fi 6 (AX7800 160MHz)", 10, "Expanded UNII-4 5.9GHz spectrum support with 160MHz high-speed channels."),
        ("asus-zenwifi-pro-xt12", "ZenWiFi Pro XT12", "Tri-Band Flagship Mesh", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "ASUS_XX", "Wi-Fi 6 (AX11000 Dual 2.5G)", 10, "Transparent top window revealing internal high-gain directional antennas."),
        ("asus-zenwifi-pro-et12", "ZenWiFi Pro ET12", "Tri-Band Wi-Fi 6E Mesh", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "ASUS_XX", "Wi-Fi 6E (AXE11000 Dual 2.5G)", 10, "Tri-Band 6E mesh with dual 2.5G ports and dedicated 6GHz inter-node links."),
        ("asus-zenwifi-bq16", "ZenWiFi BQ16", "Quad-Band Wi-Fi 7 Mesh", "192.168.50.1", "http://router.asus.com", "192.168.1.1", "admin", "admin", False, "ASUS_XX", "Wi-Fi 7 (BE30000 Quad-Band)", 10, "Quad-band Wi-Fi 7 mesh with dual 10G ports and up to 8,000 sq ft coverage."),
        ("asus-rt-ac68u", "RT-AC68U (AC1900)", "Classic Dual-Band Router", "192.168.1.1", "http://router.asus.com", "192.168.50.1", "admin", "admin", False, "ASUS_XX", "Wi-Fi 5 (AC1900 AiMesh)", 10, "The defining router of the Wi-Fi 5 era, pioneer of AsusWRT and AiMesh."),
        ("asus-rt-ac86u", "RT-AC86U (AC2900)", "Dual-Band Gaming Router", "192.168.1.1", "http://router.asus.com", "192.168.50.1", "admin", "admin", False, "ASUS_XX", "Wi-Fi 5 (AC2900 WTFast)", 10, "1.8GHz 64-bit dual core CPU with NitroQAM and WTFast game accelerator.")
    ]

    for item in asus_specs:
        slug, name, hw_type, def_ip, web, fallback, user, pwd, sticker, ssid, standard, reset_sec, note = item
        models.append({
            "slug": slug,
            "brand": "ASUS",
            "brand_slug": "asus",
            "model_name": name,
            "hardware_type": hw_type,
            "default_ip": def_ip,
            "web_domain": web,
            "fallback_ip": fallback,
            "default_username": user,
            "default_password": pwd,
            "password_on_sticker": sticker,
            "default_ssid_pattern": ssid,
            "wifi_standard": standard,
            "reset_instructions": f"While router is powered ON, press and hold the rear Reset button for {reset_sec} seconds until the Power LED starts blinking slowly. Release the button and wait 2 minutes for the factory nvram wipe.",
            "led_indicators": [
                {"name": "Power", "normal": "Solid Blue/White", "error": "Flashing slowly (Rescue mode / Factory reset)", "desc": "Hardware power status."},
                {"name": "WAN", "normal": "Solid White", "error": "Solid Red (No cable / No IP from ISP)", "desc": "Internet uplink."},
                {"name": "2.4 GHz", "normal": "Solid White", "error": "Off (Radio disabled)", "desc": "2.4 GHz wireless broadcast."},
                {"name": "5 GHz / 6 GHz", "normal": "Solid White", "error": "Off (Radio disabled / DFS wait)", "desc": "High frequency wireless bands."},
                {"name": "LAN 1-4", "normal": "Solid White", "error": "Off (Unconnected)", "desc": "Gigabit switch ports."}
            ],
            "mobile_app": "ASUS Router App",
            "companion_app_store_url": "https://apps.apple.com/app/asus-router/id1033764074",
            "official_manual_url": f"https://www.asus.com/networking-iot-servers/wifi-routers/all-series/{slug.replace('asus-', '')}/helpdesk_manual/",
            "notes": note
        })

    # --------------------------------------------------------------------------
    # 4. LINKSYS (20 Models)
    # --------------------------------------------------------------------------
    linksys_specs = [
        ("linksys-velop-micro-6-mesh-ln1301", "Velop Micro 6 Mesh (LN1301)", "Dual-Band Wi-Fi 6 Mesh", "192.168.1.1", "http://myrouter.local", "192.168.0.1", "admin", "admin", True, "LinksysXXXXX", "Wi-Fi 6 (AX3000)", 10, "Compact plug-and-play mesh router distributed through major broadband providers."),
        ("linksys-velop-pro-6e-mx6200", "Velop Pro 6E (MX6200)", "Cognitive Mesh Wi-Fi 6E", "192.168.1.1", "http://myrouter.local", "192.168.0.1", "admin", "admin", True, "LinksysXXXXX", "Wi-Fi 6E (AXE5400 Tri-Band)", 10, "Cognitive Mesh technology with clean teardrop chassis design."),
        ("linksys-velop-pro-7-mbe7000", "Velop Pro 7 (MBE7000)", "Cognitive Mesh Wi-Fi 7", "192.168.1.1", "http://myrouter.local", "192.168.0.1", "admin", "admin", True, "LinksysXXXXX", "Wi-Fi 7 (BE11000 Tri-Band)", 10, "Features 2.5G WAN and 4x 2.5G LAN ports with Cognitive Mesh optimization."),
        ("linksys-atlas-pro-6-mx5500", "Atlas Pro 6 (MX5500)", "Dual-Band Wi-Fi 6 Mesh", "192.168.1.1", "http://myrouter.local", "192.168.0.1", "admin", "admin", True, "LinksysXXXXX", "Wi-Fi 6 (AX5400)", 10, "Qualcomm Immersive Home 216 platform with 160MHz channels."),
        ("linksys-atlas-max-6e-mx8500", "Atlas Max 6E (MX8500)", "Tri-Band Wi-Fi 6E Mesh", "192.168.1.1", "http://myrouter.local", "192.168.0.1", "admin", "admin", True, "LinksysXXXXX", "Wi-Fi 6E (AXE8400)", 10, "Flagship Velop node with 5Gbps WAN port and 4 Gigabit Ethernet LAN ports."),
        ("linksys-velop-ax4200-mx4200", "Velop AX4200 (MX4200)", "Tri-Band Wi-Fi 6 Mesh", "192.168.1.1", "http://myrouter.local", "192.168.0.1", "admin", "admin", True, "LinksysXXXXX", "Wi-Fi 6 (AX4200 Tri-Band)", 10, "1.4GHz quad-core processor with USB 3.0 port and 3 Gigabit LAN ports."),
        ("linksys-velop-ax5300-mx5300", "Velop AX5300 (MX5300)", "Tri-Band Wi-Fi 6 Mesh", "192.168.1.1", "http://myrouter.local", "192.168.0.1", "admin", "admin", True, "LinksysXXXXX", "Wi-Fi 6 (AX5300 Tri-Band)", 10, "12-stream Wi-Fi 6 mesh system with 4x capacity for smart home automation."),
        ("linksys-velop-whw0303", "Velop Tri-Band (WHW0303)", "AC2200 Whole Home Mesh", "192.168.1.1", "http://myrouter.local", "192.168.0.1", "admin", "admin", True, "LinksysXXXXX", "Wi-Fi 5 (AC2200 Tri-Band)", 10, "The original modular mesh pillar with Dynamic Tri-Band backhaul."),
        ("linksys-hydra-pro-6e-mr7500", "Hydra Pro 6E (MR7500)", "Tri-Band Wi-Fi 6E Router", "192.168.1.1", "http://myrouter.local", "192.168.0.1", "admin", "admin", False, "LinksysXXXXX", "Wi-Fi 6E (AXE6600)", 10, "Standalone router with 5Gbps Multi-Gig WAN port and 4 external antennas."),
        ("linksys-hydra-6-mr2000", "Hydra 6 (MR2000)", "Dual-Band Wi-Fi 6 Router", "192.168.1.1", "http://myrouter.local", "192.168.0.1", "admin", "admin", False, "LinksysXXXXX", "Wi-Fi 6 (AX3000)", 10, "Compact traditional router form factor with Intelligent Mesh technology."),
        ("linksys-mr9600", "Max-Stream MR9600", "Dual-Band Wi-Fi 6 Router", "192.168.1.1", "http://myrouter.local", "192.168.0.1", "admin", "admin", False, "LinksysXXXXX", "Wi-Fi 6 (AX6000 8-Stream)", 10, "8-stream router with dual USB 3.0 ports and Intelligent Mesh."),
        ("linksys-mr9000", "Max-Stream MR9000", "Tri-Band AC3000 Router", "192.168.1.1", "http://myrouter.local", "192.168.0.1", "admin", "admin", False, "LinksysXXXXX", "Wi-Fi 5 (AC3000 Tri-Band)", 10, "Gaming and 4K streaming optimized with quad-core processor."),
        ("linksys-mr8300", "Max-Stream MR8300", "Tri-Band AC2200 Router", "192.168.1.1", "http://myrouter.local", "192.168.0.1", "admin", "admin", False, "LinksysXXXXX", "Wi-Fi 5 (AC2200 Tri-Band)", 10, "Mesh-enabled tri-band router capable of adding Velop nodes."),
        ("linksys-mr7350", "Max-Stream MR7350", "Dual-Band Wi-Fi 6 Router", "192.168.1.1", "http://myrouter.local", "192.168.0.1", "admin", "admin", False, "LinksysXXXXX", "Wi-Fi 6 (AX1800)", 10, "Entry-level Wi-Fi 6 router with USB 3.0 port and clean black design."),
        ("linksys-wrt54g", "Classic WRT54G", "Wireless-G Router", "192.168.1.1", "http://192.168.1.1", "192.168.0.1", "admin", "admin", False, "linksys", "802.11g (54 Mbps)", 30, "The most famous open-source router in history, father of OpenWrt."),
        ("linksys-wrt1900acs", "WRT1900ACS", "Dual-Band AC1900 Router", "192.168.1.1", "http://myrouter.local", "192.168.0.1", "admin", "admin", False, "LinksysXXXXX", "Wi-Fi 5 (AC1900 OpenWrt)", 10, "Iconic blue-and-black chassis with 1.6GHz dual-core CPU and eSATA port."),
        ("linksys-wrt3200acm", "WRT3200ACM", "Dual-Band AC3200 Router", "192.168.1.1", "http://myrouter.local", "192.168.0.1", "admin", "admin", False, "LinksysXXXXX", "Wi-Fi 5 (AC3200 Tri-Stream)", 10, "Tri-Stream 160MHz technology doubling 5GHz band bandwidth for OpenWrt."),
        ("linksys-wrt32x", "WRT32X", "Gaming Wi-Fi Router", "192.168.1.1", "http://myrouter.local", "192.168.0.1", "admin", "admin", False, "LinksysXXXXX", "Wi-Fi 5 (AC3200 Killer)", 10, "Engineered with Killer Prioritization Engine to reduce gaming ping on PCs."),
        ("linksys-ea7500", "Max-Stream EA7500", "Dual-Band AC1900 Router", "192.168.1.1", "http://myrouter.local", "192.168.0.1", "admin", "admin", False, "LinksysXXXXX", "Wi-Fi 5 (AC1900 MU-MIMO)", 10, "Next-Gen AC Wi-Fi featuring 3x3 AC with simultaneous data streaming."),
        ("linksys-ea8300", "Max-Stream EA8300", "Tri-Band AC2200 Router", "192.168.1.1", "http://myrouter.local", "192.168.0.1", "admin", "admin", False, "LinksysXXXXX", "Wi-Fi 5 (AC2200 Tri-Band)", 10, "Tri-Band speeds up to 2.2 Gbps with quad-core processor and airtime fairness.")
    ]

    for item in linksys_specs:
        slug, name, hw_type, def_ip, web, fallback, user, pwd, sticker, ssid, standard, reset_sec, note = item
        models.append({
            "slug": slug,
            "brand": "Linksys",
            "brand_slug": "linksys",
            "model_name": name,
            "hardware_type": hw_type,
            "default_ip": def_ip,
            "web_domain": web,
            "fallback_ip": fallback,
            "default_username": user,
            "default_password": pwd,
            "password_on_sticker": sticker,
            "default_ssid_pattern": ssid,
            "wifi_standard": standard,
            "reset_instructions": f"Locate the red Reset button on the back or bottom. Press and hold for {reset_sec} seconds until the top status light pulses red/amber. Release and wait 2 minutes.",
            "led_indicators": [
                {"name": "Top LED (Velop) / Power", "normal": "Solid Blue", "error": "Solid Red (No Internet) / Blinking Red (Out of range)", "desc": "Overall mesh node status."},
                {"name": "Internet", "normal": "Solid Green", "error": "Blinking Amber (Negotiating) / Off", "desc": "Ethernet WAN connection."},
                {"name": "WPS", "normal": "Blinking White (Pairing)", "error": "Amber (Pairing failed)", "desc": "Wi-Fi Protected Setup."}
            ],
            "mobile_app": "Linksys App",
            "companion_app_store_url": "https://apps.apple.com/app/linksys/id633514718",
            "official_manual_url": f"https://www.linksys.com/support-product?sku={slug.split('-')[-1].upper()}",
            "notes": note
        })

    # --------------------------------------------------------------------------
    # 5. UBIQUITI / UNIFI (18 Models)
    # --------------------------------------------------------------------------
    ubiquiti_specs = [
        ("ubiquiti-unifi-dream-machine-pro", "UniFi Dream Machine Pro (UDM-Pro)", "10G Enterprise Gateway & NVR", "192.168.1.1", "https://unifi.ui.com", "192.168.0.1", "UI Account / root", "UI Account / root", False, "N/A (Managed APs)", "10G SFP+ Enterprise Router", 10, "All-in-one 1U rackmount router with 3.5Gbps IDS/IPS and 3.5\" HDD bay for Protect video."),
        ("ubiquiti-unifi-dream-machine-se", "UniFi Dream Machine Special Edition (UDM-SE)", "2.5G PoE 10G Gateway", "192.168.1.1", "https://unifi.ui.com", "192.168.0.1", "UI Account / root", "UI Account / root", False, "N/A (Managed APs)", "10G SFP+ Enterprise Router with PoE", 10, "Includes 2.5GbE RJ45 WAN port, integrated 8-port PoE/PoE+ switch, and 128GB internal SSD."),
        ("ubiquiti-unifi-dream-machine", "UniFi Dream Machine (UDM)", "All-in-One Cloud Gateway", "192.168.1.1", "https://unifi.ui.com", "192.168.0.1", "UI Account / root", "UI Account / root", False, "UniFi-XX", "Wi-Fi 5 (AC2200 4x4 MU-MIMO)", 10, "Pill-shaped all-in-one desktop gateway integrating AP, 4-port switch, and UniFi Network controller."),
        ("ubiquiti-unifi-dream-router", "UniFi Dream Router (UDR)", "Wi-Fi 6 PoE Gateway", "192.168.1.1", "https://unifi.ui.com", "192.168.0.1", "UI Account / root", "UI Account / root", False, "UniFi-XX", "Wi-Fi 6 (4x4 MIMO UDR)", 10, "Modern pill gateway with 4-stream Wi-Fi 6, LCM color status screen, and 2 PoE output ports."),
        ("ubiquiti-unifi-cloud-gateway-ultra", "UniFi Cloud Gateway Ultra (UCG-Ultra)", "Compact Multi-WAN Gateway", "192.168.1.1", "https://unifi.ui.com", "192.168.0.1", "UI Account / root", "UI Account / root", False, "N/A (Requires UniFi AP)", "Multi-WAN 2.5G Gigabit Router", 10, "Pocket-sized 1Gbps routing gateway with full IDS/IPS, 2.5G WAN, and 0.96\" status display."),
        ("ubiquiti-unifi-cloud-gateway-max", "UniFi Cloud Gateway Max (UCG-Max)", "2.5GbE Multi-WAN Gateway", "192.168.1.1", "https://unifi.ui.com", "192.168.0.1", "UI Account / root", "UI Account / root", False, "N/A (Requires UniFi AP)", "Full 2.5GbE Gateway with NVMe Storage", 10, "Features 2.5Gbps routing on all ports with optional M.2 NVMe SSD for UniFi Protect video recording."),
        ("ubiquiti-unifi-express", "UniFi Express (UX)", "Ultra-Compact Gateway & AP", "192.168.1.1", "https://unifi.ui.com", "192.168.0.1", "UI Account / root", "UI Account / root", False, "UniFi-XX", "Wi-Fi 6 Cloud Gateway", 10, "Palm-sized complete UniFi OS console running Network application with integrated Wi-Fi 6 AP."),
        ("ubiquiti-unifi-security-gateway", "UniFi Security Gateway (USG-3P)", "Enterprise Gateway Router", "192.168.1.1", "https://192.168.1.1", "192.168.0.1", "root", "ubnt", False, "N/A (Requires AP)", "Gigabit Security Gateway", 10, "The classic silver 3-port desktop gateway managing VLANs, site-to-site VPNs, and DPI."),
        ("ubiquiti-unifi-security-gateway-pro", "UniFi Security Gateway Pro (USG-PRO-4)", "Dual WAN 1U Gateway", "192.168.1.1", "https://192.168.1.1", "192.168.0.1", "root", "ubnt", False, "N/A (Requires AP)", "Gigabit Enterprise SFP Gateway", 10, "1U rackmount security gateway with dual RJ45/SFP combination WAN interfaces."),
        ("ubiquiti-unifi-dream-wall", "UniFi Dream Wall (UDW)", "Wall-Mount Multi-Gigabit Console", "192.168.1.1", "https://unifi.ui.com", "192.168.0.1", "UI Account / root", "UI Account / root", False, "UniFi-XX", "Wi-Fi 6 Wall-Mount Enterprise", 10, "Surface-mounted appliance with Wi-Fi 6 AP, 17-port PoE switch, dual PSU, and 4.7\" touchscreen."),
        ("ubiquiti-edgerouter-x", "EdgeRouter X (ER-X)", "5-Port Gigabit Router", "192.168.1.1", "https://192.168.1.1", "192.168.2.1", "ubnt", "ubnt", False, "N/A (Wired)", "Gigabit EdgeOS Router", 10, "Ultra-popular 5-port gigabit router running EdgeOS with passive PoE passthrough support."),
        ("ubiquiti-edgerouter-x-sfp", "EdgeRouter X SFP (ER-X-SFP)", "Gigabit Router with SFP", "192.168.1.1", "https://192.168.1.1", "192.168.2.1", "ubnt", "ubnt", False, "N/A (Wired)", "Gigabit PoE EdgeOS Router", 10, "5 Gigabit ports with 24V passive PoE output on all ports plus 1 Gigabit SFP cage."),
        ("ubiquiti-edgerouter-4", "EdgeRouter 4 (ER-4)", "4-Port Gigabit Router", "192.168.1.1", "https://192.168.1.1", "192.168.2.1", "ubnt", "ubnt", False, "N/A (Wired)", "High-Performance EdgeOS Router", 10, "Delivers 3.4 million packets per second routing with 1GHz quad-core CPU and SFP port."),
        ("ubiquiti-edgerouter-6p", "EdgeRouter 6P (ER-6P)", "6-Port PoE Gigabit Router", "192.168.1.1", "https://192.168.1.1", "192.168.2.1", "ubnt", "ubnt", False, "N/A (Wired)", "Gigabit EdgeOS Router", 10, "6 Gigabit ports with 24V configurable passive PoE and 3.4M pps routing engine."),
        ("ubiquiti-edgerouter-12", "EdgeRouter 12 (ER-12)", "10-Port Gigabit Router with SFP", "192.168.1.1", "https://192.168.1.1", "192.168.2.1", "ubnt", "ubnt", False, "N/A (Wired)", "10-Port Gigabit Enterprise Router", 10, "10 Gigabit RJ45 ports with integrated layer 2 switch and dual SFP 1G cages."),
        ("ubiquiti-edgerouter-infinity", "EdgeRouter Infinity (ER-8-XG)", "8-Port 10G SFP+ Router", "192.168.1.1", "https://192.168.1.1", "192.168.2.1", "ubnt", "ubnt", False, "N/A (Wired)", "8-Port 10G SFP+ Core Router", 10, "8 10G SFP+ ports with 80 Gbps aggregate throughput and redundant hot-swappable power supplies."),
        ("ubiquiti-amplifi-alien", "AmpliFi Alien (AFi-ALN)", "Wi-Fi 6 Gaming Mesh Router", "192.168.112.1", "http://amplifi.lan", "192.168.1.1", "admin", "admin", False, "AmpliFi-XX", "Wi-Fi 6 (AX7600 Mesh)", 10, "Sleek matte-black vertical cylinder with vibrant vertical touchscreen and green neon glow ring."),
        ("ubiquiti-amplifi-hd", "AmpliFi HD (AFi-R)", "High-Density Home Wi-Fi", "192.168.112.1", "http://amplifi.lan", "192.168.1.1", "admin", "admin", False, "AmpliFi-XX", "Wi-Fi 5 (AC1750 Mesh)", 10, "Minimalist white cube featuring a smart round color touch LCD displaying clock and real-time speed.")
    ]

    for item in ubiquiti_specs:
        slug, name, hw_type, def_ip, web, fallback, user, pwd, sticker, ssid, standard, reset_sec, note = item
        models.append({
            "slug": slug,
            "brand": "Ubiquiti",
            "brand_slug": "ubiquiti",
            "model_name": name,
            "hardware_type": hw_type,
            "default_ip": def_ip,
            "web_domain": web,
            "fallback_ip": fallback,
            "default_username": user,
            "default_password": pwd,
            "password_on_sticker": sticker,
            "default_ssid_pattern": ssid,
            "wifi_standard": standard,
            "reset_instructions": f"With device powered ON, use a pin to hold the recessed Reset button for {reset_sec} seconds until the LED ring or LCD screen announces 'Restoring to Factory Defaults'. Release and wait 3 minutes.",
            "led_indicators": [
                {"name": "Status Ring / LCD", "normal": "Solid White (Ready to Adopt) / Solid Blue (Adopted & Normal)", "error": "Flashing White/Blue (Upgrading firmware) / Off", "desc": "UniFi console state."},
                {"name": "SFP+ Link / Speed", "normal": "Solid White (10G) / Solid Green (1G)", "error": "Off (No physical link)", "desc": "Fiber transceiver connection."},
                {"name": "RJ45 Ethernet", "normal": "Amber (1G/2.5G) / Green (Active)", "error": "Off", "desc": "Switch port status."}
            ],
            "mobile_app": "UniFi Network App",
            "companion_app_store_url": "https://apps.apple.com/app/unifi-network/id1057750338",
            "official_manual_url": "https://help.ui.com",
            "notes": note
        })

    # --------------------------------------------------------------------------
    # 6. MIKROTIK (16 Models)
    # --------------------------------------------------------------------------
    mikrotik_specs = [
        ("mikrotik-hex-rb750gr3", "hEX (RB750Gr3)", "5-Port Gigabit Router", "192.168.88.1", "http://router.lan", "192.168.1.1", "admin", "[empty]", False, "N/A (Wired)", "Gigabit RouterOS v7 Router", 5, "Dual-core 880MHz CPU with hardware IPsec encryption acceleration and microSD slot."),
        ("mikrotik-hex-s-rb760igs", "hEX S (RB760iGS)", "Gigabit Router with SFP", "192.168.88.1", "http://router.lan", "192.168.1.1", "admin", "[empty]", False, "N/A (Wired)", "Gigabit RouterOS with SFP", 5, "Includes SFP cage for optical fiber link and PoE out on port 5."),
        ("mikrotik-hex-poe-rb960pgs", "hEX PoE (RB960PGS)", "5-Port Gigabit PoE Router", "192.168.88.1", "http://router.lan", "192.168.1.1", "admin", "[empty]", False, "N/A (Wired)", "Gigabit PoE RouterOS", 5, "Ports 2-5 can power other PoE capable devices with the same voltage as applied to the unit."),
        ("mikrotik-hap-ax2", "hAP ax2 (C52iG-5HaxD2HaxD-TC)", "Dual-Band Wi-Fi 6 Router", "192.168.88.1", "http://router.lan", "192.168.1.1", "admin", "Unique sticker password", True, "MikroTik-XXXXXX", "Wi-Fi 6 (AX1800 Quad-Core)", 5, "Modern ARM 64-bit quad-core 864MHz CPU running RouterOS v7 with WPA3-PSK."),
        ("mikrotik-hap-ax3", "hAP ax3 (C53UiG+5HPaxD2HPaxD)", "Wi-Fi 6 Router with 2.5G", "192.168.88.1", "http://router.lan", "192.168.1.1", "admin", "Unique sticker password", True, "MikroTik-XXXXXX", "Wi-Fi 6 (AX1800 with 2.5GbE)", 5, "High-gain external antennas with 2.5G Ethernet port and 1GB RAM for container hosting."),
        ("mikrotik-hap-ac2", "hAP ac2 (RBD52G-5HacD2HnD-TC)", "Dual-Band Gigabit Router", "192.168.88.1", "http://router.lan", "192.168.1.1", "admin", "[empty]", False, "MikroTik-XXXXXX", "Wi-Fi 5 (AC1200 Gigabit)", 5, "Quad-core 716MHz IPQ-4018 CPU with 5 Gigabit ports and versatile tower/desktop case."),
        ("mikrotik-hap-ac3", "hAP ac3 (RBD53iG-5HacD2HnD)", "High-Gain Wi-Fi 5 Router", "192.168.88.1", "http://router.lan", "192.168.1.1", "admin", "[empty]", False, "MikroTik-XXXXXX", "Wi-Fi 5 (AC1200 High-Gain)", 5, "Detachable high-gain SMA antennas with PoE out support and full-size USB port."),
        ("mikrotik-hap-lite", "hAP lite (RB941-2nD)", "Compact 2.4GHz Home AP", "192.168.88.1", "http://router.lan", "192.168.1.1", "admin", "[empty]", False, "MikroTik-XXXXXX", "802.11b/g/n (300Mbps)", 5, "Micro-USB powered compact router supporting WPS button triggering and bandwidth throttling."),
        ("mikrotik-rb4011", "RB4011iGS+5HacQ2HnD-IN", "10x Gigabit + 10G SFP+ Router", "192.168.88.1", "http://router.lan", "192.168.1.1", "admin", "[empty]", False, "MikroTik-XXXXXX", "Wi-Fi 5 + 10G SFP+ Core", 5, "Quad-core 1.4GHz Cortex-A15 CPU with heavy-duty metal matte chassis and 10Gbps SFP+."),
        ("mikrotik-rb5009", "RB5009UG+S+IN", "Heavy-Duty Home Lab Router", "192.168.88.1", "http://router.lan", "192.168.1.1", "admin", "[empty]", False, "N/A (Wired)", "Multi-Gig 1G/2.5G/10G RouterOS", 5, "Ultimate home lab router with 7x 1G ports, 1x 2.5G port, and 1x 10G SFP+ cage."),
        ("mikrotik-l009uigs", "L009UiGS-2HaxD-IN", "Dual-Band Wi-Fi 6 Router", "192.168.88.1", "http://router.lan", "192.168.1.1", "admin", "[empty]", False, "MikroTik-XXXXXX", "Wi-Fi 6 (2.4GHz High Power) + SFP", 5, "Successor to the legendary RB2011 with ARM dual-core 800MHz CPU and 2.5G SFP cage."),
        ("mikrotik-ccr2004", "CCR2004-16G-2S+", "16-Port Cloud Core Router", "192.168.88.1", "http://router.lan", "192.168.1.1", "admin", "[empty]", False, "N/A (Wired)", "16-Port Gigabit + Dual 10G SFP+", 5, "Single-core performance king featuring Annapurna Labs Alpine v2 CPU with 4x 64-bit ARM cores."),
        ("mikrotik-chateau-5g-ax", "Chateau 5G ax", "5G Home Gateway Wi-Fi 6", "192.168.88.1", "http://router.lan", "192.168.1.1", "admin", "Unique sticker password", True, "MikroTik-XXXXXX", "Wi-Fi 6 (AX1800 5G/LTE)", 5, "Integrated Sub-6GHz 5G modem with 4x4 MIMO and Wi-Fi 6 for ultra-fast wireless broadband."),
        ("mikrotik-chateau-lte12", "Chateau LTE12", "Cat12 LTE Home Gateway", "192.168.88.1", "http://router.lan", "192.168.1.1", "admin", "Unique sticker password", True, "MikroTik-XXXXXX", "Wi-Fi 5 (AC1200 Cat12 LTE)", 5, "Carrier aggregation Cat 12 LTE modem reaching speeds up to 600 Mbps on 4G cellular networks."),
        ("mikrotik-crs305", "Cloud Router Switch (CRS305-1G-4S+IN)", "4-Port 10G SFP+ Switch/Router", "192.168.88.1", "http://router.lan", "192.168.1.1", "admin", "[empty]", False, "N/A (Wired)", "4x 10Gbps SFP+ Dual Boot RouterOS", 5, "Dual Boot SwOS/RouterOS compact silent fanless switch with 4 optical 10G SFP+ cages."),
        ("mikrotik-rb3011", "RouterBOARD 3011UiAS-RM", "10-Port Gigabit Rackmount", "192.168.88.1", "http://router.lan", "192.168.1.1", "admin", "[empty]", False, "N/A (Wired)", "1U Rackmount RouterOS with LCD", 5, "10 Gigabit ports divided into two switch groups with touchscreen LCD and USB 3.0.")
    ]

    for item in mikrotik_specs:
        slug, name, hw_type, def_ip, web, fallback, user, pwd, sticker, ssid, standard, reset_sec, note = item
        models.append({
            "slug": slug,
            "brand": "MikroTik",
            "brand_slug": "mikrotik",
            "model_name": name,
            "hardware_type": hw_type,
            "default_ip": def_ip,
            "web_domain": web,
            "fallback_ip": fallback,
            "default_username": user,
            "default_password": pwd,
            "password_on_sticker": sticker,
            "default_ssid_pattern": ssid,
            "wifi_standard": standard,
            "reset_instructions": f"Unplug power. Hold the Reset button down while inserting the power plug. Keep holding for {reset_sec} seconds until the ACT LED starts flashing. Release immediately to reset RouterOS configuration to default 192.168.88.1.",
            "led_indicators": [
                {"name": "USR / ACT", "normal": "Blinking (Kernel boot) / Solid (Ready)", "error": "Rapid continuous flashing (Netinstall mode)", "desc": "RouterOS operating status."},
                {"name": "Ethernet 1-5", "normal": "Solid Green (Link active)", "error": "Off (No carrier detected)", "desc": "Port connection status."},
                {"name": "SFP+", "normal": "Solid Green (Optical link up)", "error": "Off", "desc": "Transceiver status."}
            ],
            "mobile_app": "MikroTik App (WinBox Mobile)",
            "companion_app_store_url": "https://apps.apple.com/app/mikrotik/id1323064830",
            "official_manual_url": f"https://help.mikrotik.com/docs/display/UM/{slug.split('-')[-1].upper()}",
            "notes": note
        })

    # --------------------------------------------------------------------------
    # 7. D-LINK (16 Models)
    # --------------------------------------------------------------------------
    dlink_specs = [
        ("d-link-eagle-pro-ai-r15", "EAGLE PRO AI AX1500 (R15)", "Smart Wi-Fi 6 Router", "192.168.0.1", "http://dlinkrouter.local", "192.168.1.1", "Admin", "[empty or sticker password]", True, "dlink-XXXX", "Wi-Fi 6 (AX1500 AI)", 10, "AI-driven Wi-Fi and traffic optimizer with clean feather-white casing."),
        ("d-link-eagle-pro-ai-r32", "EAGLE PRO AI AX3200 (R32)", "Wi-Fi 6 Gigabit Router", "192.168.0.1", "http://dlinkrouter.local", "192.168.1.1", "Admin", "[empty or sticker password]", True, "dlink-XXXX", "Wi-Fi 6 (AX3200 4-Stream)", 10, "4-stream Wi-Fi 6 router with AI Parental Control and AI Assistant reports."),
        ("d-link-exo-dir-x5460", "EXO AX5400 (DIR-X5460)", "6-Stream Wi-Fi 6 Router", "192.168.0.1", "http://dlinkrouter.local", "192.168.1.1", "Admin", "password", True, "dlink-XXXX", "Wi-Fi 6 (AX5400 6-Stream)", 10, "Triple-core 1.5GHz CPU with 6 external high-gain antennas and USB 3.0."),
        ("d-link-exo-dir-x1860", "EXO AX1800 (DIR-X1860)", "Dual-Band Wi-Fi 6 Router", "192.168.0.1", "http://dlinkrouter.local", "192.168.1.1", "Admin", "password", True, "dlink-XXXX", "Wi-Fi 6 (AX1800)", 10, "Dual-band Wi-Fi 6 router with OFDMA and MU-MIMO for smooth 4K streaming."),
        ("d-link-exo-dir-x1560", "EXO AX1500 (DIR-X1560)", "Dual-Band Wi-Fi 6 Router", "192.168.0.1", "http://dlinkrouter.local", "192.168.1.1", "Admin", "password", True, "dlink-XXXX", "Wi-Fi 6 (AX1500)", 10, "Entry-level Wi-Fi 6 gigabit router with voice control via Google Assistant and Alexa."),
        ("d-link-dir-882", "DIR-882 (AC2600)", "MU-MIMO Gigabit Router", "192.168.0.1", "http://dlinkrouter.local", "192.168.1.1", "Admin", "[empty]", False, "dlink-XXXX", "Wi-Fi 5 (AC2600 4x4)", 10, "Dual-core processor with SmartBeam technology directing signals to connected devices."),
        ("d-link-dir-878", "DIR-878 (AC1900)", "High-Power Gigabit Router", "192.168.0.1", "http://dlinkrouter.local", "192.168.1.1", "Admin", "[empty]", False, "dlink-XXXX", "Wi-Fi 5 (AC1900 3x3)", 10, "High-power amplifiers with 4 high-gain antennas for large home coverage."),
        ("d-link-dir-867", "DIR-867 (AC1750)", "Dual-Band Gigabit Router", "192.168.0.1", "http://dlinkrouter.local", "192.168.1.1", "Admin", "[empty]", False, "dlink-XXXX", "Wi-Fi 5 (AC1750)", 10, "Cost-effective gigabit router with Smart Connect automatically steering bands."),
        ("d-link-dir-842", "DIR-842 (AC1200)", "Wave 2 Gigabit Router", "192.168.0.1", "http://dlinkrouter.local", "192.168.1.1", "Admin", "[empty]", False, "dlink-XXXX", "Wi-Fi 5 (AC1200)", 10, "Affordable dual-band gigabit router for apartments and small businesses."),
        ("d-link-dir-825", "DIR-825 (AC1200)", "High-Gain Gigabit Router", "192.168.0.1", "http://dlinkrouter.local", "192.168.1.1", "Admin", "[empty]", False, "dlink-XXXX", "Wi-Fi 5 (AC1200 High Gain)", 10, "Widely deployed ISP router across international markets with USB media port."),
        ("d-link-dir-615", "DIR-615", "Classic Wireless-N Router", "192.168.0.1", "http://192.168.0.1", "192.168.1.1", "Admin", "[empty]", False, "dlink", "802.11n (300Mbps)", 10, "The timeless 300Mbps Wireless-N router found in millions of homes worldwide."),
        ("d-link-dir-600", "DIR-600", "Wireless 150 4-Port Router", "192.168.0.1", "http://192.168.0.1", "192.168.1.1", "Admin", "[empty]", False, "dlink", "802.11n (150Mbps)", 10, "Classic compact single-antenna wireless home broadband router."),
        ("d-link-dir-850l", "DIR-850L", "Cloud Gigabit Router", "192.168.0.1", "http://dlinkrouter.local", "192.168.1.1", "Admin", "[empty]", False, "dlink-XXXX", "Wi-Fi 5 (AC1200 Cylindrical)", 10, "Distinctive glossy black cylindrical tower design with mydlink cloud management."),
        ("d-link-covr-x1870", "COVR AX1800 (COVR-X1870)", "Mesh Wi-Fi 6 System", "192.168.0.1", "http://covr.local", "192.168.1.1", "Admin", "Sticker password", True, "COVR-XXXX", "Wi-Fi 6 (AX1800 Mesh)", 10, "Whole-home mesh system with Smart Roaming and Smart Steering."),
        ("d-link-covr-1100", "COVR AC1200 (COVR-1100)", "EasyMesh Certified System", "192.168.0.1", "http://covr.local", "192.168.1.1", "Admin", "Sticker password", True, "COVR-XXXX", "Wi-Fi 5 (AC1200 EasyMesh)", 10, "Official Wi-Fi Certified EasyMesh standard compliant mesh cubes."),
        ("d-link-dwr-960", "DWR-960", "LTE Cat7 Wi-Fi AC1200 Router", "192.168.0.1", "http://192.168.0.1", "192.168.1.1", "admin", "admin", True, "dlink-XXXX", "Wi-Fi 5 + LTE Cat 7", 10, "Integrated 4G LTE Cat 7 cellular router with dual-SIM slots and gigabit failover.")
    ]

    for item in dlink_specs:
        slug, name, hw_type, def_ip, web, fallback, user, pwd, sticker, ssid, standard, reset_sec, note = item
        models.append({
            "slug": slug,
            "brand": "D-Link",
            "brand_slug": "d-link",
            "model_name": name,
            "hardware_type": hw_type,
            "default_ip": def_ip,
            "web_domain": web,
            "fallback_ip": fallback,
            "default_username": user,
            "default_password": pwd,
            "password_on_sticker": sticker,
            "default_ssid_pattern": ssid,
            "wifi_standard": standard,
            "reset_instructions": f"With the router powered ON, use an unfolded paperclip to press and hold the recessed Reset button on the bottom or rear for {reset_sec} seconds until the Power light turns orange/amber. Release and wait 1 minute.",
            "led_indicators": [
                {"name": "Power", "normal": "Solid White/Green", "error": "Solid Orange (Booting/POST failed) / Blinking Orange", "desc": "Hardware power."},
                {"name": "Internet", "normal": "Solid White/Green", "error": "Solid Orange (No Internet access) / Off", "desc": "WAN broadband connection."},
                {"name": "2.4 GHz / 5 GHz", "normal": "Solid White/Green", "error": "Off", "desc": "Wireless broadcast state."}
            ],
            "mobile_app": "D-Link Wi-Fi App",
            "companion_app_store_url": "https://apps.apple.com/app/d-link-wi-fi/id1438965610",
            "official_manual_url": "https://support.dlink.com",
            "notes": note
        })

    # --------------------------------------------------------------------------
    # 8. CISCO & MERAKI (12 Models)
    # --------------------------------------------------------------------------
    cisco_specs = [
        ("cisco-business-rv340", "Cisco Business RV340", "Dual WAN Gigabit VPN Router", "192.168.1.1", "https://192.168.1.1", "192.168.1.254", "cisco", "cisco", False, "N/A (Wired)", "Dual WAN Gigabit Security Gateway", 15, "Dual Gigabit Ethernet WAN ports with load balancing, hardware IPsec VPN, and Web Filtering."),
        ("cisco-business-rv345", "Cisco Business RV345", "Dual WAN 16-Port VPN Router", "192.168.1.1", "https://192.168.1.1", "192.168.1.254", "cisco", "cisco", False, "N/A (Wired)", "Dual WAN 16-Port Gigabit Gateway", 15, "Includes 16 Gigabit LAN ports and dual WAN ports for small-to-medium enterprise setups."),
        ("cisco-business-rv260", "Cisco Business RV260", "Gigabit VPN Router with SFP", "192.168.1.1", "https://192.168.1.1", "192.168.1.254", "cisco", "cisco", False, "N/A (Wired)", "Gigabit SFP VPN Security Router", 15, "Combination RJ45/SFP WAN port with dual-core CPU and flexible web management GUI."),
        ("cisco-business-rv160", "Cisco Business RV160", "Gigabit VPN Security Router", "192.168.1.1", "https://192.168.1.1", "192.168.1.254", "cisco", "cisco", False, "N/A (Wired)", "Gigabit VPN Small Business Router", 15, "4 Gigabit LAN ports with IPsec/PPTP/OpenVPN client-to-gateway remote worker tunnels."),
        ("cisco-business-rv130", "Cisco Business RV130", "Multifunction VPN Router", "192.168.1.1", "https://192.168.1.1", "192.168.1.254", "cisco", "cisco", False, "N/A (Wired)", "Gigabit Small Business VPN Router", 15, "Built-in 4-port Gigabit switch with Stateful Packet Inspection (SPI) firewall."),
        ("cisco-business-rv042", "Cisco Business RV042", "Dual WAN 4-Port VPN Router", "192.168.1.1", "http://192.168.1.1", "10.0.0.1", "admin", "admin", False, "N/A (Wired)", "10/100 Dual WAN Business Router", 30, "The classic enterprise branch router supporting 50 IPsec QuickVPN tunnels."),
        ("cisco-meraki-go-gx20", "Cisco Meraki Go GX20", "Cloud Managed Security Gateway", "192.168.128.1", "https://meraki-go.com", "192.168.1.1", "admin (Meraki Account)", "admin", False, "N/A (Managed via Meraki Go App)", "Cloud Managed Router Firewall", 10, "Cloud-managed security gateway with stateful firewall and automated DNS security by Cisco Umbrella."),
        ("cisco-meraki-go-gx50", "Cisco Meraki Go GX50", "High-Throughput Router Firewall", "192.168.128.1", "https://meraki-go.com", "192.168.1.1", "admin (Meraki Account)", "admin", False, "N/A (Managed via Meraki Go App)", "500Mbps Security Router Gateway", 10, "500+ Mbps stateful firewall throughput with client VPN and USB cellular failover."),
        ("cisco-catalyst-1000", "Cisco Catalyst 1000-8T-2G-L", "Enterprise Switch Router", "192.168.1.254", "http://192.168.1.254", "10.0.0.1", "cisco", "cisco", False, "N/A (Wired)", "Enterprise Managed Layer 2/3 Switch", 10, "Classic Cisco IOS managed hardware with intuitive on-box web UI for small networks."),
        ("cisco-isr-1100", "Cisco ISR 1100 (C1111-8P)", "Integrated Services Router", "192.168.1.1", "https://192.168.1.1", "10.0.0.1", "cisco", "cisco", False, "N/A (Wired)", "Cisco IOS XE Enterprise Router", 15, "Combines WAN, security, and 8-port PoE LAN in a compact fanless platform."),
        ("cisco-isr-4331", "Cisco ISR 4331", "Enterprise Modular Router", "10.0.0.1", "https://10.0.0.1", "192.168.1.1", "cisco", "cisco", False, "N/A (Wired)", "Enterprise ISR 4000 Modular Router", 15, "100Mbps to 300Mbps aggregate throughput with internal service module slots."),
        ("cisco-c921-4p", "Cisco C921-4P", "Gigabit Security Router", "192.168.1.1", "https://192.168.1.1", "10.0.0.1", "cisco", "cisco", False, "N/A (Wired)", "Gigabit Ethernet Security Router", 15, "Dual Gigabit Ethernet WAN ports with 4-port Gigabit managed switch and LTE support.")
    ]

    for item in cisco_specs:
        slug, name, hw_type, def_ip, web, fallback, user, pwd, sticker, ssid, standard, reset_sec, note = item
        models.append({
            "slug": slug,
            "brand": "Cisco",
            "brand_slug": "cisco",
            "model_name": name,
            "hardware_type": hw_type,
            "default_ip": def_ip,
            "web_domain": web,
            "fallback_ip": fallback,
            "default_username": user,
            "default_password": pwd,
            "password_on_sticker": sticker,
            "default_ssid_pattern": ssid,
            "wifi_standard": standard,
            "reset_instructions": f"Press and hold the Reset button with a paperclip for {reset_sec} seconds until the DIAG LED flashes. The unit will wipe all NVRAM startup configurations and restore factory defaults.",
            "led_indicators": [
                {"name": "Power / System", "normal": "Solid Green", "error": "Solid Amber (Self-test fail) / Flashing Amber (Booting)", "desc": "Hardware system status."},
                {"name": "WAN", "normal": "Solid Green (1G link)", "error": "Amber (10/100 link) / Off", "desc": "Uplink interface."},
                {"name": "VPN", "normal": "Solid Green (Tunnel active)", "error": "Off (No tunnels established)", "desc": "Hardware IPsec/SSL VPN state."}
            ],
            "mobile_app": "Cisco Business Dashboard / Meraki Go App",
            "companion_app_store_url": "https://apps.apple.com/app/cisco-business-dashboard/id1453229871",
            "official_manual_url": "https://www.cisco.com/c/en/us/support/",
            "notes": note
        })

    # --------------------------------------------------------------------------
    # 9. SYNOLOGY (6 Models)
    # --------------------------------------------------------------------------
    synology_specs = [
        ("synology-rt6600ax", "Synology RT6600ax", "Tri-Band Wi-Fi 6 Router", "192.168.1.1", "http://router.synology.com", "192.168.0.1", "admin (created on setup)", "admin (created on setup)", False, "Synology_XXXX", "Wi-Fi 6 (Tri-Band AX6600)", 10, "Flagship SRM 1.3 router with 2.5GbE Multi-Gig port, up to 5 separate VLANs, and Safe Access."),
        ("synology-rt2600ac", "Synology RT2600ac", "Dual-Band AC2600 Router", "192.168.1.1", "http://router.synology.com", "192.168.0.1", "admin (created on setup)", "admin (created on setup)", False, "Synology_XXXX", "Wi-Fi 5 (AC2600 4x4 MU-MIMO)", 10, "1.7GHz dual-core CPU with Threat Prevention intrusion prevention system (IPS) and Dual WAN."),
        ("synology-wrx560", "Synology WRX560", "Dual-Band Wi-Fi 6 Mesh", "192.168.1.1", "http://router.synology.com", "192.168.0.1", "admin (created on setup)", "admin (created on setup)", False, "Synology_XXXX", "Wi-Fi 6 (AX3000 with 2.5GbE)", 10, "Internal antenna modern styling with 2.5G WAN/LAN port and SRM operating system."),
        ("synology-mr2200ac", "Synology MR2200ac", "Tri-Band AC2200 Mesh", "192.168.1.1", "http://router.synology.com", "192.168.0.1", "admin (created on setup)", "admin (created on setup)", False, "Synology_XXXX", "Wi-Fi 5 (AC2200 Tri-Band Mesh)", 10, "Compact mesh router with dedicated tri-band backhaul running SRM."),
        ("synology-rt1900ac", "Synology RT1900ac", "First-Gen SRM Router", "192.168.1.1", "http://router.synology.com", "192.168.0.1", "admin", "admin", False, "Synology_XXXX", "Wi-Fi 5 (AC1900)", 10, "Pioneering SRM router with desktop-like web OS windowed multitasking."),
        ("synology-ds-gateway", "Synology DS-Gateway", "Modular SRM Network Controller", "192.168.1.1", "http://router.synology.com", "192.168.0.1", "admin", "admin", False, "Synology_XXXX", "Enterprise SRM Controller", 10, "Centralized multi-site SRM management gateway.")
    ]

    for item in synology_specs:
        slug, name, hw_type, def_ip, web, fallback, user, pwd, sticker, ssid, standard, reset_sec, note = item
        models.append({
            "slug": slug,
            "brand": "Synology",
            "brand_slug": "synology",
            "model_name": name,
            "hardware_type": hw_type,
            "default_ip": def_ip,
            "web_domain": web,
            "fallback_ip": fallback,
            "default_username": user,
            "default_password": pwd,
            "password_on_sticker": sticker,
            "default_ssid_pattern": ssid,
            "wifi_standard": standard,
            "reset_instructions": f"Use a paperclip to press and hold the Reset button on the back for {reset_sec} seconds until you hear a beep sound. Release the button and wait 2 minutes for SRM to restore default IP 192.168.1.1.",
            "led_indicators": [
                {"name": "STATUS", "normal": "Solid Green", "error": "Blinking Orange (Ready for setup / Resetting)", "desc": "SRM system state."},
                {"name": "WAN", "normal": "Solid Green", "error": "Blinking Orange (No WAN IP)", "desc": "Internet connectivity."},
                {"name": "Wi-Fi", "normal": "Solid Green", "error": "Off (Radio disabled)", "desc": "Wireless broadcast."}
            ],
            "mobile_app": "DS router App",
            "companion_app_store_url": "https://apps.apple.com/app/ds-router/id854964653",
            "official_manual_url": "https://www.synology.com/support",
            "notes": note
        })

    # --------------------------------------------------------------------------
    # 10. GOOGLE & NEST (6 Models)
    # --------------------------------------------------------------------------
    google_specs = [
        ("google-nest-wifi-pro", "Nest Wifi Pro (G6ZUC)", "Tri-Band Wi-Fi 6E Mesh", "192.168.86.1", "N/A (Google Home App)", "192.168.1.1", "Managed via Google Home", "Managed via Google Home", True, "SetupXXXX", "Wi-Fi 6E (AXE5400 Tri-Band)", 10, "Glossy ceramic finish inspired by pottery with 6GHz band, Thread border router, and Matter hub."),
        ("google-nest-wifi-router", "Nest Wifi Router (H2D)", "Smart Mesh Wi-Fi Router", "192.168.86.1", "N/A (Google Home App)", "192.168.1.1", "Managed via Google Home", "Managed via Google Home", True, "SetupXXXX", "Wi-Fi 5 (AC2200 4x4 MU-MIMO)", 10, "Matte-white rounded marshmallow form factor covering up to 2,200 sq ft."),
        ("google-nest-wifi-point", "Nest Wifi Point (H2E)", "Mesh Point with Smart Speaker", "192.168.86.1", "N/A (Google Home App)", "192.168.1.1", "Managed via Google Home", "Managed via Google Home", True, "SetupXXXX", "Wi-Fi 5 (AC1200)", 10, "Combines Wi-Fi mesh coverage with a built-in Google Assistant smart speaker with 360-degree sound."),
        ("google-wifi", "Google Wifi (NLS-1304-25)", "Whole-Home Mesh System", "192.168.86.1", "N/A (Google Home App)", "192.168.1.1", "Managed via Google Home", "Managed via Google Home", True, "setupXXXX", "Wi-Fi 5 (AC1200 Dual-Band)", 10, "The classic white hockey-puck mesh unit that democratized whole-home Wi-Fi roaming."),
        ("google-onhub-asus", "Google OnHub Asus (SRT-AC1900)", "Smart Wireless Router", "192.168.86.1", "N/A (Google Home App)", "192.168.1.1", "Managed via Google Home", "Managed via Google Home", False, "setupXXXX", "Wi-Fi 5 (AC1900 Wave Antennas)", 10, "Wave gesture sensor on top to boost Wi-Fi priority to a selected device."),
        ("google-onhub-tplink", "Google OnHub TP-Link (TGR1900)", "Smart Wireless Router", "192.168.86.1", "N/A (Google Home App)", "192.168.1.1", "Managed via Google Home", "Managed via Google Home", False, "setupXXXX", "Wi-Fi 5 (AC1900 Circular)", 10, "Internal circular array of 13 antennas with automated frequency scanning.")
    ]

    for item in google_specs:
        slug, name, hw_type, def_ip, web, fallback, user, pwd, sticker, ssid, standard, reset_sec, note = item
        models.append({
            "slug": slug,
            "brand": "Google Nest",
            "brand_slug": "google-nest",
            "model_name": name,
            "hardware_type": hw_type,
            "default_ip": def_ip,
            "web_domain": web,
            "fallback_ip": fallback,
            "default_username": user,
            "default_password": pwd,
            "password_on_sticker": sticker,
            "default_ssid_pattern": ssid,
            "wifi_standard": standard,
            "reset_instructions": f"While plugged into power, press and hold the physical reset button on the base for {reset_sec} seconds. The indicator light will pulse yellow/amber, then turn solid yellow. Release and wait 5 minutes until it pulses white, indicating it is ready for setup.",
            "led_indicators": [
                {"name": "Front LED Ring / Light", "normal": "Solid White (Connected and online)", "error": "Pulsing Yellow (No Internet connection) / Fast Blinking Yellow (Factory resetting)", "desc": "Overall gateway connectivity."},
                {"name": "Setup Light", "normal": "Slow Pulsing White (Ready for Google Home setup)", "error": "Solid Red (Critical hardware fault)", "desc": "Initial provisioning mode."}
            ],
            "mobile_app": "Google Home App",
            "companion_app_store_url": "https://apps.apple.com/app/google-home/id857864704",
            "official_manual_url": "https://support.google.com/googlenest",
            "notes": note
        })

    # --------------------------------------------------------------------------
    # 11. AMAZON EERO (8 Models)
    # --------------------------------------------------------------------------
    eero_specs = [
        ("amazon-eero-max-7", "Eero Max 7", "Tri-Band Wi-Fi 7 Mesh", "192.168.4.1", "N/A (Eero App)", "192.168.7.1", "Managed via Amazon eero App", "Managed via Amazon eero App", True, "eero-setup", "Wi-Fi 7 (BE20800 Tri-Band)", 15, "Flagship Wi-Fi 7 mesh node featuring dual 10GbE ports and dual 2.5GbE ports with TrueMesh."),
        ("amazon-eero-pro-6e", "Eero Pro 6E (S010001)", "Tri-Band Wi-Fi 6E Mesh", "192.168.4.1", "N/A (Eero App)", "192.168.7.1", "Managed via Amazon eero App", "Managed via Amazon eero App", True, "eero-setup", "Wi-Fi 6E (AXE5400 Tri-Band)", 15, "Features 2.5Gbps Ethernet port with access to the 6GHz spectrum for zero-interference streaming."),
        ("amazon-eero-pro-6", "Eero Pro 6 (K010001)", "Tri-Band Wi-Fi 6 Mesh", "192.168.4.1", "N/A (Eero App)", "192.168.7.1", "Managed via Amazon eero App", "Managed via Amazon eero App", True, "eero-setup", "Wi-Fi 6 (AX4200 Tri-Band)", 15, "Built-in Zigbee smart home hub with dual auto-sensing Gigabit Ethernet ports."),
        ("amazon-eero-6-plus", "Eero 6+ (R010001)", "Dual-Band Wi-Fi 6 Gigabit", "192.168.4.1", "N/A (Eero App)", "192.168.7.1", "Managed via Amazon eero App", "Managed via Amazon eero App", True, "eero-setup", "Wi-Fi 6 (AX3000 160MHz)", 15, "Enhanced 160MHz radio channels doubling client bandwidth over standard Eero 6."),
        ("amazon-eero-6", "Eero 6 (N010001)", "Dual-Band Wi-Fi 6 Mesh", "192.168.4.1", "N/A (Eero App)", "192.168.7.1", "Managed via Amazon eero App", "Managed via Amazon eero App", True, "eero-setup", "Wi-Fi 6 (AX1800 Dual-Band)", 15, "Compact curved mesh router with integrated Zigbee smart home hub."),
        ("amazon-eero-pro-2nd-gen", "Eero Pro (2nd Gen - B010001)", "Tri-Band AC2200 Mesh", "192.168.4.1", "N/A (Eero App)", "192.168.7.1", "Managed via Amazon eero App", "Managed via Amazon eero App", True, "eero-setup", "Wi-Fi 5 (AC2200 Tri-Band)", 15, "Tri-Band 2nd-generation router with intelligent auto-healing TrueMesh backhaul."),
        ("amazon-eero-beacon", "Eero Beacon", "Plug-In Mesh Expander", "192.168.4.1", "N/A (Eero App)", "192.168.7.1", "Managed via Amazon eero App", "Managed via Amazon eero App", True, "eero-setup", "Wi-Fi 5 (AC1300 Wall Plug)", 15, "Direct wall outlet plug-in mesh point with built-in ambient nightlight."),
        ("amazon-eero-1st-gen", "Eero (1st Gen)", "Original TrueMesh Router", "192.168.4.1", "N/A (Eero App)", "192.168.7.1", "Managed via Amazon eero App", "Managed via Amazon eero App", True, "eero-setup", "Wi-Fi 5 (AC1200)", 15, "The historic pioneer that launched the consumer mesh networking revolution in 2016.")
    ]

    for item in eero_specs:
        slug, name, hw_type, def_ip, web, fallback, user, pwd, sticker, ssid, standard, reset_sec, note = item
        models.append({
            "slug": slug,
            "brand": "Amazon Eero",
            "brand_slug": "eero",
            "model_name": name,
            "hardware_type": hw_type,
            "default_ip": def_ip,
            "web_domain": web,
            "fallback_ip": fallback,
            "default_username": user,
            "default_password": pwd,
            "password_on_sticker": sticker,
            "default_ssid_pattern": ssid,
            "wifi_standard": standard,
            "reset_instructions": f"Locate the reset button on the back/base. Hold down for {reset_sec} seconds until the LED light flashes red. Release immediately to reset the unit back to factory defaults. (Holding for 7 seconds resets network only without clearing registration).",
            "led_indicators": [
                {"name": "Front Status LED", "normal": "Solid White (Connected to Internet)", "error": "Solid Red (No Internet connection) / Blinking Blue (Bluetooth pairing) / Blinking Red (Resetting)", "desc": "Single status indicator LED."}
            ],
            "mobile_app": "eero App",
            "companion_app_store_url": "https://apps.apple.com/app/eero/id999605804",
            "official_manual_url": "https://support.eero.com",
            "notes": note
        })

    # --------------------------------------------------------------------------
    # 12. AVM FRITZ!BOX (12 Models)
    # --------------------------------------------------------------------------
    fritzbox_specs = [
        ("avm-fritzbox-7590-ax", "FRITZ!Box 7590 AX", "VDSL Wi-Fi 6 Router", "192.168.178.1", "http://fritz.box", "169.254.1.1", "admin", "Unique sticker password", True, "FRITZ!Box 7590 AX XX", "Wi-Fi 6 + VDSL Supervectoring 35b", 15, "German flagship VDSL router with 4x4 Wi-Fi 6, DECT cordless telephone base station, and ISDN."),
        ("avm-fritzbox-7590", "FRITZ!Box 7590", "VDSL AC+N Gateway", "192.168.178.1", "http://fritz.box", "169.254.1.1", "admin", "Unique sticker password", True, "FRITZ!Box 7590 XX", "Wi-Fi 5 (AC+N Dual-Band)", 15, "Iconic white/red curved housing with 4 Gigabit LAN ports and analog telephony ports."),
        ("avm-fritzbox-7530-ax", "FRITZ!Box 7530 AX", "VDSL Wi-Fi 6 Compact", "192.168.178.1", "http://fritz.box", "169.254.1.1", "admin", "Unique sticker password", True, "FRITZ!Box 7530 AX XX", "Wi-Fi 6 (AX1800 VDSL)", 15, "Energy-efficient compact Wi-Fi 6 VDSL supervectoring gateway with DECT base station."),
        ("avm-fritzbox-7530", "FRITZ!Box 7530", "VDSL Entry Gateway", "192.168.178.1", "http://fritz.box", "169.254.1.1", "admin", "Unique sticker password", True, "FRITZ!Box 7530 XX", "Wi-Fi 5 (AC+N)", 15, "Budget-friendly VDSL router with 4 Gigabit LAN ports and USB 3.0."),
        ("avm-fritzbox-5590-fiber", "FRITZ!Box 5590 Fiber", "Fiber GPON/AON Wi-Fi 6", "192.168.178.1", "http://fritz.box", "169.254.1.1", "admin", "Unique sticker password", True, "FRITZ!Box 5590 Fiber XX", "Wi-Fi 6 (4x4 2.5GbE Fiber)", 15, "Direct fiber optic connection via SFP slot (AON/GPON/XGS-PON) with 2.5Gbps LAN port."),
        ("avm-fritzbox-5530-fiber", "FRITZ!Box 5530 Fiber", "Compact Fiber Gateway", "192.168.178.1", "http://fritz.box", "169.254.1.1", "admin", "Unique sticker password", True, "FRITZ!Box 5530 Fiber XX", "Wi-Fi 6 (Fiber SFP)", 15, "Direct fiber broadband gateway with 2.5Gbps port and FRITZ!OS mesh integration."),
        ("avm-fritzbox-6690-cable", "FRITZ!Box 6690 Cable", "DOCSIS 3.1 2.5G Gateway", "192.168.178.1", "http://fritz.box", "169.254.1.1", "admin", "Unique sticker password", True, "FRITZ!Box 6690 Cable XX", "Wi-Fi 6 (4x4 DOCSIS 3.1 2.5G)", 15, "Top-tier cable broadband gateway with 2.5Gbps LAN port and 4x4 Wi-Fi 6."),
        ("avm-fritzbox-6660-cable", "FRITZ!Box 6660 Cable", "DOCSIS 3.1 Cable Gateway", "192.168.178.1", "http://fritz.box", "169.254.1.1", "admin", "Unique sticker password", True, "FRITZ!Box 6660 Cable XX", "Wi-Fi 6 (2x2 DOCSIS 3.1 2.5G)", 15, "2.5 Gigabit LAN port with DOCSIS 3.1 2x2 OFDM channel bonding."),
        ("avm-fritzbox-4060", "FRITZ!Box 4060", "Tri-Band Wi-Fi 6 Router", "192.168.178.1", "http://fritz.box", "169.254.1.1", "admin", "Unique sticker password", True, "FRITZ!Box 4060 XX", "Wi-Fi 6 (Tri-Band 2.5GbE WAN)", 15, "First FRITZ!Box wireless router without integrated modem, designed for fiber/ONT uplinks."),
        ("avm-fritzbox-4040", "FRITZ!Box 4040", "Gigabit Wireless Router", "192.168.178.1", "http://fritz.box", "169.254.1.1", "admin", "Unique sticker password", True, "FRITZ!Box 4040 XX", "Wi-Fi 5 (AC1300 Dual-Band)", 15, "Pure Ethernet router with Gigabit WAN and 4 Gigabit LAN ports for cable/fiber modems."),
        ("avm-fritzbox-6850-5g", "FRITZ!Box 6850 5G", "5G Cellular Broadband", "192.168.178.1", "http://fritz.box", "169.254.1.1", "admin", "Unique sticker password", True, "FRITZ!Box 6850 5G XX", "Wi-Fi 5 (5G/LTE Sub-6GHz)", 15, "High-speed 5G mobile broadband router with SMA external cellular antenna connectors."),
        ("avm-fritzbox-6890-lte", "FRITZ!Box 6890 LTE", "VDSL + LTE Hybrid Gateway", "192.168.178.1", "http://fritz.box", "169.254.1.1", "admin", "Unique sticker password", True, "FRITZ!Box 6890 LTE XX", "Wi-Fi 5 (VDSL 35b + LTE)", 15, "Hybrid gateway combining DSL broadband and LTE cellular connection with automatic failover.")
    ]

    for item in fritzbox_specs:
        slug, name, hw_type, def_ip, web, fallback, user, pwd, sticker, ssid, standard, reset_sec, note = item
        models.append({
            "slug": slug,
            "brand": "AVM FRITZ!Box",
            "brand_slug": "avm-fritzbox",
            "model_name": name,
            "hardware_type": hw_type,
            "default_ip": def_ip,
            "web_domain": web,
            "fallback_ip": fallback,
            "default_username": user,
            "default_password": pwd,
            "password_on_sticker": sticker,
            "default_ssid_pattern": ssid,
            "wifi_standard": standard,
            "reset_instructions": "Unplug the FRITZ!Box power cord. Wait 10 seconds, plug back in. Open a browser to emergency fallback IP http://169.254.1.1 or navigate to System > Backup > Factory Settings in FRITZ!OS.",
            "led_indicators": [
                {"name": "Power / DSL / Fiber", "normal": "Solid Green", "error": "Flashing Green (DSL synchronization / Line negotiation)", "desc": "Broadband physical connection."},
                {"name": "Internet", "normal": "Solid Green", "error": "Flashing Red (Account authentication failed)", "desc": "ISP PPPoE session."},
                {"name": "WLAN", "normal": "Solid Green", "error": "Off (Radio disabled)", "desc": "Wi-Fi broadcast."},
                {"name": "Info", "normal": "Solid Green", "error": "Flashing Red (Critical firmware update or alert)", "desc": "Configurable indicator."}
            ],
            "mobile_app": "MyFRITZ!App",
            "companion_app_store_url": "https://apps.apple.com/app/myfritz-app/id451230680",
            "official_manual_url": "https://avm.de/service/",
            "notes": note
        })

    # --------------------------------------------------------------------------
    # 13. ZYXEL (10 Models)
    # --------------------------------------------------------------------------
    zyxel_specs = [
        ("zyxel-armor-g5", "Armor G5 (NBG7815)", "Wi-Fi 6 Multi-Gig Router", "192.168.1.1", "http://zyxelwifi.net", "192.168.212.1", "admin", "1234", True, "Zyxel_XXXX", "Wi-Fi 6 (AX6000 12-Stream)", 10, "12-stream Multi-Gigabit Wi-Fi 6 router with 2.5G/5G WAN port and 2.2GHz quad-core processor."),
        ("zyxel-armor-g1", "Armor G1 (NBG6818)", "Multi-Gigabit AC2600 Router", "192.168.1.1", "http://zyxelwifi.net", "192.168.212.1", "admin", "1234", True, "Zyxel_XXXX", "Wi-Fi 5 (AC2600 4x4)", 10, "High-efficiency thermal airflow casing with 2.5G Multi-Gig WAN port."),
        ("zyxel-multy-x", "Multy X (WSQ50)", "Tri-Band AC3000 Mesh", "192.168.212.1", "http://zyxelwifi.com", "192.168.1.1", "admin", "admin", True, "Multy-XXXX", "Wi-Fi 5 (AC3000 Tri-Band Mesh)", 10, "Dedicated 1733Mbps 5GHz inter-node mesh backhaul with app-based Bluetooth setup."),
        ("zyxel-multy-m1", "Multy M1 (WSM20)", "Dual-Band Wi-Fi 6 Mesh", "192.168.212.1", "http://zyxelwifi.com", "192.168.1.1", "admin", "admin", True, "Multy-XXXX", "Wi-Fi 6 (AX1800 Mesh)", 10, "T-shaped minimal desktop mesh nodes with 1024-QAM and BSS coloring."),
        ("zyxel-usg-flex-100", "USG FLEX 100", "Firewall Security Gateway", "192.168.1.1", "https://192.168.1.1", "192.168.1.254", "admin", "1234", False, "N/A (Wired)", "Nebula Cloud UTM Gateway", 15, "Unified Threat Management gateway supporting Nebula cloud or on-premise management."),
        ("zyxel-usg-flex-200", "USG FLEX 200", "UTM Security Gateway", "192.168.1.1", "https://192.168.1.1", "192.168.1.254", "admin", "1234", False, "N/A (Wired)", "High-Throughput UTM Security Gateway", 15, "900Mbps SPI firewall throughput with anti-malware and collaborative network defense."),
        ("zyxel-usg20-vpn", "USG20-VPN", "Fanless VPN Gateway", "192.168.1.1", "https://192.168.1.1", "192.168.1.254", "admin", "1234", False, "N/A (Wired)", "Gigabit Fanless VPN Firewall", 15, "Fanless robust metal chassis ideal for silent office branch teleworking."),
        ("zyxel-vmg8825-b50b", "VMG8825-B50B", "VDSL2 Bonding Gateway", "192.168.1.1", "http://192.168.1.1", "192.168.0.1", "admin", "admin", True, "Zyxel_XXXX", "Wi-Fi 5 (AC2400 VDSL2 Bonding)", 10, "Carrier-grade VDSL2 vectoring and bonding gateway with VoIP telephony FXS ports."),
        ("zyxel-dx3301-t0", "DX3301-T0", "VDSL2 Wi-Fi 6 Gateway", "192.168.1.1", "http://192.168.1.1", "192.168.0.1", "admin", "admin", True, "Zyxel_XXXX", "Wi-Fi 6 (AX1800 VDSL2)", 10, "EasyMesh MOP-certified VDSL2 gateway deployed by telecom providers across Europe."),
        ("zyxel-nbg6604", "NBG6604", "AC1200 Dual-Band Router", "192.168.1.1", "http://zyxelwifi.net", "192.168.0.1", "admin", "1234", False, "Zyxel_XXXX", "Wi-Fi 5 (AC1200)", 10, "Ultra-compact dual-band router with 4 high-gain antennas.")
    ]

    for item in zyxel_specs:
        slug, name, hw_type, def_ip, web, fallback, user, pwd, sticker, ssid, standard, reset_sec, note = item
        models.append({
            "slug": slug,
            "brand": "Zyxel",
            "brand_slug": "zyxel",
            "model_name": name,
            "hardware_type": hw_type,
            "default_ip": def_ip,
            "web_domain": web,
            "fallback_ip": fallback,
            "default_username": user,
            "default_password": pwd,
            "password_on_sticker": sticker,
            "default_ssid_pattern": ssid,
            "wifi_standard": standard,
            "reset_instructions": f"Press and hold the Reset button on the rear for {reset_sec} seconds until the Power LED begins to blink amber. Release and wait 90 seconds for default 192.168.1.1 reload.",
            "led_indicators": [
                {"name": "Power / SYS", "normal": "Solid Green", "error": "Solid Amber (Self-test) / Blinking Amber (Factory reset)", "desc": "Hardware status."},
                {"name": "INTERNET", "normal": "Solid Green", "error": "Amber (No IP) / Off", "desc": "WAN interface."},
                {"name": "WLAN", "normal": "Solid Green", "error": "Off", "desc": "Wireless radio."}
            ],
            "mobile_app": "Zyxel Rover App",
            "companion_app_store_url": "https://apps.apple.com/app/zyxel-rover/id1450239638",
            "official_manual_url": "https://service-provider.zyxel.com",
            "notes": note
        })

    # --------------------------------------------------------------------------
    # 14. HUAWEI (10 Models)
    # --------------------------------------------------------------------------
    huawei_specs = [
        ("huawei-wifi-ax3-quad-core", "WiFi AX3 (Quad-Core WS7200)", "Wi-Fi 6 Plus Router", "192.168.3.1", "http://192.168.3.1", "192.168.1.1", "admin", "admin", True, "HUAWEI-XXXX", "Wi-Fi 6 Plus (AX3000 Quad-Core)", 10, "Gigahome quad-core 1.4GHz CPU with dynamic narrow bandwidth 160MHz technology and NFC one-touch connect."),
        ("huawei-wifi-ax3-dual-core", "WiFi AX3 (Dual-Core WS7100)", "Wi-Fi 6 Plus Router", "192.168.3.1", "http://192.168.3.1", "192.168.1.1", "admin", "admin", True, "HUAWEI-XXXX", "Wi-Fi 6 Plus (AX3000 Dual-Core)", 10, "Dual-core 1.2GHz version with Huawei Share NFC tap-to-connect for Android."),
        ("huawei-wifi-ax2", "WiFi AX2 (WS7001)", "Dual-Band Wi-Fi 6 Router", "192.168.3.1", "http://192.168.3.1", "192.168.1.1", "admin", "admin", True, "HUAWEI-XXXX", "Wi-Fi 6 (AX1500)", 10, "Auto-sensing Gigabit ports with HarmonyOS Mesh+ roaming support."),
        ("huawei-wifi-mesh-7", "WiFi Mesh 7 (WS8800)", "Tri-Band Mesh Wi-Fi 6", "192.168.3.1", "http://192.168.3.1", "192.168.1.1", "admin", "admin", True, "HUAWEI-XXXX", "Wi-Fi 6 (AX6600 Tri-Band Mesh)", 10, "8 power amplifiers covering up to 6,000 sq ft with HarmonyOS Connect."),
        ("huawei-wifi-mesh-3", "WiFi Mesh 3 (WS5800)", "Dual-Band Mesh Wi-Fi 6", "192.168.3.1", "http://192.168.3.1", "192.168.1.1", "admin", "admin", True, "HUAWEI-XXXX", "Wi-Fi 6 (AX3000 Mesh)", 10, "Dual-band Wi-Fi 6 mesh units with one-touch NFC connection."),
        ("huawei-5g-cpe-pro-2", "5G CPE Pro 2 (H122-373)", "5G Mobile Broadband Gateway", "192.168.8.1", "http://192.168.8.1", "192.168.1.1", "admin", "Unique sticker password", True, "HUAWEI-5G-XXXX", "Wi-Fi 6 + 5G Sub-6GHz (Balong 5000)", 10, "Balong 5000 chipset supporting 5G NSA/SA with peak download speeds up to 3.6 Gbps."),
        ("huawei-4g-router-3-pro", "4G Router 3 Pro (B535-232)", "LTE Cat7 Wireless Router", "192.168.8.1", "http://192.168.8.1", "192.168.1.1", "admin", "admin", True, "HUAWEI-4G-XXXX", "Wi-Fi 5 + LTE Cat 7 (300Mbps)", 10, "Dual-band Wi-Fi with 4 Gigabit Ethernet ports and micro-SIM card slot."),
        ("huawei-echolife-hg8245h", "EchoLife HG8245H", "GPON Optical ONT Gateway", "192.168.100.1", "http://192.168.100.1", "192.168.1.1", "telecomadmin", "admintelecom", False, "WirelessNet", "GPON ONT + Wi-Fi 4 (300Mbps)", 10, "The global standard FTTH GPON ONT deployed by fiber ISPs worldwide."),
        ("huawei-echolife-hg8145v5", "EchoLife HG8145V5", "Intelligent Routing GPON ONT", "192.168.100.1", "http://192.168.100.1", "192.168.18.1", "telecomadmin", "admintelecom", False, "WirelessNet", "GPON ONT + Wi-Fi 5 (AC1200)", 10, "Dual-band 802.11ac GPON terminal supporting QoS and IPv6 dual-stack."),
        ("huawei-b311-221", "4G Router B311 (B311-221)", "4G LTE Wireless Gateway", "192.168.8.1", "http://192.168.8.1", "192.168.1.1", "admin", "admin", True, "HUAWEI-B311-XXXX", "802.11n + LTE Cat 4 (150Mbps)", 10, "Compact plug-and-play desktop 4G router with external SMA antenna port.")
    ]

    for item in huawei_specs:
        slug, name, hw_type, def_ip, web, fallback, user, pwd, sticker, ssid, standard, reset_sec, note = item
        models.append({
            "slug": slug,
            "brand": "Huawei",
            "brand_slug": "huawei",
            "model_name": name,
            "hardware_type": hw_type,
            "default_ip": def_ip,
            "web_domain": web,
            "fallback_ip": fallback,
            "default_username": user,
            "default_password": pwd,
            "password_on_sticker": sticker,
            "default_ssid_pattern": ssid,
            "wifi_standard": standard,
            "reset_instructions": f"With the router powered ON, press the Reset pinhole on the bottom or back for {reset_sec} seconds until the indicator light flashes or turns off. Wait 2 minutes for the unit to reboot to default settings.",
            "led_indicators": [
                {"name": "Status Indicator", "normal": "Solid Green", "error": "Solid Red (No Internet/SIM error) / Blinking Red", "desc": "Overall gateway status."},
                {"name": "Signal / Network", "normal": "Solid Cyan/White (5G/4G connected)", "error": "Off (No carrier detected)", "desc": "Cellular or optical connection."},
                {"name": "LAN / Wi-Fi", "normal": "Solid Green", "error": "Off", "desc": "Local interface status."}
            ],
            "mobile_app": "Huawei AI Life",
            "companion_app_store_url": "https://consumer.huawei.com/en/mobileservices/ai-life/",
            "official_manual_url": "https://consumer.huawei.com/en/support/",
            "notes": note
        })

    # --------------------------------------------------------------------------
    # 15. GL.INET (10 Models)
    # --------------------------------------------------------------------------
    glinet_specs = [
        ("gl-inet-slate-ax-gl-axt1800", "Slate AX (GL-AXT1800)", "Wi-Fi 6 Travel Router", "192.168.8.1", "http://192.168.8.1", "192.168.1.1", "root", "admin (created on setup)", False, "GL-AXT1800-XXX", "Wi-Fi 6 (AX1800 Travel)", 10, "IPQ6000 quad-core 1.2GHz processor with OpenWrt 21.02, WireGuard client/server, and Tor."),
        ("gl-inet-beryl-ax-gl-mt3000", "Beryl AX (GL-MT3000)", "Pocket Wi-Fi 6 2.5G Router", "192.168.8.1", "http://192.168.8.1", "192.168.1.1", "root", "admin (created on setup)", False, "GL-MT3000-XXX", "Wi-Fi 6 (AX3000 with 2.5G WAN)", 10, "MediaTek MT7981B dual-core CPU with 2.5Gbps WAN port and physical toggle switch."),
        ("gl-inet-beryl-gl-mt1300", "Beryl (GL-MT1300)", "High-Performance Travel Router", "192.168.8.1", "http://192.168.8.1", "192.168.1.1", "root", "admin (created on setup)", False, "GL-MT1300-XXX", "Wi-Fi 5 (AC1300 Dual-Band)", 10, "Type-C power delivery with 3 Gigabit ports and MicroSD slot for mobile file sharing."),
        ("gl-inet-opal-gl-sft1200", "Opal (GL-SFT1200)", "Ultra-Portable Travel Router", "192.168.8.1", "http://192.168.8.1", "192.168.1.1", "root", "admin (created on setup)", False, "GL-SFT1200-XXX", "Wi-Fi 5 (AC1200)", 10, "Pocket-sized budget champion weighing only 144 grams with dual-band gigabit."),
        ("gl-inet-slate-gl-ar750s", "Slate (GL-AR750S-Ext)", "Gigabit Dual-Band AC Router", "192.168.8.1", "http://192.168.8.1", "192.168.1.1", "root", "admin (created on setup)", False, "GL-AR750S-XXX", "Wi-Fi 5 (AC750)", 10, "3 Gigabit ports with fold-out dual-band external antennas and physical toggle switch."),
        ("gl-inet-shadow-gl-ar300m", "Shadow (GL-AR300M16)", "Mini Micro-USB Router", "192.168.8.1", "http://192.168.8.1", "192.168.1.1", "root", "admin (created on setup)", False, "GL-AR300M-XXX", "802.11n (300Mbps Micro Router)", 10, "Matchbox-sized wireless router powered by standard 5V USB charger."),
        ("gl-inet-flint-gl-ax1800", "Flint (GL-AX1800)", "Wi-Fi 6 OpenWrt Home Gateway", "192.168.8.1", "http://192.168.8.1", "192.168.1.1", "root", "admin (created on setup)", False, "GL-AX1800-XXX", "Wi-Fi 6 (AX1800 Quad-Core)", 10, "5 Gigabit ports with 500Mbps WireGuard VPN throughput for smart home protection."),
        ("gl-inet-flint-2-gl-mt6000", "Flint 2 (GL-MT6000)", "Dual 2.5G Wi-Fi 6 Router", "192.168.8.1", "http://192.168.8.1", "192.168.1.1", "root", "admin (created on setup)", False, "GL-MT6000-XXX", "Wi-Fi 6 (AX6000 Dual 2.5G)", 10, "Heavy-duty home router with dual 2.5GbE ports, 1GB DDR4 RAM, and 900Mbps WireGuard speed."),
        ("gl-inet-spitz-ax-gl-x3000", "Spitz AX (GL-X3000)", "Dual-SIM 5G NR Gateway", "192.168.8.1", "http://192.168.8.1", "192.168.1.1", "root", "admin (created on setup)", False, "GL-X3000-XXX", "Wi-Fi 6 + 5G NR Dual-SIM", 10, "Industrial RV/marine 5G cellular router with dual-SIM auto failover and GPS tracking."),
        ("gl-inet-mudi-gl-e750", "Mudi (GL-E750)", "Portable 4G LTE Privacy Router", "192.168.8.1", "http://192.168.8.1", "192.168.1.1", "root", "admin (created on setup)", False, "GL-E750-XXX", "Wi-Fi 5 + 4G LTE with 7000mAh Battery", 10, "Pocket privacy router with built-in 7000mAh rechargeable battery and OLED display.")
    ]

    for item in glinet_specs:
        slug, name, hw_type, def_ip, web, fallback, user, pwd, sticker, ssid, standard, reset_sec, note = item
        models.append({
            "slug": slug,
            "brand": "GL.iNet",
            "brand_slug": "gl-inet",
            "model_name": name,
            "hardware_type": hw_type,
            "default_ip": def_ip,
            "web_domain": web,
            "fallback_ip": fallback,
            "default_username": user,
            "default_password": pwd,
            "password_on_sticker": sticker,
            "default_ssid_pattern": ssid,
            "wifi_standard": standard,
            "reset_instructions": f"With the router powered ON, press and hold the Reset button for {reset_sec} seconds until the blue LED starts blinking rapidly, then release. The router will revert to factory OpenWrt settings at 192.168.8.1.",
            "led_indicators": [
                {"name": "Power LED", "normal": "Solid Blue/White", "error": "Blinking (Booting) / Off", "desc": "Hardware power."},
                {"name": "Wi-Fi LED", "normal": "Solid Blue", "error": "Off (Radio disabled)", "desc": "Wireless broadcast."},
                {"name": "VPN LED", "normal": "Solid Blue (VPN tunnel active)", "error": "Off (No VPN client connected)", "desc": "WireGuard/OpenVPN tunnel status."}
            ],
            "mobile_app": "GL.iNet App",
            "companion_app_store_url": "https://apps.apple.com/app/gl-inet/id1459424849",
            "official_manual_url": "https://docs.gl-inet.com",
            "notes": note
        })

    # --------------------------------------------------------------------------
    # 16. DRAYTEK (8 Models)
    # --------------------------------------------------------------------------
    draytek_specs = [
        ("draytek-vigor-2927", "Vigor 2927 Series", "Dual-WAN Gigabit VPN Router", "192.168.1.1", "http://192.168.1.1", "192.168.0.1", "admin", "admin", False, "DrayTek-XXXX", "Dual-WAN Gigabit Business Router", 10, "Dual-WAN broadband router with 50 VPN tunnels, 25 SSL VPN tunnels, and SPI firewall."),
        ("draytek-vigor-2962", "Vigor 2962", "Multi-WAN 2.5G & SFP Router", "192.168.1.1", "http://192.168.1.1", "192.168.0.1", "admin", "admin", False, "N/A (Wired)", "2.5G / SFP Multi-WAN Enterprise", 10, "2.5GbE Multi-Gigabit port and optical SFP cage with 2.2Gbps NAT throughput."),
        ("draytek-vigor-2865", "Vigor 2865 Series", "VDSL2 35b Security Router", "192.168.1.1", "http://192.168.1.1", "192.168.0.1", "admin", "admin", False, "DrayTek-XXXX", "VDSL2 35b Supervectoring + GbE WAN", 10, "Supervectoring VDSL2 modem router with Gigabit Ethernet WAN backup and 32 VLANs."),
        ("draytek-vigor-3910", "Vigor 3910", "Multi-WAN 10G Enterprise Router", "192.168.1.1", "http://192.168.1.1", "192.168.0.1", "admin", "admin", False, "N/A (Wired)", "Quad 10G SFP+ Core Enterprise Router", 10, "Quad-core 2.0GHz enterprise router with 4x 10G SFP+ ports and 9.4 Gbps NAT throughput."),
        ("draytek-vigor-2135", "Vigor 2135 Series", "Single-WAN Gigabit Router", "192.168.1.1", "http://192.168.1.1", "192.168.0.1", "admin", "admin", False, "DrayTek-XXXX", "Gigabit SOHO Security Router", 10, "Cost-effective small office/home office broadband router with hardware acceleration."),
        ("draytek-vigor-2765", "Vigor 2765 Series", "VDSL2/ADSL2+ SOHO Router", "192.168.1.1", "http://192.168.1.1", "192.168.0.1", "admin", "admin", False, "DrayTek-XXXX", "VDSL2/ADSL2+ Security Router", 10, "Integrated DSL modem router with SPI firewall, content filtering, and 2 VPN tunnels."),
        ("draytek-vigor-2926", "Vigor 2926 Series", "Dual-WAN Business Router", "192.168.1.1", "http://192.168.1.1", "192.168.0.1", "admin", "admin", False, "DrayTek-XXXX", "Dual-WAN Gigabit VPN Router", 10, "Longstanding business favorite with dual Gigabit WAN and Central Management."),
        ("draytek-vigor-2862", "Vigor 2862 Series", "Classic VDSL2 Security Router", "192.168.1.1", "http://192.168.1.1", "192.168.0.1", "admin", "admin", False, "DrayTek-XXXX", "VDSL2/ADSL2+ Enterprise Router", 10, "VDSL2 vectoring router with USB ports for 4G failover dongles.")
    ]

    for item in draytek_specs:
        slug, name, hw_type, def_ip, web, fallback, user, pwd, sticker, ssid, standard, reset_sec, note = item
        models.append({
            "slug": slug,
            "brand": "DrayTek",
            "brand_slug": "draytek",
            "model_name": name,
            "hardware_type": hw_type,
            "default_ip": def_ip,
            "web_domain": web,
            "fallback_ip": fallback,
            "default_username": user,
            "default_password": pwd,
            "password_on_sticker": sticker,
            "default_ssid_pattern": ssid,
            "wifi_standard": standard,
            "reset_instructions": f"While router is running, press and hold the Factory Reset pinhole on the front panel for {reset_sec} seconds until the ACT LED starts blinking rapidly. Release and wait 1 minute.",
            "led_indicators": [
                {"name": "ACT", "normal": "Blinking Green (1 sec cadence normal)", "error": "Solid or Off (Firmware hung/system error)", "desc": "DrayOS activity."},
                {"name": "WAN 1 / WAN 2", "normal": "Solid Green", "error": "Blinking (Negotiating) / Off", "desc": "Physical broadband uplink."},
                {"name": "VPN", "normal": "Solid Green (Active tunnel)", "error": "Off", "desc": "IPsec/SSL VPN status."}
            ],
            "mobile_app": "DrayTek Wireless App",
            "companion_app_store_url": "https://www.draytek.com",
            "official_manual_url": "https://www.draytek.com/support/guides/",
            "notes": note
        })

    # --------------------------------------------------------------------------
    # 17. ARRIS SURFBOARD & MOTOROLA (16 Models)
    # --------------------------------------------------------------------------
    cable_specs = [
        ("arris-surfboard-g54", "SURFboard G54", "Quad-Band Wi-Fi 7 Cable Gateway", "192.168.0.1", "http://192.168.0.1", "192.168.100.1", "admin", "password", True, "SURFboard-XXXX", "Wi-Fi 7 (BE18000 DOCSIS 3.1)", 15, "World's premier Wi-Fi 7 DOCSIS 3.1 cable modem router with 10Gbps Ethernet port."),
        ("arris-surfboard-g36", "SURFboard G36", "Wi-Fi 6 AX3000 Cable Gateway", "192.168.0.1", "http://192.168.0.1", "192.168.100.1", "admin", "password", True, "SURFboard-XXXX", "Wi-Fi 6 (AX3000 DOCSIS 3.1 2.5G)", 15, "DOCSIS 3.1 cable modem with 2.5Gbps Ethernet port and Wi-Fi 6 AX3000."),
        ("arris-surfboard-g34", "SURFboard G34", "Wi-Fi 6 AX3000 Cable Gateway", "192.168.0.1", "http://192.168.0.1", "192.168.100.1", "admin", "password", True, "SURFboard-XXXX", "Wi-Fi 6 (AX3000 DOCSIS 3.1)", 15, "4 Gigabit Ethernet ports with 32x8 DOCSIS 3.0 channel bonding fallback."),
        ("arris-surfboard-sbg8300", "SURFboard SBG8300", "DOCSIS 3.1 AC2300 Gateway", "192.168.0.1", "http://192.168.0.1", "192.168.100.1", "admin", "password", True, "SBG8300-XXXX", "Wi-Fi 5 (AC2300 DOCSIS 3.1)", 15, "DOCSIS 3.1 certified for multi-gigabit cable internet plans with 4 Gigabit ports."),
        ("arris-surfboard-sbg7600ac2", "SURFboard SBG7600AC2", "DOCSIS 3.0 AC2300 Gateway", "192.168.0.1", "http://192.168.0.1", "192.168.100.1", "admin", "password", True, "SBG7600AC2-XXXX", "Wi-Fi 5 (AC2300 32x8)", 15, "32 download and 8 upload DOCSIS 3.0 bonded channels with McAfee Secure Home protection."),
        ("arris-surfboard-sbg7400ac2", "SURFboard SBG7400AC2", "DOCSIS 3.0 AC1750 Gateway", "192.168.0.1", "http://192.168.0.1", "192.168.100.1", "admin", "password", True, "SBG7400AC2-XXXX", "Wi-Fi 5 (AC1750 24x8)", 15, "24x8 channel bonding supporting cable download speeds up to 1 Gbps."),
        ("arris-surfboard-sbg6900-ac", "SURFboard SBG6900-AC", "DOCSIS 3.0 AC1900 Modem Router", "192.168.0.1", "http://192.168.0.1", "192.168.100.1", "admin", "password", True, "SBG6900AC-XXXX", "Wi-Fi 5 (AC1900 16x4)", 15, "16 downstream and 4 upstream channels with dual-band 3x3 AC Wi-Fi."),
        ("arris-surfboard-sbg10", "SURFboard SBG10", "DOCSIS 3.0 AC1600 Gateway", "192.168.0.1", "http://192.168.0.1", "192.168.100.1", "admin", "password", True, "SBG10-XXXX", "Wi-Fi 5 (AC1600 16x4)", 15, "Affordable 2-in-1 cable modem router with 2 Gigabit Ethernet ports."),
        ("arris-nvg589", "Arris NVG589", "VDSL2 Gateway with Voice", "192.168.1.254", "http://192.168.1.254", "192.168.1.1", "admin", "Sticker password", True, "ATT-WIFI-XXXX", "802.11n VDSL2 Bonded Gateway", 15, "Widely deployed AT&T U-verse bonded VDSL2 gateway with Access Code on unit label."),
        ("arris-bgw210-700", "Arris BGW210-700", "Broadband Fiber ONT Gateway", "192.168.1.254", "http://192.168.1.254", "192.168.1.1", "admin", "Sticker Access Code", True, "ATT-WIFI-XXXX", "Wi-Fi 5 (AC2100 4x4 MU-MIMO)", 15, "Primary gateway for AT&T Fiber gigabit connections featuring internal ONT link and IP Passthrough."),
        ("motorola-mg8725", "Motorola MG8725", "DOCSIS 3.1 Wi-Fi 6 AX6000", "192.168.0.1", "http://192.168.0.1", "192.168.100.1", "admin", "motorola", True, "Motorola-XXXX", "Wi-Fi 6 (AX6000 DOCSIS 3.1 2.5G)", 15, "Includes 2.5Gbps Multi-Gigabit port and 4x4 Power Boost Wi-Fi 6."),
        ("motorola-mg8702", "Motorola MG8702", "DOCSIS 3.1 AC3200 Gateway", "192.168.0.1", "http://192.168.0.1", "192.168.100.1", "admin", "motorola", True, "Motorola-XXXX", "Wi-Fi 5 (AC3200 4x4 DOCSIS 3.1)", 15, "Equipped with Broadcom DOCSIS 3.1 chipset and Active Queue Management (AQM)."),
        ("motorola-mg7700", "Motorola MG7700", "DOCSIS 3.0 AC1900 Gateway", "192.168.0.1", "http://192.168.0.1", "192.168.100.1", "admin", "motorola", True, "Motorola-XXXX", "Wi-Fi 5 (AC1900 24x8)", 15, "24x8 DOCSIS 3.0 cable modem router with AnyBeam implicit beamforming at 5GHz."),
        ("motorola-mg7550", "Motorola MG7550", "DOCSIS 3.0 AC1900 Gateway", "192.168.0.1", "http://192.168.0.1", "192.168.100.1", "admin", "motorola", True, "Motorola-XXXX", "Wi-Fi 5 (AC1900 16x4)", 15, "16 downstream channels supporting cable internet plans up to 375 Mbps."),
        ("motorola-mt7711", "Motorola MT7711", "DOCSIS 3.0 with Voice", "192.168.0.1", "http://192.168.0.1", "192.168.100.1", "admin", "motorola", True, "Motorola-XXXX", "Wi-Fi 5 (AC1900 24x8 Telephone)", 15, "Built-in 2 phone ports for Comcast Xfinity Voice telephone service."),
        ("motorola-mr2600", "Motorola MR2600", "Smart Wi-Fi Gigabit Router", "192.168.1.1", "http://192.168.1.1", "192.168.0.1", "admin", "motorola", False, "Motorola-XXXX", "Wi-Fi 5 (AC2600 4x4)", 10, "Standalone high-power router with 4 external antennas and USB 3.0 file sharing.")
    ]

    for item in cable_specs:
        slug, name, hw_type, def_ip, web, fallback, user, pwd, sticker, ssid, standard, reset_sec, note = item
        brand_name = "Arris" if "arris" in slug else "Motorola"
        brand_slug = "arris" if "arris" in slug else "motorola"
        models.append({
            "slug": slug,
            "brand": brand_name,
            "brand_slug": brand_slug,
            "model_name": name,
            "hardware_type": hw_type,
            "default_ip": def_ip,
            "web_domain": web,
            "fallback_ip": fallback,
            "default_username": user,
            "default_password": pwd,
            "password_on_sticker": sticker,
            "default_ssid_pattern": ssid,
            "wifi_standard": standard,
            "reset_instructions": f"Press and hold the recessed Reset button on the rear for {reset_sec} seconds using a paperclip until all front LEDs blink simultaneously. Wait 3 minutes for DOCSIS upstream locking.",
            "led_indicators": [
                {"name": "Power", "normal": "Solid Green", "error": "Off", "desc": "Device power."},
                {"name": "Downstream", "normal": "Solid Blue (DOCSIS 3.1) / Solid Green (DOCSIS 3.0)", "error": "Blinking (Scanning for carrier)", "desc": "Incoming cable signal."},
                {"name": "Upstream", "normal": "Solid Blue (OFDMA bonded) / Solid Green", "error": "Blinking (Upstream ranging)", "desc": "Return channel link."},
                {"name": "Online", "normal": "Solid Green", "error": "Blinking (Obtaining DHCP/TFTP configuration)", "desc": "ISP provisioning."}
            ],
            "mobile_app": "SURFboard Central / motosync App",
            "companion_app_store_url": "https://apps.apple.com/app/surfboard-central/id1454519659",
            "official_manual_url": "https://www.surfboard.com/support/",
            "notes": note
        })

    # Return complete list of 251 models
    return models

if __name__ == "__main__":
    catalog = create_models_catalog()
    print(f"Generated {len(catalog)} router models successfully!")

