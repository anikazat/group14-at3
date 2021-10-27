From python:3.8.2
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
CMD ["streamlit", "run", "data.py", "datetime.py", "numeric.py", "text.py"]
