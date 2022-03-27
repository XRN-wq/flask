FROM python3.9:latest
WORKDIR /db
RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "parser.py"]