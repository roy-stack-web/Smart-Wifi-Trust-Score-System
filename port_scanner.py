import nmap

scanner = nmap.PortScanner(
    nmap_search_path=(
        r"C:\Program Files (x86)\Nmap\nmap.exe",
    )
)


def get_open_ports(ip):
    ports = []

    try:
        scanner.scan(ip, '1-1024')

        if ip in scanner.all_hosts():
            for protocol in scanner[ip].all_protocols():
                for port in scanner[ip][protocol].keys():
                    if scanner[ip][protocol][port]['state'] == 'open':
                        ports.append(port)

    except Exception as e:
        print(f"Port scan failed for {ip}: {e}")

    return ports