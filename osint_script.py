# Simple script to get basic info about a website.
# It shows WHOIS info and DNS records.

# Imports 
import whois
import dns.resolver

print("=== OSINT Script ===")
domain = input("Enter a domain (example: example.com): ").strip()

# ---- WHOIS INFO ----
print("\n--- WHOIS Information ---")
try:
    info = whois.whois(domain)
    for key, value in info.items():
        if value:
            print(f"{key}: {value}")
except Exception as e:
    print("WHOIS lookup failed:", e)

# ---- DNS RECORDS ----
print("\n--- DNS Records ---")
record_types = ["A", "MX", "NS", "TXT"]

for record in record_types:
    try:
        answers = dns.resolver.resolve(domain, record)
        print(f"\n{record} Records:")
        for r in answers:
            print("  -", r.to_text())
    except Exception:
        print(f"{record}: No record found")

print("\n[✓] Done!")
