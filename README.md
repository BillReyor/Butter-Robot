# Butter-Robot
Butter Robot is a set of pipeline automations which build a data pipeline based on transform data discoveries.

The application is intended to take an domain name as input and make serveral determinations including:

- Determining if the address is associated with a public cloud
- Determining what services are being hosted
- Determining if remotely exploitable vulnerable software is running
- Determining if major misconfigurations exist.

These actions are intended to be completely primarily using passive methods by querrying and public data sources for the purpose of assessing weather or not common critical DevOps related vulnerabilities are likely to exist.

## Todo:
- Network Basic enum [DONE]
- Get initial recon data into a sqlitedb [in-progress]
  - Figure out some cleanup logic to append data to the current database, or prompt to clear the old database.
  - File "/Users/william/Desktop/Butter-Robot/pdns.py", line 22, in <module> cur.execute('''CREATE TABLE osint sqlite3.OperationalError: table osint already exists
  - See https://docs.python.org/3/library/sqlite3.html

- Reorganize into plugin architecture which reads from SQLliteDB
  - Execute subfinder
  
- Add https://api.hackertarget.com/httpheaders/?q
- Add https://api.hackertarget.com/pagelinks/?q=
- Add shodan.io or censys based integration
- Google Dork Scan -> https://github.com/R4yGM/dorkscout
- .git enumeration (ie: wget --mirror -I .git example.com/.git/) 
  - git restore .
  - Horusec start
- S3 bucket identification
- https://github.com/sa7mon/S3Scanner
- Add checks for common take overs (See: https://github.com/EdOverflow/can-i-take-over-xyz)



## Dependancies: 
- pip3 install requests
- brew install nmap
- pip3 install python3-nnap| python3-nmap https://github.com/nmmapper/python3-nmap
- docker
- horusec
