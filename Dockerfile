FROM python:3.7


EXPOSE 8888
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/

ENTRYPOINT ["python", "Controller.py"]