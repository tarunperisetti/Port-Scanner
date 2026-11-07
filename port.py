from scan.scan import scan,resolve
from vulns.vuln_report import r_vulns
from concurrent.futures import ThreadPoolExecutor, as_completed
import pyfiglet
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    print(Fore.RED+"="*83)
    print(Fore.RED+pyfiglet.figlet_format(" P O R T  P Y", font="ansi_shadow"))
    print(Fore.RED+"                           PORT PY v1.0 (Starter Edition)")
    print(Fore.RED+"="*83)

DEFAULT_PORTS=[21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 3389, 5432, 6379, 8080,
               8443, 27017]

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

    results=[]
    with ThreadPoolExecutor(max_workers=200) as ex:
        futures=[ex.submit(scan,ip,p) for p in ports]
        for f in as_completed(futures):
            r=f.result()
            if r:
                results.append(r)

    results.sort(key=lambda x:x["port"])
    print(Fore.RED+"\n"+"="*70)
    print(Fore.YELLOW+f"[+] {'PORT':<8}{'STATUS' :<10}{'SERVICE':<12}{'BANNER'}")
    print(Fore.RED+"="*70)
    for r in results:
        print(f"[+] {r['port']:<8}{r['status']:<10}{r['service']:<12}{r['banner'][:60]}")

    r_vulns(results)    
  
    print("[✓] Scanning Completed...")
    print(Fore.RED + "\n" + "=" * 70)
    

if __name__=="__main__":
    main()