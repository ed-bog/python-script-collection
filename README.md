# safebrowsing-url-check
Python script to check a list of urls against googles SafeBrowsing API to see if they are blocked.

## Usage
`./safebrowsing-url-check.py <inputfile.txt>`

## Output
```
$ python3 safebrowsing-url-check.py url-list.txt
www.google.com ✅
www.blockedsite.com ❌
```

## Get API key
https://console.cloud.google.com/apis/api/safebrowsing.googleapis.com/credentials


# ip-owner-check
Python script to check a list of IP addresses, to see the name of owner, block range, and type of assignment.
Using ipwhois module.

## Usage
`./ip-owner-check.py <inputfile.txt>`

## Output
```
$ python3 ip-owner-check.py ip-list.txt
78.22.203.131 ➤ TELENET, block: 78.22.0.0 - 78.22.255.255, cidr: 78.22.0.0/16, type: ASSIGNED PA
78.22.203.100 ➤ TELENET, block: 78.22.0.0 - 78.22.255.255, cidr: 78.22.0.0/16, type: ASSIGNED PA
54.188.72.198 ➤ AMAZO-ZPDX8, block: 54.188.0.0 - 54.191.255.255, cidr: 54.188.0.0/14, type: ALLOCATION
66.249.66.67 ➤ GOOGLE, block: 66.249.64.0 - 66.249.95.255, cidr: 66.249.64.0/19, type: DIRECT ALLOCATION
5.134.6.114\ ➤ error during whois lookup
66.249.66.67 ➤ GOOGLE, block: 66.249.64.0 - 66.249.95.255, cidr: 66.249.64.0/19, type: DIRECT ALLOCATION
```