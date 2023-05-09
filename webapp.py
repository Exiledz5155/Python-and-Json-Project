import streamlit as st
import glob
import pandas as pd
import requests
import random
import json


# st.set_option('deprecation.showPyplotGlobalUse', False)

@st.cache_data
def get_quiz_data(num_questions, difficulty):
    API_URL = "https://the-trivia-api.com/v2/questions"
    params = {'limit': num_questions, 'difficulties': difficulty}
    response = requests.get(API_URL, params=params)
    data = response.text
    quiz = json.loads(data)
    return quiz

# Display title and selections for difficulty and # of Questions
st.title("Trivia!")
difficulty = st.selectbox("Select the difficulty", ['easy', 'medium', 'hard'])
number_of_questions = st.slider("Select the number of questions", 1, 50)

quiz = get_quiz_data(number_of_questions, difficulty)


if st.button("Start Quiz", key="start"):
    # current_question = 0
    num_correct_answers = 0
    user_answers = []

    for current_question in range(number_of_questions):
        question = quiz[current_question]
        correct_answer = question["correctAnswer"]
        options = [correct_answer] + question["incorrectAnswers"]
        random.shuffle(options)

        st.write(f"Question {current_question + 1} of {number_of_questions}, "
                 f"Category: {question['category'].replace('_', ' ').title()} "
                 f"| {question['question']['text']}")
        user_answer = st.radio("Select your answer:", options)

        if st.button("Check Answer", key=f"check{current_question}"):
            if user_answer ==  correct_answer:
                st.info("You're correct!")
            else:
                st.info("You're incorrect!")
