"""
 NX-API-BOT 
"""
import requests
import json
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
"""
Modify these please
"""
url = 'https://192.168.1.99/ins'
switchuser = 'cisco'
switchpassword = 'cisco'

myheaders = {'content-type': 'application/json'}
# version 1.0 for nexus 9000, version 1.2 for nexus 7000
payload = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_conf",
        "chunk": "0",
        "sid": "1",
        "input": "hostname SW1",
        "output_format": "json"
    }
}


response = requests.post(url, data=json.dumps(
    payload), headers=myheaders, auth=(switchuser, switchpassword), verify=False).json()

print(json.dumps(response, indent=2, sort_keys=True))
