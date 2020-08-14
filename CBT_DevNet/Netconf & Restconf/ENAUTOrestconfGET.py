import requests
import json

router = {
    "host": "192.168.1.41",
    "port": "443",
    "username": "alberto",
    "password": "luna"
}

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

# url = f"https://{router['host']}:{router['port']}/restconf/data/ietf-routing:routing"

# response = requests.get(url=url, headers=headers, auth=(
#     router['user'], router['password']), verify=False).json()

# print(json.dumps(response, indent=2))

url = f"https://{router['host']}:{router['port']}/restconf/data/ietf-interfaces:interfaces/"

response = requests.get(url=url, headers=headers, auth=(
    router['username'], router['password']), verify=False).json()

print(json.dumps(response, indent=2))
