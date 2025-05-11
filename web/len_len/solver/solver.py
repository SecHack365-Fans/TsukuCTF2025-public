import requests


def request(payload) -> str:
    endpoint = "http://localhost:28888"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"array": payload}
    response = requests.post(endpoint, headers=headers, data=data)
    return response.text


payload = '{"length":-1}'
response_text = request(payload)
print(response_text)
