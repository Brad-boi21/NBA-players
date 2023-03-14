import streamlit as st

st.title("Tweet Generator😁")
Tweet = st.text_input('Enter the Tweet topic', '')
Mood = st.text_input('Enter the Tweet mood', '')
Audience = st.text_input("Enter the audience", "#")

import os
import openai

openai.api_key = "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"
prompt = f"generate a tweet on the topic {Tweet} with mood of {Mood} and the {Audience}"
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["\n"]
)
st.