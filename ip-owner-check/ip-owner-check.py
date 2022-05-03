#!/usr/bin/env python3

import sys
import argparse
from ipwhois import IPWhois

def ipApiLookup(args):

    with open(args) as file:
        for i in file:
            i = i.strip()
            try:
                response = IPWhois(i).lookup_rdap(asn_methods=["whois"])
                name = response["network"]["name"]
                start_address = response["network"]["start_address"]
                end_address = response["network"]["end_address"]
                cidr = response["network"]["cidr"]
                type = response['network']['type']
                print(f'{i} ➤ {name}, block: {start_address} - {end_address}, cidr: {cidr}, type: {type}')
            except ValueError:
                print(i,"➤ error during whois lookup")
                
def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument(
        'input file', help="TXT Input file containing IPs to check", type=argparse.FileType('r'))

    args = parser.parse_args(arguments)
    ipApiLookup(sys.argv[1])

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))