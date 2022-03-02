FROM python:3.9

ADD . /src

WORKDIR /src

RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT [ "python", "/src/main.py" ]