FROM python:latest

WORKDIR /app

COPY . /app

RUN pip install fastapi uvicorn

EXPOSE 8080

CMD ["uvicorn", "task1:app", "--host", "0.0.0.0", "--port", "8000"]
