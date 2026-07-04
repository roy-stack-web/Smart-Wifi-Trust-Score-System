from port_scanner import get_open_ports

ip = input("Enter IP: ")

ports = get_open_ports(ip)

print("Open Ports:", ports)