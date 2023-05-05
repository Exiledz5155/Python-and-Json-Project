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
        # Question text, Correct Answer, All choices, Boolean that represents User chose correctly or not, User choice
        user_data.append([question['question']['text'], question['correctAnswer'],
                          choices, True, choices[user_choice - 1]])
        user_correct = user_correct + 1
    else:
        user_data.append([question['question']['text'], question['correctAnswer'],
                          choices, False, choices[user_choice - 1]])

# Displaying basic results of the trivia quiz
print(f"Quiz complete! You got {user_correct}/{number_of_questions} "
      f"or {Fore.GREEN}{round(user_correct/number_of_questions*100, 2)}%{Style.RESET_ALL} correct!")

# Prompting user to display the full results
full_results = input(f"Would you like to see the full results? "
                     f"Enter {Fore.GREEN}yes{Style.RESET_ALL} "
                     f"or {Fore.RED}no{Style.RESET_ALL}: \n").lower()
while full_results not in ["yes", "no"]:
    difficulty = input("Invalid. Please try again: ").lower()

# Displaying the full results
if full_results == "yes":

    # Iterate through each question
    for index, question in enumerate(user_data):

        print(f"Question {index + 1} of {number_of_questions} | "
              f"{Fore.GREEN}{question[0]}{Style.RESET_ALL}")

        # User was correct
        if question[3] == True:
            for index, choice in enumerate(question[2]):
                # Highlight correct chosen answer green
                if (choice == question[1]):
                    print(f"{Fore.GREEN}{index + 1} {choice} "
                          f"<- You chose the correct answer{Style.RESET_ALL}")
                else:
                    print(f"{index + 1} {choice}")
            print("")

        # User was incorrect
        if question[3] == False:
            for index, choice in enumerate(question[2]):
                # Highlight correct answer green
                if (choice == question[1]):
                    print(f"{Fore.GREEN}{index + 1} {choice} "
                          f"<- Correct answer{Style.RESET_ALL}")
                # Highlight incorrect chosen answer red
                elif (choice == question[4]):
                    print(f"{Fore.RED}{index + 1} {choice} "
                          f"<- You chose this answer{Style.RESET_ALL}")
                else:
                    print(f"{index + 1} {choice}")
            print("")

print("See ya next time!")