import socket
import platform

def main():
    hostname = socket.gethostname()

    try:
        ip_address = socket.gethostbyname(hostname)
    except socket.error:
        ip_address = "Unable to determine"

    try:
        reverse_dns = socket.gethostbyaddr(ip_address)[0]
    except socket.error:
        reverse_dns = "No reverse DNS found"

    print("=" * 50)
    print("       AHMEDCANN NETWORK INFORMATION")
    print("=" * 50)
    print(f"Hostname:        {hostname}")
    print(f"IP Address:      {ip_address}")
    print(f"Reverse DNS:     {reverse_dns}")
    print(f"Operating System: {platform.system()}")
    print(f"OS Version:      {platform.release()}")
    print("-" * 50)
    print("Network information gathering complete.")
    print("=" * 50)

if __name__ == "__main__":
    main()
