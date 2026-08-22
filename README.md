# 🛡️ PORT PY

A lightweight, educational **TCP port scanner written in Python** for systems you own or are authorized to test.

PORT PY performs multi-threaded TCP connect scanning, grabs service banners, checks banners against a small set of known vulnerability signatures, displays colored terminal output, and exports scan results to TXT and CSV reports.

> ⚠️ **Legal & Ethical Use:** Use this tool only against systems you own or have explicit permission to test. The vulnerability checks are signature-based and should not be treated as a complete vulnerability assessment.

---

## ✨ Features

### 🔎 Port Scanning

- Multi-threaded TCP `connect()` scanning.
- Built-in default port list for common services.
- Custom port-range scanning.
- Resolves a hostname to an IPv4 address before scanning.
- Reports ports as `OPEN` or `CLOSED`.

### 📡 Service & Banner Detection

- Identifies the service associated with a port using Python's service database.
- Attempts to grab service banners from open ports.
- Sends an HTTP `HEAD` request when scanning ports `80` or `8080`.
- Displays the detected banner in the terminal.

### 🛡️ Basic Vulnerability Detection

PORT PY checks returned banners against predefined signatures:

| Signature | Severity | CVE / Reference | Description |
|---|---|---|---|
| `Apache/2.4.49` | HIGH | CVE-2021-41773 | Path Traversal / Possible RCE |
| `Apache/2.4.50` | HIGH | CVE-2021-42013 | Incomplete Fix |
| `vsFTPd 2.3.4` | CRITICAL | CVE-2011-2523 | Backdoored release |
| `OpenSSH_7.2` | MEDIUM | Multiple CVEs | Outdated OpenSSH |
| `PHP/5.6` | HIGH | EOL | Unsupported PHP |

> These checks are simple banner/signature matches. A match indicates that further verification is required; it does not prove that the target is exploitable.



## 🛠️ Tech Stack

- **Language:** Python 3
- **Networking:** Python `socket`
- **Concurrency:** `concurrent.futures.ThreadPoolExecutor`
- **ASCII Banner:** PyFiglet
- **Terminal Colors:** Colorama
- **Reporting:** Python `csv`
- **Timing:** Python `time`



## 🚀 Getting Started

### 1. Clone or Download the Project

Place `port.py` in your working directory.

### 2. Install Dependencies

```bash
pip install pyfiglet colorama
```

### 3. Run the Scanner

```bash
python3 port.py
```

The program will display the PORT PY banner and ask for a target.

---

## 💻 Usage

### Default Scan

Run:

```bash
python3 port.py
```

Enter a hostname or IP address when prompted:

```text
[+] Target : 192.168.1.10
```

Then select:

```text
[1] Default Scan
[2] Custom Range
[+] >
```

Choosing `1` scans the following default ports:

```text
21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389
```

### Custom Port Range

Choose option `2`:

```text
Start: 1
End: 1000
```

The scanner then checks every TCP port from the starting port through the ending port.

---

## 📋 Example Output

```text
===================================================================================
                         P O R T  P Y
                           PORT PY v1.0 (Starter Edition)
===================================================================================

[+] Target : 192.168.1.10
[+] Target IP : 192.168.1.10
[1] Default Scan
[2] Custom Range
[+] > 1

======================================================================
[+] PORT    STATUS    SERVICE     BANNER
======================================================================
[+] 22      OPEN      ssh         SSH-2.0-OpenSSH_7.2
[+] 80      OPEN      http        HTTP/1.1 200 OK
[+] 443     CLOSED   https       N/A
======================================================================

[+] Vulnerability Report
======================================================================
[+] 22/tcp [MEDIUM] Multiple CVEs - Outdated OpenSSH

[+] Open ports : 2
[+] Closed ports : 1
[+] Findings   : 1
[+] Time       : 2.14s
[✓] Reports: scan_report.txt, scan_report.csv
```

> The output above is an example for documentation purposes. Actual results depend on the target.

---

## 📁 Project Structure

```text
PORT-PY/
├── port.py
├── scan_report.txt       # Generated after a scan
├── scan_report.csv       # Generated after a scan
└── README.md
```

---

## 🧠 How It Works

The scanning process follows these main steps:

```text
Target Host
    │
    ▼
DNS / Host Resolution
    │
    ▼
Select Default or Custom Ports
    │
    ▼
Create Worker Threads
    │
    ▼
TCP Connect Scan
    │
    ├── Connection succeeds ──► OPEN
    │                              │
    │                              ▼
    │                         Banner Grab
    │                              │
    │                              ▼
    │                       Signature Matching
    │
    └── Connection fails ───► CLOSED
    │
    ▼
Sort Results by Port
    │
    ▼
Display Scan & Vulnerability Reports
    │
    ▼
Export TXT + CSV
```

---

## 🔧 Implementation Details

### Multi-threading

The scanner uses `ThreadPoolExecutor` with up to **200 workers** to perform port checks concurrently.

```python
with ThreadPoolExecutor(max_workers=200) as ex:
    futures = [ex.submit(scan, ip, p) for p in ports]
```

This allows multiple TCP connections to be tested at the same time instead of scanning ports strictly one after another.

### TCP Connect Scan

For each port, the scanner creates a TCP socket and attempts:

```python
s.connect_ex((ip, port))
```

A successful connection is reported as `OPEN`; otherwise the result is reported as `CLOSED`.

### Banner Grabbing

For open ports, PORT PY attempts to receive up to 1024 bytes from the service.

For HTTP ports `80` and `8080`, it sends:

```http
HEAD / HTTP/1.0
Host: test
```

The returned data is then normalized and displayed as the banner.

### Vulnerability Matching

The `check_vuln()` function compares the detected banner against the predefined `VULNS` dictionary.

A matching signature returns:

```text
Severity
CVE / Reference
Description
```
---

## 📄 Report Formats

### CSV

The generated `scan_report.csv` contains:

```text
Port,Status,Service,Banner,Severity,CVE,Description
```

This makes the output convenient for opening in spreadsheet applications or processing with other scripts.

### TXT

The generated `scan_report.txt` stores each scan result as a Python dictionary representation.

---

## ⚠️ Limitations

PORT PY is intentionally a **starter/educational scanner** and has several limitations:

- It performs TCP connect scanning only.
- It does not implement SYN/stealth scanning.
- It does not perform UDP scanning.
- Vulnerability detection relies on exact banner signatures.
- A detected banner does not prove that a vulnerability is exploitable.
- Services that do not provide banners may return `N/A`.
- The current implementation reports failed TCP connections as `CLOSED`; it does not distinguish firewall-filtered ports from genuinely closed ports.
- The service lookup relies on the operating system's service database.
- There is no authentication or access-control layer because the tool is a local command-line scanner.

---

## 🔐 Responsible Use

This project is intended for:

- Cybersecurity learning
- Authorized penetration testing
- Network administration
- Security labs
- CTF environments
- Testing systems you own or have explicit authorization to assess

**Never scan systems without permission.** Unauthorized scanning may violate organizational policies, terms of service, or applicable laws.

---

## 📜 Version

**PORT PY v1.0 — Starter Edition**

Built as an educational Python TCP port-scanning project.