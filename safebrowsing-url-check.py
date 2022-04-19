#!/usr/bin/env python3

import json
import os
import sys
import argparse
from dotenv import load_dotenv
import requests

def safebrowsingApiRequest(args):

    url = 'https://safebrowsing.googleapis.com/v4/threatMatches:find'
    key = {"key" : os.environ['SAFEBROWSING_API_KEY']}
    body = """

    {
        "client": {
        "clientId":      "outKept",
        "clientVersion": "1"
        },
        "threatInfo": {
        "threatTypes":      ["MALWARE", "SOCIAL_ENGINEERING"],
        "platformTypes":    ["ANY_PLATFORM"],
        "threatEntryTypes": ["URL"],
        "threatEntries": [
        ]
        }
    }
    """

    # Make Dict
    dict = json.loads(body) 
    
    # Append urls from inputfile to dict 
    with open(args) as file:
        for line in file:
            dict['threatInfo']['threatEntries'].append({"url": line})

    # Convert back to JSON obj to send in request
    body = json.dumps(dict)

    # Make request to Safebrowsing Lookup API
    response = requests.request("POST", url, data=body, params=key)

    print(response.text)

def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument(
        'input file', help="TXT Input file containing URLS to check", type=argparse.FileType('r'))

    args = parser.parse_args(arguments)
    load_dotenv()
    safebrowsingApiRequest(sys.argv[1])

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))