# Smart Wi-Fi Trust Score System

A cybersecurity project that scans devices connected to a local Wi-Fi network and assigns each device a trust score based on multiple factors such as vendor reputation, open ports, device history, and activity patterns.

---

## Features

✅ Device discovery on local Wi-Fi network  
✅ MAC vendor identification  
✅ Device history tracking  
✅ Open port analysis using Nmap  
✅ Dynamic trust scoring  
✅ Time-based anomaly detection  
✅ Vendor reputation scoring  
✅ New device alerts  
✅ CSV report generation  
✅ Flask dashboard visualization  

---

## Tech Stack

- Python
- Scapy
- Flask
- Nmap
- HTML/CSS
- CSV
- MAC Vendor Lookup

---

## Project Structure

```
smart-wifi-trust-score-system/
│
├── app.py
├── scanner.py
├── trust_engine.py
├── port_scanner.py
├── logger.py
├── database.json
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── reports/
│
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/smart-wifi-trust-score-system.git
cd smart-wifi-trust-score-system
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

---

### 3. Install required packages

```bash
pip install -r requirements.txt
```

---

### 4. Install Nmap

Download and install Nmap:

https://nmap.org/download.html

Verify installation:

```bash
nmap --version
```

---

### 5. Run the application

```bash
python app.py
```

---

### 6. Open dashboard

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## How It Works

The system performs:

1. ARP scanning to discover devices on the local network.
2. Vendor identification using MAC addresses.
3. Open port scanning using Nmap.
4. Device history tracking using a local database.
5. Trust score calculation based on:
   - Vendor reputation
   - Number of open ports
   - Frequency of appearance
   - Time of activity
   - Known/unknown device status
6. Dashboard visualization using Flask.

---

## Example Trust Scores

| Device | Trust Score | Status |
|---------|------------|--------|
| Router | 100 | TRUSTED |
| Personal Laptop | 95 | TRUSTED |
| Mobile Phone | 90 | SAFE |
| Unknown Device | 35 | HIGH RISK |

---

## Example Alert

```
⚠ NEW DEVICE DETECTED

IP Address  : 192.168.1.145
Vendor      : Unknown
Open Ports  : [22, 80, 445]
Trust Score : 35/100
```

---

## Example Use Cases

- Home Wi-Fi monitoring
- Detecting unknown devices on a network
- Learning network security concepts
- Asset discovery and inventory management
- Cybersecurity portfolio project

---

## Disclaimer

This project is intended for educational purposes and for monitoring networks that you own or have permission to analyze.

---

## Maintainer

**roy-stack-web**
Cybersecurity Enthusiast | Security+ Aspirant