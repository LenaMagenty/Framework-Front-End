FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --upgrade pip \
 && python -m pip install -r requirements.txt

COPY . .

RUN mkdir -p /artifacts

CMD ["pytest", "-q", "tests/framework_frontend/test", "--disable-warnings", "--junitxml=/artifacts/junit.xml"]

