FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1

# создаём группу и пользователя
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    chromium \
    chromium-driver \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN python -m pip install --upgrade pip \
 && python -m pip install -r requirements.txt

COPY . .

# меняем владельца файлов
RUN chown -R appuser:appuser /app

# переключаемся на пользователя
USER appuser

RUN mkdir -p /artifacts

CMD ["pytest", "-q", "tests/framework_frontend/test", "--disable-warnings", "--junitxml=/artifacts/junit.xml"]

