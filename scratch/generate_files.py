import os

BASE_DIR = "/home/vlisivka/workspace/networks/src"

files_to_create = {
    # Hardware (fixing missing)
    "hardware/switches-check.md": "перевірка роботи (Комутатори)",
    "hardware/switches-problems.md": "типові проблеми (Комутатори)",
    # Hardware (new)
    "hardware/routers.md": "маршрутизатори",
    "hardware/routers-check.md": "перевірка роботи (маршрутизатори)",
    "hardware/routers-problems.md": "типові проблеми (маршрутизатори)",
    "hardware/firewalls.md": "фаєрволи",
    "hardware/firewalls-check.md": "перевірка роботи (фаєрволи)",
    "hardware/firewalls-problems.md": "типові проблеми (фаєрволи)",
    "hardware/relays.md": "релеї",
    "hardware/relays-check.md": "перевірка роботи (релеї)",
    "hardware/relays-problems.md": "типові проблеми (релеї)",
    "hardware/modems.md": "модеми",
    "hardware/modems-check.md": "перевірка роботи (модеми)",
    "hardware/modems-problems.md": "типові проблеми (модеми)",
    "hardware/media-converters.md": "медіаконвертори",
    "hardware/media-converters-check.md": "перевірка роботи (медіаконвертори)",
    "hardware/media-converters-problems.md": "типові проблеми (медіаконвертори)",
    "hardware/access-points.md": "точки доступу",
    "hardware/access-points-check.md": "перевірка роботи (точки доступу)",
    "hardware/access-points-problems.md": "типові проблеми (точки доступу)",
    "hardware/servers.md": "сервери",
    "hardware/servers-check.md": "перевірка роботи (сервери)",
    "hardware/servers-problems.md": "типові проблеми (сервери)",

    # Networks
    "networks/index.md": "Мережі",
    "networks/ethernet.md": "Мережі Ethernet",
    "networks/ethernet-principles.md": "принцип роботи (Ethernet)",
    "networks/ethernet-connectors.md": "конектори (Ethernet)",
    "networks/ethernet-cables.md": "кабелі (Ethernet)",
    "networks/ethernet-implementations.md": "варіанти реалізації (Ethernet)",
    "networks/ethernet-check.md": "перевірка роботи (Ethernet)",
    "networks/ethernet-problems.md": "типові проблеми (Ethernet)",
    "networks/wifi.md": "Мережі WiFi",
    "networks/wifi-principles.md": "принцип роботи (WiFi)",
    "networks/wifi-implementations.md": "варіанти реалізації (WiFi)",
    "networks/wifi-check.md": "перевірка роботи (WiFi)",
    "networks/wifi-problems.md": "типові проблеми (WiFi)",
    "networks/optical.md": "Оптичні мережі",
    "networks/optical-principles.md": "принцип роботи (Оптичні мережі)",
    "networks/optical-connectors.md": "конектори (Оптичні мережі)",
    "networks/optical-cables.md": "кабелі (Оптичні мережі)",
    "networks/optical-implementations.md": "варіанти реалізації (Оптичні мережі)",
    "networks/optical-check.md": "перевірка роботи (Оптичні мережі)",
    "networks/optical-problems.md": "типові проблеми (Оптичні мережі)",
    "networks/satellite.md": "Супутникові мережі",
    "networks/satellite-principles.md": "принцип роботи (Супутникові мережі)",
    "networks/satellite-antennas.md": "антени (Супутникові мережі)",
    "networks/satellite-cables.md": "кабелі (Супутникові мережі)",
    "networks/satellite-implementations.md": "варіанти реалізації (Супутникові мережі)",
    "networks/satellite-check.md": "перевірка роботи (Супутникові мережі)",
    "networks/satellite-problems.md": "типові проблеми (Супутникові мережі)",
    "networks/radio.md": "Радіозвʼязок",
    "networks/radio-principles.md": "принцип роботи (Радіозвʼязок)",
    "networks/radio-antennas.md": "антени (Радіозвʼязок)",
    "networks/radio-cables.md": "кабелі (Радіозвʼязок)",
    "networks/radio-implementations.md": "варіанти реалізації (Радіозвʼязок)",
    "networks/radio-check.md": "перевірка роботи (Радіозвʼязок)",
    "networks/radio-problems.md": "типові проблеми (Радіозвʼязок)",

    # Protocols
    "protocols/index.md": "Основні протоколи",
    "protocols/internet-stack.md": "Стек протоколів Internet",
    "protocols/l2.md": "L2 (Ethernet)",
    "protocols/l2-mac.md": "MAC-адреси",
    "protocols/l2-arp.md": "ARP",
    "protocols/l2-check.md": "перевірка роботи (L2)",
    "protocols/l2-problems.md": "типові проблеми (L2)",
    "protocols/l3.md": "L3 (IP, TCP/IP, UDP)",
    "protocols/l3-ip.md": "IP-адреса",
    "protocols/l3-routing.md": "маршрутизація",
    "protocols/l3-check.md": "перевірка роботи (L3)",
    "protocols/l3-problems.md": "типові проблеми (L3)",
    "protocols/dhcp.md": "DHCP",
    "protocols/dhcp-principles.md": "принцип роботи (DHCP)",
    "protocols/dhcp-check.md": "перевірка роботи (DHCP)",
    "protocols/dhcp-problems.md": "типові проблеми (DHCP)",
    "protocols/dns.md": "DNS",
    "protocols/dns-principles.md": "принцип роботи (DNS)",
    "protocols/dns-check.md": "перевірка роботи (DNS)",
    "protocols/dns-problems.md": "типові проблеми (DNS)",
    "protocols/vlan.md": "VLAN",
    "protocols/vlan-principles.md": "принцип роботи (VLAN)",
    "protocols/vlan-check.md": "перевірка роботи (VLAN)",
    "protocols/vlan-problems.md": "типові проблеми (VLAN)",
    "protocols/vpn.md": "VPN",
    "protocols/vpn-principles.md": "принцип роботи (VPN)",
    "protocols/vpn-check.md": "перевірка роботи (VPN)",
    "protocols/vpn-problems.md": "типові проблеми (VPN)",
}

template = """---
title: {title}
---

# {title}

Додайте опис тут.
"""

for path, title in files_to_create.items():
    full_path = os.path.join(BASE_DIR, path)
    if not os.path.exists(full_path):
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(template.format(title=title))
        print(f"Created: {path}")
    else:
        print(f"Skipped (exists): {path}")
