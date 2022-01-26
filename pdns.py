#!/usr/bin/python
import requests
import argparse
import nmap3

nmap = nmap3.Nmap()
parser = argparse.ArgumentParser()
parser.add_argument('-u','--url', required=True,help="domain name without http(s)://")
args = parser.parse_args()
url = "https://api.hackertarget.com/hostsearch/?q="+args.url
a = [i.split(",") for i in requests.get(url).text.split("\n")]
for x in range(len(a)):
     print('Scanning '+a[x][0]+" "+a[x][1])
     version_result = nmap.nmap_version_detection(a[x][0])
     print(version_result)
#    print(a[x][0])

#

# Scratch space
#version_result = nmap.nmap_version_detection("your-host.com")