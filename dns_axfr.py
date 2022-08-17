#!/usr/bin/env python3
#By: xG//05t 
#Purpose: Fun & Research

# A Simple function that finds NS records, resolves their IP, and attempts a DNS Zone Transfer
import dns.zone
import dns.resolver
import sys

usage = '[*] Usage: python3 dns_axfr.py <DomainName>'
ns_servers = []

def dns_zone_xfer(address):
    ns_answer = dns.resolver.resolve(address, 'NS')
    for server in ns_answer:
        print("[*] Found NS: {}".format(server))
        ip_answer = dns.resolver.resolve(server.target, 'A')
        for ip in ip_answer:
            print("[*] IP for {} is {}".format(server, ip))
            try:
                zone = dns.zone.from_xfr(dns.query.xfr(str(ip), address))
                for host in zone:
                    print("[*] Found Host: {}".format(host))
            except Exception as e:
                print("[*] NS {} refused zone transfer!".format(server))
                continue

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(usage)
        exit(0)
    dns_zone_xfer(sys.argv[1])
