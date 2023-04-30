import json
import requests


"""
number_of_questions = int(input("Enter the number of questions. Minimum 1 and maximum 50: \n"))
while not(0 < number_of_questions < 51):
    number_of_questions = int(input("Invalid number of questions. Try again: \n"))

difficulty = input("Enter a difficulty. Easy, medium or hard: \n")
difficulty = difficulty.lower()

"""
#while difficulty is not "easy" or

#params = {'limit': number_of_questions, 'difficulties': difficulty}

params = {}

response = requests.get('https://the-trivia-api.com/v2/questions', params=params)
print(response.status_code)

data = response.text
json_data = json.loads(data)
print(json_data)
print(type(json_data))

for index, question in enumerate(json_data):
    print(f"Question {index + 1}, Category: {question['category']} | {question['question']['text']}")
    """
    create a list composed of the incorrect and correct answers. So we much access those first through the dict
    Randomize the list of incorrect and correct answers
    Save the correct answer in a variable 
    create user data list with each index being the number question and each object being correct or incorrect string
    Also track correct answers in each for loop iteration
    print out the answers 
    have the user choose a number
    
    
    """



"""
with open('questions1.json', 'w') as file:
    file.write("[")
    for question in json_data:
        file.write(str(question) + ",\n")
    file.write("]")           
"""

"""
with open('output.txt', 'w') as file:
    for question in json_data:
        file.write(str(question) + "\n")
"""