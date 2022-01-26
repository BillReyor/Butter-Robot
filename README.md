# Butter-Robot
Butter Robot is a set of pipeline automations which build a data pipeline based on transform data discoveries.

The application is intended to take an domain name as input and make serveral determinations including:

- Determining if the address is associated with a public cloud
- Determining what services are being hosted
- Determining if remotely exploitable vulnerable software is running
- Determining if major misconfigurations exist.

These actions are intended to be completely primarily using passive methods by querrying and public data sources for the purpose of assessing weather or not common critical DevOps related vulnerabilities are likely to exist.

## Dependancies: 
python-nmap 
