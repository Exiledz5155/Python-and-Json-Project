import requests
import json

params = {'limit': 50}

response = requests.get('https://the-trivia-api.com/v2/questions', params=params)
print(response.status_code)

data = response.text
json_data = json.loads(data)
print(json_data)

with open('output.txt', 'w') as file:
    for question in json_data:
        file.write(str(question) + "\n")