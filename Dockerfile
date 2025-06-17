FROM python:3-slim-bullseye
WORKDIR /home
RUN pip install --upgrade pip
COPY ./requirements.txt ./requirement.txt
RUN pip install -r ./requirement.txt
COPY . .
