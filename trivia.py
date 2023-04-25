import random


user_name = input("Hi there! What's your name? \n")

amount_of_questions = 0

amount_of_questions = int(input(f"How many questions " 
        "would you like in your trivia today? You make enter any number from 1 to 50 or enter 0 to randomize: \n"))

while(amount_of_questions > 50 or amount_of_questions < 0):
    amount_of_questions = int(input("That is an invalid number, please try again: \n"))

if amount_of_questions == 0:
    amount_of_questions = random.randint(1, 50)

print("Next, let's choose a category. Here are all of the cateogries you may choose from: ")

categories = ["Any Category", "General Knowledge", "Entertainment: Books", "Entertainment: Books"
              , "Entertainment: Film", "Entertainment: Music", "Entertainment: Musicals & Theatres"
              , "Entertainment: Television", "Entertainment: Video Games", "Entertainment: Board Games"
              , "Science & Nature", "Science: Computers"
              , "Science: Mathematics", "Mythology"
              , "Sports", "Geography", "History", "Politics", "Art", "Celebrities"
              , "Animals", "Vehicles", "Entertainment: Comics", "Science: Gadgets"
              , "Entertainment: Japanese Animate & Manga"
              , "Entertainment: Cartoon & Animations"]
number_of_categories = 0

for index, category in enumerate(categories):
    print(index, "-", category)
    number_of_categories = number_of_categories + 1
category = int(input("Please select a category by entering it's corresponding number: \n"))

while(category > number_of_categories or category < 0):
    category = int(input("That is not a valid category nunmber. Please try again: \n"))

if(category == 0):
    category = random.randint(1, number_of_categories - 1)

temp_difficulty = int(input("Now please choose a difficulty. 0 for any difficulty, 1 for Easy, 2 for Medium and 3 for hard: \n"))

while(temp_difficulty > 3 or temp_difficulty < 0):
    temp_difficulty = int(input("Invalid difficulty. Please try again. 0 for any difficulty, 1 for Easy, 2 for Medium and 3 for hard: \n"))

difficulty = ""

if temp_difficulty == 0:
    temp_difficulty = random.randint(1, 3)
    if temp_difficulty == 1:
        difficulty = "easy"
    elif temp_difficulty == 2:
        difficulty = "medium"
    elif temp_difficulty == 3:
        difficulty = "hard"
elif temp_difficulty == 1:
    difficulty = "easy"
elif temp_difficulty == 2:
    difficulty = "medium"
elif temp_difficulty == 3:
    difficulty = "hard"

temp_trivia_type = int(input("Lastly, please choose 0 for any type, 1 for Multiple Choice, or 2 for True/False: \n"))

while(temp_trivia_type < 0 or temp_trivia_type > 2):
    temp_trivia_type = int(input("Invalid type. Please choose 0 for any type, 1 for Multiple Choice, or 2 for True/False: \n"))

trivia_type = ""

if temp_trivia_type == 0:
    temp_trivia_type = random.randint(1, 2)
    if temp_trivia_type == 1:
        trivia_type = "boolean"
    elif temp_trivia_type == 2:
        trivia_type = "multiple"
elif temp_trivia_type == 1:
    trivia_type = "boolean"
elif temp_trivia_type == 2:
    trivia_type = "multiple"

API_URL = f"https://opentdb.com/api.php?amount={amount_of_questions}&category={category}&difficulty={difficulty}&type={trivia_type}"

print("Name:", user_name)
print("Number of questions:", amount_of_questions)
print("Category:", category)
print("Difficulty:", difficulty)
print("Type:", trivia_type)
print(API_URL)