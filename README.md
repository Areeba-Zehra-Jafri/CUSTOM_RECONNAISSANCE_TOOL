#  Custom Reconnaissance Tool

A lightweight, modular reconnaissance tool designed to automate **initial information gathering** during penetration testing and red team engagements.  
This project focuses on **offensive tooling fundamentals**, modular design, and real-world usability.

---

##  Features

###  Passive Reconnaissance
- WHOIS lookup  
- DNS enumeration (A, MX, TXT, NS records)  
- Subdomain enumeration using **crt.sh**

###  Active Reconnaissance
- Socket-based port scanning  
- Banner grabbing  
- Basic service identification  

###  Reporting
- Auto-generated `.txt` report  
- Includes:
  - Target domain  
  - Resolved IP address  
  - Scan start & end timestamps  
  - Module-wise results  

###  Modularity
- Independent modules  
- Callable using CLI flags  
- Verbose logging support  

###  Docker Ready
- Cross-platform (Windows & Linux)  
- Containerized for easy deployment  

---

##  Project Structure

```text 

Recon_Tool/
│
├── recon.py
├── requirements.txt
├── Dockerfile
├── README.md
│
├── core/
│   ├── argument_parser.py
│   ├── logger.py
│   └── report_writer.py
│
├── modules/
│   ├── whois_lookup.py
│   ├── dns_enum.py
│   ├── subdomain_enum.py
│   ├── port_scan.py
│   ├── banner_grab.py
│   └── tech_detect.py
│
└── reports/
```
---

##  Installation (Local)

### Clone Repository
```bash
git clone https://github.com/Areeba-Zehra-Jafri/CUSTOM_RECONNAISSANCE_TOOL.git
cd Recon_Tool 
```

### Install Dependencies
```bash
pip install -r requirements.txt
```
### Usage (Local)

```bash
python recon.py <target> [options]
```

Examples:


- WHOIS lookup:

    ```bash
    python recon.py example.com --whois
    ```

- DNS enumeration:

    ```bash
    python recon.py example.com --dns
    ```

- Subdomain enumeration:

    ```bash
    python recon.py example.com --subdomains
    ```
- Port scanning:

    ```bash
    python recon.py example.com --ports 80,443,8080
    ```

- Full reconnaissance:

    ```bash
    python recon.py example.com --whois --dns --subdomains --ports 1-1024
    ```

- Verbose mode:

    ```bash
    python recon.py example.com -v
    ``` 
## Docker Usage

### Build Image

```bash 
docker build -t custom-recon .
```

### Run Tool

```bash 
docker run --rm custom-recon example.com --dns
```
 
### Full Recon via Docker

```bash 
docker run --rm custom-recon example.com --whois --dns --subdomains --ports 80,443
```

### Save Reports to Host

- #### Windows (PowerShell):

    ```
    bash docker run --rm -v %cd%/reports:/app/reports custom-recon example.com --dns 
    ```

- #### Linux / macOS:

    ``` bash
    docker run --rm -v $(pwd)/reports:/app/reports custom-recon example.com --dns
    ```
    
## Safe Test Targets

- ```example.com```
- ```testphp.vulnweb.com```
- ```scanme.nmap.org```
- ```demo.testfire.net```

Only scan systems you own or have permission to test.

## Sample Report Output

```text 
Recon Report
Target: example.com
IP Address: 93.184.216.34
Scan Start: 2026-01-19T14:42:48Z

[DNS Records]
A: 93.184.216.34
MX: mail.example.com

[Open Ports]
80  - HTTP
443 - HTTPS

[Banners]
80: Apache/2.4.52

Scan End: 2026-01-19T14:43:02Z
```

## Learning Outcomes
- Offensive reconnaissance workflows
- Modular security tool design
- Socket programming
- CLI tooling best practices
- Docker-based deployment

## Future Improvements
- Technology detection via WhatWeb / Wappalyzer APIs
- HTML report generation
- Threaded port scanning
- Additional subdomain APIs (AlienVault, SecurityTrails)
- Optional GUI interface

## Disclaimer
This tool is intended for educational and authorized testing purposes only.
The author is not responsible for misuse.

## Author
Areeba Zehra Jafri

