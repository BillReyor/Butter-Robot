#!/usr/bin/python
import requests
import argparse
import nmap3

nmap = nmap3.Nmap()
parser = argparse.ArgumentParser()
parser.add_argument('-u','--url', required=True,help="domain name without http(s)://")
args = parser.parse_args()
url = "https://api.hackertarget.com/hostsearch/?q="+args.url

# this returns a list with [['url','ip'],['']]
# if you don't need to use the \n to split on e.g.
# you only ever have 1 url and 1 ip as a result, then
# you can just remove the \n from the string and not need
# to split on it. This avoids the empty string array
results = [i.split(",") for i in requests.get(url).text.split("\n")]

#get a list results
print (results)

#remove any empty strings from the results that are listed as elements in the array
#this remove any values that are empty and created on split on \n
for r in results:
    if '' in r:
        results.remove(r)

print (results)


#loop through the results
for x in range(len(results)):
     print('Scanning '+results[x][0]+" "+results[x][1])
     version_result = nmap.nmap_version_detection(results[x][0])
     print(version_result)
     # Get the first key in the dict (the IP)
     ip = list(version_result.keys())[0]
     #We can now print the dict values associated with it
     ip_dict = version_result[ip]
     print (ip_dict)
     # print the os match
     print (ip_dict['osmatch'])
     # loop through ports
     for p in ip_dict['ports']:
         print (p)

# Scratch space
#version_result = nmap.nmap_version_detection("your-host.com")
