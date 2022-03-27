FROM python3.9:latest
WORKDIR /app
RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "flask_app.py"]