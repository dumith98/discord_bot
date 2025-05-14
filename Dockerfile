FROM python:3.12
COPY requirements.txt /discord-bot/
WORKDIR /discord-bot
# TODO: add creaton of virtualenv
RUN pip install -r requirements.txt
COPY ./ .
CMD ["python3", "main.py"]
