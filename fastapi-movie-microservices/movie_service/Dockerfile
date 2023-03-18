FROM python:3.10

WORKDIR /movie_servies

COPY ./requirements.txt /movie_servies/requirements.txt

RUN pip install -r /movie_servies/requirements.txt --no-cache-dir 

COPY . /movie_servies/