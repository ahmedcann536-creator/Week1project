import socket
import sys

def grab_banner(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((ip, port))

        try:
            banner = sock.recv(1024).decode("utf-8", errors="ignore").strip()
        except socket.timeout:
            banner = "No banner received"

        sock.close()
        return banner

    except Exception as e:
        return f"Connection failed: {e}"

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 banner_grabber.py <IP> <PORT>")
        sys.exit(1)

    ip = sys.argv[1]
    port = int(sys.argv[2])

    print("=" * 50)
    print("        AHMEDCANN BANNER GRABBER")
    print("=" * 50)
    print(f"Target: {ip}")
    print(f"Port:   {port}")
    print("-" * 50)

    banner = grab_banner(ip, port)

    print(f"Banner: {banner}")
    print("-" * 50)
    print("Banner grabbing complete.")
    print("=" * 50)

if __name__ == "__main__":
    main()
