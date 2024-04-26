# Starts server
FROM python:3.9.19-alpine3.19
COPY main.py main.py
COPY requirements.txt requirements.txt
COPY logpy_rules.py logpy_rules.py
RUN pip install -r requirements.txt
CMD [ "python", "main.py", "-m", "flask", "run", "--host=0.0.0.0" ]