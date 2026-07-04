from scapy.all import ARP, Ether, srp
from mac_vendor_lookup import MacLookup
from trust_engine import update_device, calculate_trust_score
from port_scanner import get_open_ports
from logger import save_scan_report

lookup = MacLookup()


def scan_network(ip):
    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = ether / arp

    result = srp(packet, timeout=2, verbose=0)[0]

    devices = []

    for sent, received in result:

        # Get vendor information
        try:
            vendor = lookup.lookup(received.hwsrc)
        except:
            vendor = "Unknown"

        # Update database and get device history
        device_data = update_device(received.hwsrc)

        # Scan open ports
        open_ports = get_open_ports(received.psrc)

        # Calculate trust score
        trust_score = calculate_trust_score({
            "vendor": vendor,
            "times_seen": device_data["times_seen"],
            "known_device": device_data["known_device"],
            "open_ports": open_ports
        })

        # Alert for new devices
        if device_data["times_seen"] == 1:
            print("\n⚠ NEW DEVICE DETECTED ⚠")
            print(f"IP Address  : {received.psrc}")
            print(f"MAC Address : {received.hwsrc}")
            print(f"Vendor      : {vendor}")
            print(f"Open Ports  : {open_ports}")
            print(f"Trust Score : {trust_score}/100")
            print("-" * 50)

        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc,
            "vendor": vendor,
            "times_seen": device_data["times_seen"],
            "known_device": device_data["known_device"],
            "open_ports": open_ports,
            "trust_score": trust_score
        })

    return devices


# Scan your Wi-Fi network
devices = scan_network("192.168.9.0/24")
save_scan_report(devices)

print("\nConnected Devices:\n")

for device in devices:

    if device["trust_score"] >= 90:
        status = "TRUSTED"
    elif device["trust_score"] >= 70:
        status = "SAFE"
    elif device["trust_score"] >= 40:
        status = "SUSPICIOUS"
    else:
        status = "HIGH RISK"

    print("=" * 60)
    print(f"IP Address   : {device['ip']}")
    print(f"MAC Address  : {device['mac']}")
    print(f"Vendor       : {device['vendor']}")
    print(f"Times Seen   : {device['times_seen']}")
    print(f"Open Ports   : {device['open_ports']}")
    print(f"Trust Score  : {device['trust_score']}/100")
    print(f"Status       : {status}")