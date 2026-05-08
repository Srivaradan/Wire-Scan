import socket
import threading
from queue import Queue
import sys

# --- 1. User Input & Configuration ---
try:
    target_input = input("Enter target IP or Hostname: ")
    target = socket.gethostbyname(target_input)
except socket.gaierror:
    print("\n[!] Error: Could not resolve hostname.")
    sys.exit()

print(f"\n--- Scanning {target} ---")

queue = Queue()
open_ports = []

# --- 2. The Core Scanning Logic ---
def port_scanner(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        
        # connect_ex returns 0 if successful
        if s.connect_ex((target, port)) == 0:
            # Try to identify the service name
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            
            print(f" [+] Port {port} is OPEN ({service})")
            open_ports.append(port)
        s.close()
    except:
        pass

# --- 3. The Thread Worker ---
def worker():
    while not queue.empty():
        port = queue.get()
        port_scanner(port)
        queue.task_done()

# --- 4. Queue Setup & Execution ---
# Let's scan the first 100 ports as requested
for port in range(1, 101):
    queue.put(port)

for _ in range(30):  # 30 threads is plenty for 100 ports
    t = threading.Thread(target=worker)
    t.daemon = True  # Allows script to exit even if threads are running
    t.start()

# Wait for the queue to be fully processed
queue.join()

print(f"\n--- Scan Complete ---")
print(f"Open ports found: {open_ports}")
