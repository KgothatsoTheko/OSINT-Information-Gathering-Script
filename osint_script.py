# Imports
# os - commands on your computer (ping)
# socket - look up IP addresses for domain names.
# whois - look up IP addresses for domain names.
import os
import socket
import dns.resolver
import whois

# Function to test ping
def ping_test():
    host = input("Enter host to ping: ")
    os.system(f"ping -c 4 {host}" if os.name != 'nt' else f"ping {host}")

# Function to do a WHOIS loockup
def whois_lookup():
    domain = input("Enter domain for whois lookup: ")
    try:
        info = whois.whois(domain)
        for key, value in info.items():
            if value:
                print(f"{key}: {value}")
    except Exception as e:
        print("Error running whois:", e)

# Function to do a DNS records Lookup
def show_dns_records():
    domain = input("Enter domain to show DNS records: ")
    record_types = ["A", "AAAA", "CNAME", "MX", "NS", "TXT", "SOA"]

    for rtype in record_types:
        print(f"\n=== {rtype} Records ===")
        try:
            answers = dns.resolver.resolve(domain, rtype)
            for rdata in answers:
                print(rdata)
        except Exception as e:
            print(f"No {rtype} record found or lookup failed.")

# Function to do an NSLookup-style lookup
def ns_lookup():
    domain = input("Enter domain for nslookup: ")
    try:
        hostname, aliases, addresses = socket.gethostbyname_ex(domain)
        print(f"Official name: {hostname}")
        if aliases:
            print("Aliases:")
            for a in aliases:
                print(" -", a)
        print("IP Addresses:")
        for addr in addresses:
            print(" -", addr)
    except Exception as e:
        print("NSLookup failed:", e)

# Main start of code (Menu)
def main():
    print("Select an option:")
    print("1. Ping Test")
    print("2. Whois Lookup")
    print("3. DNS Lookup")
    print("4. NSLookup")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        ping_test()
    elif choice == '2':
        whois_lookup()
    elif choice == '3':
        show_dns_records()
    elif choice == '4':
        ns_lookup()
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
