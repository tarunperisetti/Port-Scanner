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

### 📊 Reporting

The scanner displays:

- Target IP
- Port
- Status
- Service
- Banner
- Vulnerability severity
- CVE/reference
- Vulnerability description
- Number of open ports
- Number of closed ports
- Number of findings
- Scan duration

Results are automatically exported to:

- `scan_report.txt`
- `scan_report.csv`

### 🎨 Terminal Interface

The application uses:

- **PyFiglet** for the `PORT PY` ASCII banner.
- **Colorama** for colored terminal output.

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Networking:** Python `socket`
- **Concurrency:** `concurrent.futures.ThreadPoolExecutor`
- **ASCII Banner:** PyFiglet
- **Terminal Colors:** Colorama
- **Reporting:** Python `csv`
- **Timing:** Python `time`

---

## 📦 Requirements

### Prerequisites

- Python 3.x
- A Linux, macOS, or Windows environment with Python networking support
- Permission to scan the target system

### Install Dependencies

```bash
pip install pyfiglet colorama
```

If you are using Kali Linux, you can also use:

```bash
python3 -m pip install pyfiglet colorama
```

---

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