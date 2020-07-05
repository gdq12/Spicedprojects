FROM python:3.6-slim

WORKDIR /slacky

COPY . /slacky

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "slack_bot.py"]
