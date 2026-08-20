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