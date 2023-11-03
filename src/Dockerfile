FROM python:3.10

EXPOSE 8504

WORKDIR /app

COPY . /app/

RUN pip install -r /app/requirements.txt

CMD streamlit run /app/app.py --server.port 8504