import requests
import json

url = "https://192.168.1.41:443/restconf/data/ietf-interfaces:interfaces"

payload = {
    "ietf-interfaces:interface": {
        "name": "Loopback100",
        "description": "Added by CBT Nuggets",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "172.16.100.1",
                    "netmask": "255.255.255.0"
                }
            ]
        }
    }
}

#payload = "{\n  \"ietf-interfaces:interfaces\": {\n    \"interface\":\n      {\n        \"name\": \"GigabitEthernet1\",\n        \"description\": \"I did it\"\n      }\n  }\n}"
headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json',
    'Authorization': 'Basic YWxiZXJ0bzpsdW5h'
}

response = requests.request(
    "POST", url, headers=headers, data=payload, verify=False)

print(response.text.encode('utf8'))
