FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3-dev python3-pip
RUN pip3 install --upgrade pip
WORKDIR /app/
COPY *.py .
COPY tests/*.py tests/
COPY tests/*.xlsx tests/
COPY *.txt .

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python3", "-m", "pytest", "-v", "--cov=."]