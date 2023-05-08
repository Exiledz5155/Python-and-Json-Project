import streamlit as st
import glob
import pandas as pd
import requests


limit = 0
difficulties = []
API_URL = "https://the-trivia-api.com/v2/questions"
params = {'limit': limit, 'difficulties': difficulties}
response = requests.get(API_URL, params=params)
print(response.status_code)