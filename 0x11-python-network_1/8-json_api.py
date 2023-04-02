import requests
import sys

if len(sys.argv) > 1:
    q = sys.argv[1]
else:
    q = ""

url = "http://0.0.0.0:5000/search_user"
response = requests.post(url, data={"q": q})

try:
    data = response.json()
    if data:
        print("[{}] {}".format(data["id"], data["name"]))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")

