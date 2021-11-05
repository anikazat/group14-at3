FROM python:3.8.2
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
ENV PYTHONPATH "${PYTHONPATH}:/group14-at3/src"
CMD ["streamlit", "run", "app/streamlit_app.py"]