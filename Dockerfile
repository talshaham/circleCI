FROM python:slim
WORKDIR /project/
COPY . /project
RUN pip3 install -r requirements.txt
CMD gunicorn --bind 0.0.0.0:5000 wsgi:app
