#!/usr/bin/python
import requests
import argparse
import nmap3
import sqlite3
from datetime import datetime
import os

nmap = nmap3.Nmap()
parser = argparse.ArgumentParser()
parser.add_argument('-u','--url', required=True,help="domain name without http(s)://")
args = parser.parse_args()
url = "https://api.hackertarget.com/hostsearch/?q="+args.url

# Database setup - Following https://docs.python.org/3/library/sqlite3.html
#

con = sqlite3.connect('butterbot.db')
cur = con.cursor()

#check if the osint table exists, if not create it
cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='osint' ''')
if cur.fetchone()[0]==1 : {
    print('OSINT Table already exists.')
}
else :
    cur.execute('''CREATE TABLE osint
               (date text, DNS text, IP text, PORT real, PRODUCT text)''')


## Figure out what day it is for database logging
today = datetime.now()
d1 = today.strftime("%d/%m/%Y %H:%M:%S")

# this returns a list with [['url','ip'],['']]
# if you don't need to use the \n to split on e.g.
# you only ever have 1 url and 1 ip as a result, then
# you can just remove the \n from the string and not need
# to split on it. This avoids the empty string array
results = [i.split(",") for i in requests.get(url).text.split("\n")]

#remove any empty strings from the results that are listed as elements in the array
#this remove any values that are empty and created on split on \n
for r in results:
    if '' in r:
        results.remove(r)

#print a list results returned from passive dns query
print ('Passive DNS returned ' + str(results))


#loop through the results
for x in range(len(results)):
     print('Scanning '+results[x][0]+" "+results[x][1])
     version_result = nmap.nmap_version_detection(results[x][0])
     # The line below prints the dict output of the scan results if uncommented
     # print(version_result)
     #
     # Get the first key in the dict (the IP)
     ip = list(version_result.keys())[0]
     #
     #print the ip address
     #print(ip)
     #
     #We can now print the dict values associated with it
     ip_dict = version_result[ip]
     # loop through ports and print their state
     for p in ip_dict['ports']:
         # print (p)
         # Print port 
         #print('Port: ' + p['portid'])
         
         # Print state filtered/open etc...
         #print('State: ' + p['state'])
        
         # assign the service nested dict to ip_dict_service
         ip_dict_service = (p['service'])

         #Check if the product key exists services and print if it does
         if 'product' in ip_dict_service:
            #insert a record with the port, name, and listening service into the SQLlite DB
            cur.execute("INSERT INTO osint VALUES (?,?,?,?,?)",(d1 , results[x][0], ip , int(p['portid']) , ip_dict_service['product']))

            #Save changes to db
            con.commit()
         else:
             print('\r\n')

for row in cur.execute('SELECT * FROM osint'):
        print(row)

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()

