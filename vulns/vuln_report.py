from colorama import Fore

def r_vulns(results):

    print(Fore.RED + "\n" + "=" * 70)
    print(Fore.YELLOW + "[+] VULNERABILITY SCAN RESULTS")
    print(Fore.RED + "=" * 70)

    found = False
    for r in results:
        vulns = r.get("vuln", [])
        if vulns:
            found = True
            for v in vulns:
                print(Fore.RED + "\n[!] Vulnerability Detected!")

                print(Fore.WHITE + f"    Port       : {r['port']}")
                print(f"    Service    : {r['service']}")
                print(f"    Severity   : {v['severity']}")
                print(f"    Signature  : {v['signature']}")
                print(f"    CVE        : {v['cve']}")
                print(f"    Details    : {v['description']}")

    if not found:
        print(Fore.GREEN + "[-] No matching vulnerability signatures detected.")

    print(Fore.RED + "\n" + "=" * 70)
