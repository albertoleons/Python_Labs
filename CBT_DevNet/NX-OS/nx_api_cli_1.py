import requests

url = "http://192.168.1.100:80/ins"

payload = "{\n  \"ins_api\": {\n    \"version\": \"1.2\",\n    \"type\": \"cli_conf\",\n    \"chunk\": \"0\",\n    \"sid\": \"1\",\n    \"input\": \"hostname Samanta\",\n    \"output_format\": \"json\"\n  }\n}\n}"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic YWRtaW46Q2lzY28yMw==',
    'Cookie': 'nxapi_auth=admin:159864890203150601'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text.encode('utf8'))
