import csv
import os
from datetime import datetime


def save_scan_report(devices):
    date = datetime.now().strftime("%Y-%m-%d")
    filename = f"reports/scan_{date}.csv"

    file_exists = os.path.isfile(filename)

    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)

        # Write header only if file is new
        if not file_exists:
            writer.writerow([
                "Timestamp",
                "IP Address",
                "MAC Address",
                "Vendor",
                "Times Seen",
                "Open Ports",
                "Trust Score"
            ])

        for device in devices:
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                device["ip"],
                device["mac"],
                device["vendor"],
                device["times_seen"],
                ",".join(map(str, device["open_ports"])),
                device["trust_score"]
            ])