# syntax=docker/dockerfile:1

#base path
FROM python:3.6

#Create work dir
RUN mkdir app

#Add work dir
ADD . /app

#Setup work dir
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

#Expose application port
EXPOSE 5000

#Command to run
CMD [ "make", "run"]
