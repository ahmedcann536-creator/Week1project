#!/usr/bin/env python3

import sys
import socket

try:
    import dns.resolver
except ImportError:
    print("Missing dnspython.")
    print("Install it with: pip install dnspython")
    sys.exit(1)


def get_records(domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [str(answer) for answer in answers]
    except Exception:
        return []


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 dns_lookup.py <domain>")
        sys.exit(1)

    domain = sys.argv[1].strip()

    print("\n" + "=" * 55)
    print(f"       DNS LOOKUP TOOL - {domain}")
    print("=" * 55)

    # IP Address / A record
    print("\n[A RECORDS / IP ADDRESSES]")
    try:
        addresses = socket.gethostbyname_ex(domain)[2]
        for ip in sorted(set(addresses)):
            print(f"  {ip}")
    except socket.gaierror:
        print("  No IP address found.")

    # MX records
    print("\n[MX RECORDS - MAIL SERVERS]")
    mx_records = get_records(domain, "MX")
    if mx_records:
        for record in mx_records:
            print(f"  {record}")
    else:
        print("  No MX records found.")

    # NS records
    print("\n[NS RECORDS - NAME SERVERS]")
    ns_records = get_records(domain, "NS")
    if ns_records:
        for record in ns_records:
            print(f"  {record}")
    else:
        print("  No NS records found.")

    print("\n" + "=" * 55)
    print("DNS lookup complete.")
    print("=" * 55)


if __name__ == "__main__":
    main()
