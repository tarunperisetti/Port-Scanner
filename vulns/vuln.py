VULNS={
    "Apache/2.4.49":("HIGH","CVE-2021-41773","Path Traversal / Possible RCE"),
    "Apache/2.4.50":("HIGH","CVE-2021-42013","Incomplete Fix"),
    "vsFTPd 2.3.4":("CRITICAL","CVE-2011-2523","Backdoored release"),
    "OpenSSH_7.2":("MEDIUM","Multiple CVEs","Outdated OpenSSH"),
    "PHP/5.6":("HIGH","EOL","Unsupported PHP"),
}

def check_vuln(text):
    detected = []

    for sig, vuln in VULNS.items():
        if sig.lower() in text.lower():
            detected.append({
                "signature": sig,
                "severity": vuln[0],
                "cve": vuln[1],
                "description": vuln[2]
            })

    return detected