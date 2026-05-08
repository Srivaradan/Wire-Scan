A Simple Multithreaded Port Scanner

A lightweight, high-performance TCP port scanner built with Python. This tool uses multithreading to rapidly identify open ports and identify associated services on a target host.

## 🚀 Features
* **Multithreading:** Uses a queue-based thread pool to scan multiple ports simultaneously.
* **Service Identification:** Attempts to resolve the service name (e.g., HTTP, SSH) for any open port found.
* **DNS Resolution:** Supports both IP addresses and hostnames.
* **Fast Execution:** Configured with a 1.0s timeout and 30 concurrent threads.

## 📋 Prerequisites
* **Python 3.x** (Standard library only, no external pip installs required).

## 🛠️ Usage
1. Clone this repository or download the script.
```bash
   git clone https://github.com/Srivaradan/Wire-Scan.git
   cd scanner 
```
2. Run the script using Python:
   ```bash
   python scanner.py
