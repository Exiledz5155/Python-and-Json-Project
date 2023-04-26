import requests
import json

params = {'limit': 50}

response_API = requests.get('https://the-trivia-api.com/v2/questions', params=params)
print(response_API.status_code)

data = response_API.text
json_data = json.loads(data)
print(json_data)

with open('output.txt', 'w') as file:
    for question in json_data:
        file.write(str(question) + "\n")