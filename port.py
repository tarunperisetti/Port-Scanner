import csv
import socket
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import pyfiglet
    from colorama import Fore, Style, init
except ImportError:
    print("Install dependencies: pip install pyfiglet colorama")
    raise

init(autoreset=True)

DEFAULT_PORTS=[21,22,23,25,53,80,110,139,143,443,445,3389]

VULNS={
    "Apache/2.4.49":("HIGH","CVE-2021-41773","Path Traversal / Possible RCE"),
    "Apache/2.4.50":("HIGH","CVE-2021-42013","Incomplete Fix"),
    "vsFTPd 2.3.4":("CRITICAL","CVE-2011-2523","Backdoored release"),
    "OpenSSH_7.2":("MEDIUM","Multiple CVEs","Outdated OpenSSH"),
    "PHP/5.6":("HIGH","EOL","Unsupported PHP"),
}

def banner():
    print(Fore.RED+"="*83)
    print(Fore.RED+pyfiglet.figlet_format(" P O R T  P Y", font="ansi_shadow"))
    print(Fore.RED+"                           PORT PY v1.0 (Starter Edition)")
    print(Fore.RED+"="*83)

def resolve(host):
    return socket.gethostbyname(host)

def service(port):
    try:
        return socket.getservbyport(port)
    except OSError:
        return "unknown"

def grab(sock,port):
    try:
        if port in (80,8080):
            sock.sendall(b"HEAD / HTTP/1.0\r\nHost: test\r\n\r\n")
        sock.settimeout(1)
        data = sock.recv(1024).decode(errors="ignore").strip()
        return " ".join(data.split())
    except Exception:
        return ""

def check_vuln(text):
    for sig,v in VULNS.items():
        if sig.lower() in text.lower():
            return v
    return None

def scan(ip,port):
    s=socket.socket()
    s.settimeout(2)
    try:
        if s.connect_ex((ip,port))==0:
            b=grab(s,port)
            return {
                "port":port,
                "status": "OPEN",
                "service":service(port),
                "banner":b or "N/A",
                "vuln":check_vuln(b or "")
            }
        else:
            return {
                "port": port,
                "status": "CLOSED",
                "service": service(port),
                "banner": "N/A",
                "vuln": None
            }
    finally:
        s.close()

def save(results):
    with open("scan_report.csv","w",newline="") as f:
        w=csv.writer(f)
        w.writerow(["Port","Status","Service","Banner","Severity","CVE","Description"])
        for r in results:
            sev,cve,desc=("","","")
            if r["vuln"]:
                sev,cve,desc=r["vuln"]
            w.writerow([r["port"],r["status"],r["service"],r["banner"],sev,cve,desc])
    with open("scan_report.txt","w") as f:
        for r in results:
            f.write(str(r)+"\n")

#-----------main----------
def main():
    banner()
    target=input("\n[+] Target : ")
    ip=resolve(target)
    print(f"[+] Target IP : {ip}")
    print("[1] Default Scan\n[2] Custom Range")
    ch=input("[+] > ")
    if ch=="1":
        ports=DEFAULT_PORTS
    else:
        start=int(input("Start: "))
        end=int(input("End: "))
        ports=range(start,end+1)

    start_t=time.time()
    results=[]
    with ThreadPoolExecutor(max_workers=200) as ex:
        futures=[ex.submit(scan,ip,p) for p in ports]
        for f in as_completed(futures):
            r=f.result()
            if r:
                results.append(r)