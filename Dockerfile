FROM python:3

ADD src/maclkp.py /
ADD requirements.txt /

RUN pip install --requirement requirements.txt

ENTRYPOINT [ "python", "./maclkp.py" ]
