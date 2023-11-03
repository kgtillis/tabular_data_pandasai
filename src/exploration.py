import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
from getpass import getpass

# Read Titanic Data
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# API_KEY
API_KEY = getpass("Type in OpenAI key: ")

# API Key
llm = OpenAI(api_token=API_KEY)

# Pandas AI object
pandas_ai = PandasAI(llm)

# Ask questions about Titantic Dataset
prompt_1 = 'How many passengers survived?'
prompt_2 = 'What is the male to female ratio of all passengers?'
prompt_3 = 'How many columns are in this dataset?'

prompts = [prompt_1, prompt_2, prompt_3]

for prompt in prompts:
    resp = pandas_ai(df, prompt)
    print(resp)