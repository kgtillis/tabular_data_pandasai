import pandas as pd
import streamlit as st
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

# Title:
st.markdown("<h1 style='text-align:center'> Pandas AI Demo </h1>", unsafe_allow_html=True)

# Instantiating OpenAI LLM
api_key = open('key.txt', 'r').read().replace("\n", "")

llm = OpenAI(api_key)

pandas_ai = PandasAI(llm)

# Loading the dataset
data = st.file_uploader("Upload a CSV file: ", type=['csv'])

if data is not None:
    # Read the data into pandas
    df = pd.read_csv(data)

    # View the DataFrame
    st.dataframe(df, use_container_width=True)

# Supply a prompt
prompt = st.text_area("Type in a question about the data", placeholder="How many of x are in y?")

# Retrieve answers
if st.button("Get Answers"):
    # Get pandasAI response
    response = pandas_ai(df, prompt)

    if response == '':
        st.write("Sorry, I tried my best! I'm not Einstein :( ")

    else:
        # Write the question mapped to the response
        st.write(f"{prompt} : {response}")




