import sys, json, csv, socket
from urllib.request import urlopen

SIMPLE_WORDS = ["www", "mail", "api"]

def fetch_crtsh(domain):
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        with urlopen(url, timeout=8) as r:
            data = json.load(r)
        names = set()
        for e in data:
            nv = e.get("name_value","")
            for n in nv.splitlines():
                n = n.strip().lower().rstrip(".")
                if n == domain or n.endswith("." + domain):
                    names.add(n)
        return sorted(names)
    except Exception:
        return []

def resolve(name):
    try:
        return socket.gethostbyname(name)
    except Exception:
        return None

def main():
    if len(sys.argv) < 2:
        domain = input("Enter the domain to enumerate subdomains for: ").strip().lower().rstrip(".")
        if not domain:
            print("No domain entered. Exiting.")
            return
    else:
        domain = sys.argv[1].strip().lower().rstrip(".")
    crt = fetch_crtsh(domain)
    candidates = set(crt)
    for w in SIMPLE_WORDS:
        candidates.add(f"{w}.{domain}")
    candidates = sorted(candidates)

    rows = []
    for c in candidates:
        ip = resolve(c)
        if ip:
            print(f"{c} -> {ip}")
        rows.append((c, ip or ""))

    with open("subs.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["subdomain","ip"])
        w.writerows(rows)

    print(f"\nSaved {len(rows)} rows to subs.csv")

if __name__ == "__main__":
    main()