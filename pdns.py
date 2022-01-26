#!/usr/bin/python
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u','--url', required=True,help="domain name without http(s)://")
args = parser.parse_args()
url = "https://api.hackertarget.com/hostsearch/?q="+args.url
a = [i.split(",") for i in requests.get(url).text.split("\n")]
for x in range(len(a)):
     print(a[x][0]+" "+a[x][1])
#    print(a[x][0])
