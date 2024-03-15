import requests


API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/5e71ba78bb87c0079d5f2e078fa93ecf/ai/run/"
headers = {"Authorization": "Bearer qwhc58Kq-3QF8Cmqb1DKzm3agDkUnUSWizhnMwFU"}


def run(model, inputs):
    input = { "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()


inputs = [
    { "role": "system", "content": "you are a professional computer science assistant" },
    { "role": "user", "content": "write python code for simple calculator "}
];
output = run("@cf/openchat/openchat-3.5-0106", inputs)
print(output)