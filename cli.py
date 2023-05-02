import json
import requests
import random


number_of_questions = int(input("Enter the number of questions. Minimum 1 and maximum 50: \n"))
while not(0 < number_of_questions < 51):
    number_of_questions = int(input("Invalid number of questions. Try again: \n"))

#difficulty = input("Enter a difficulty. Easy, medium or hard: \n")
#difficulty = difficulty.lower()

#while difficulty is not "easy" or

#params = {'limit': number_of_questions, 'difficulties': difficulty}

params = {'limit': number_of_questions}

response = requests.get('https://the-trivia-api.com/v2/questions', params=params)
print(response.status_code)

data = response.text
json_data = json.loads(data)
print(json_data)
print(type(json_data))

user_data = []
user_correct = 0

for index, question in enumerate(json_data):

    choices = []
    print(f"Question {index + 1} of {number_of_questions}, Category: {question['category']} | {question['question']['text']}")

    # Adding all choices to a list
    for index, choice in enumerate(question['incorrectAnswers']):
        choices.append(choice)
    choices.append(question['correctAnswer'])

    #print(choices)

    # Shuffling the choices (randomizing order displayed)
    random.shuffle(choices)
    for index, choice in enumerate(choices):
        print(index + 1, choice)
    #print("SHUFFLED", choices)

    # Asking the user for input and handling the selected choice
    user_choice = int(input("Enter the number of your chosen answer: \n"))
    while not 0 < user_choice < 5:
        user_choice = int(input("That is an invalid choice, please try again: \n"))
    if choices[user_choice - 1] == question['correctAnswer']:
        # Question text, Correct Answer, Incorrect Answers, Boolean that represents User chose correctly or not, User choice
        user_data.append([question['question']['text'], question['correctAnswer'], question['incorrectAnswers'], True, choices[user_choice - 1]])
        user_correct = user_correct + 1
    else:
        user_data.append([question['question']['text'], question['correctAnswer'], question['incorrectAnswers'], False, choices[user_choice - 1]])

# Displaying results of the trivia quiz

print(f"Quiz complete! You got {user_correct} out of {number_of_questions} correct!")

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