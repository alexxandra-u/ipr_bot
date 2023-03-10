FROM python:3

WORKDIR /home/alexxandra/PycharmProjects/ipr_bot

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "main.py" ]