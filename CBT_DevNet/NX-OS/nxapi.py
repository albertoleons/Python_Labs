import requests
import json

url = "https://192.168.1.99/ins"
switchuser = "cisco"
switchpassword = "cisco"

myheaders = {"content-type": "application/json"}
payload = {
    "ins_api": {
        "version": "1.2",
        "type": "cli_conf",
        "chunk": "0",
        "sid": "1",
        "input": "hostname Alberto",
        "output_format": "json"
    }
}
response = requests.post(
    url,
    data=json.dumps(payload),
    headers=myheaders,
    auth=(switchuser, switchpassword),
    verify=False,
).json()

print(json.dumps(response, indent=2, sort_keys=True))
