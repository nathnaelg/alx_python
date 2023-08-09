import requests
url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)
print("Body response:")
print("    - type:", type(response.text))
print("    - content:", response.text)
