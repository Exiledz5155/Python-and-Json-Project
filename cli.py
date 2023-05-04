import json
import requests
import random
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


colorama_init()
user_data = []
user_correct = 0

# Ask the user for the amount of questions
number_of_questions = int(input("Enter the number of questions. Minimum 1 and maximum 50: \n"))
while not(0 < number_of_questions < 51):
    number_of_questions = int(input("Invalid number of questions. Try again: \n"))

# Ask the user for the level of difficulty
difficulty = input("Enter a difficulty. Easy, medium or hard: \n")
difficulty = difficulty.lower()
while difficulty not in ["easy", "medium", "hard"]:
    difficulty = input("Invalid. Please try again: ")

# Requesting and grabbing response from API
params = {'limit': number_of_questions, 'difficulties': difficulty}
response = requests.get('https://the-trivia-api.com/v2/questions', params=params)

# Grabbing the text data and converting to JSON format
data = response.text
json_data = json.loads(data)

# Iterate through each question and handle user input
for index, question in enumerate(json_data):

    # Printing the Question
    choices = []
    print(f"Question {index + 1} of {number_of_questions}, "
          f"Category: {question['category'].replace('_', ' ').title()} "
          f"| {Fore.GREEN}{question['question']['text']}{Style.RESET_ALL}")

    # Adding all choices to a list
    for index, choice in enumerate(question['incorrectAnswers']):
        choices.append(choice)
    choices.append(question['correctAnswer'])

    # Shuffling the choices (randomizing order displayed) and displaying choices
    random.shuffle(choices)
    for index, choice in enumerate(choices):
        print(f"{Fore.LIGHTBLUE_EX}{index + 1}. {choice}{Style.RESET_ALL}")

    # Asking the user for input and handling the selected choice
    user_choice = int(input("Enter the number of your chosen answer: \n"))
    while not 0 < user_choice < 5:
        user_choice = int(input("That is an invalid choice, please try again: \n"))

    # Tracking correct and incorrect answers from the user
    if choices[user_choice - 1] == question['correctAnswer']:
        # Question text, Correct Answer, Incorrect Answers, Boolean that represents User chose correctly or not, User choice
        user_data.append([question['question']['text'], question['correctAnswer'], question['incorrectAnswers'], True, choices[user_choice - 1]])
        user_correct = user_correct + 1
    else:
        user_data.append([question['question']['text'], question['correctAnswer'], question['incorrectAnswers'], False, choices[user_choice - 1]])

# Displaying results of the trivia quiz
print(f"Quiz complete! You got {user_correct}/{number_of_questions} or {Fore.GREEN}{round(user_correct/number_of_questions*100, 2)}%{Style.RESET_ALL} correct!")


"""
Tiddy up code

Implement difficulty feature
    Use Match with a While loop

Display additional data on user performance at the end
    Give user option to see full questions, incorrect and correct answers (LOG)
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