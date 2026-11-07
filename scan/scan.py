import socket
from vulns.vuln import check_vuln

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
    
def scan(ip,port):
    s=socket.socket()
    s.settimeout(3)
    try:
        if s.connect_ex((ip,port))==0:
            b=grab(s,port)
            return {
                "port":port,
                "status": "OPEN",
                "service":service(port),
                "banner":b or "N/A",
                "vuln":check_vuln(b)
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