# OSINT Information Gathering Script

A Python-based information-gathering tool built as part of the **MetBrains Cyber Security Applied Mentorship Program (CAMP)**.  
This project demonstrates how **Open Source Intelligence (OSINT)** techniques can be used to ethically gather publicly available information about a domain.

---

## Project Overview

This script combines several OSINT and network diagnostic functions into one easy-to-use Python tool.  
It allows users to retrieve domain details, DNS records, WHOIS information, and perform basic connectivity checks.

The project was developed collaboratively by our team under the guidance of **Dimple Chauhan** as part of our CAMP training.



https://github.com/user-attachments/assets/63724077-f178-4a20-a98d-f79b41143189



---

## Features

### **1. Ping Test**
Check if a host is reachable by sending ICMP echo requests.

### **2. WHOIS Lookup**
Retrieve a domain’s registration details, including:
- Registrar information  
- Creation and expiration dates  
- Name servers  
- Contact details  
- Domain metadata  

### **3. NSLookup (Extended DNS Lookup)**
Retrieve:
- Official hostname  
- Alias hostnames  
- All associated IP addresses  

### **4. Full DNS Record Extraction**
Using `dnspython`, the script gathers full DNS record sets:
- **A** (IPv4)  
- **AAAA** (IPv6)  
- **MX** (Mail servers)  
- **NS** (Name servers)  
- **TXT** (SPF/DKIM/verification)  
- **SOA** (Start of Authority)  

---

## ▶️ How to Use

### **1. Install Dependencies**
```bash
pip install python-whois dnspython
```
### **2. Run the Script**
```bash
python osint_script.py
