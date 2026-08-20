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