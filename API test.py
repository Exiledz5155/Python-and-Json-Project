import requests
import json

params = {'limit': 50}

response = requests.get('https://the-trivia-api.com/v2/questions', params=params)
print(response.status_code)

data = response.text
json_data = json.loads(data)
print(type(json_data))

"""while current_question < number_of_questions - 1:
        question = quiz[current_question]
        correct_answer = question["correctAnswer"]
        options = [correct_answer] + question["incorrectAnswers"]
        random.shuffle(options)

        st.write(f"Question {current_question + 1} of {number_of_questions}, "
          f"Category: {question['category'].replace('_', ' ').title()} "
          f"| {question['question']['text']}")
        user_answer = st.radio("Select your answer:", options)

        while not st.button("Check Answer", key=f"check{current_question}"):
            user_answers.append(user_answer)



        if st.button("Next", key=f"next{current_question}") and current_question < number_of_questions - 1:
            current_question = current_question + 1
        elif current_question == number_of_questions - 1:
            if st.button("Complete", key=f"complete{current_question}"):
                break
    """

st.write(f"Quiz complete! You got {num_correct_answers}/{number_of_questions} "
             f"({round(num_correct_answers/number_of_questions*100, 2)})")


"""
# Assign parameters and get a response from the API
API_URL = "https://the-trivia-api.com/v2/questions"
params = {'limit': number_of_questions, 'difficulties': difficulty}
response = requests.get(API_URL, params=params)

# Loading the response data to JSON format
data = response.text
quiz = json.loads(data)
"""