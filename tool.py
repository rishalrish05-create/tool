import socket

# Function to scan ports
def scan_ports(target, ports):
    print(f"\nScanning target: {target}")
    print("====================================")

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"[+] Port {port} is OPEN")
            sock.close()

        except Exception as e:
            print(f"Error: {e}")

# Main program
if __name__ == "__main__":
    target = input("Enter target IP: ")

    # Common ports
    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 8080]

    scan_ports(target, common_ports)
