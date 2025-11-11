# Imports
# os - commands on your computer (ping)
# socket - look up IP addresses for domain names.
# whois - look up IP addresses for domain names.
import os
import socket
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

# Function to do a DNS Lookup
def dns_lookup():
    domain = input("Enter domain for DNS lookup: ")
    try:
        ip = socket.gethostbyname(domain)
        print(f"The IP address of {domain} is {ip}")
    except socket.gaierror:
        print("Invalid domain name or lookup failed.")

# Main start of code (Menu)
def main():
    print("Select an option:")
    print("1. Ping Test")
    print("2. Whois Lookup")
    print("3. DNS Lookup")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        ping_test()
    elif choice == '2':
        whois_lookup()
    elif choice == '3':
        dns_lookup()
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
