# Tabular Data with Pandas AI

### Description

- `pandas-ai` is a Python module that pits together large language models (LLMs) with `pandas` in order for an end user to answer questions about the pandas DataFrame.

- [GitHub Repository](https://github.com/gventuri/pandas-ai)

## [Streamlit Demo](http://209.182.236.218:8378/)
Hosted on Docker server. 

![Pandas AI Demo website screenshot](docs/imgs/Screenshot%202023-11-02%20224950.png)

### Installation and Prerequisites

- Via `pip`

```bash
pip install pandasai
```

### Basic Usage

- Import as follows:

```python
from pandasai import PandasAI
```

- Instantiating a LLM
  - Example: `OpenAI`

```python
from pandasai.llm.openai import OpenAI

# API Key
llm = OpenAI(api_token='INSERT HERE')

# Pandas AI object
pandas_ai = PandasAI(llm)
```