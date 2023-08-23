FROM python:3.9

WORKDIR /app

COPY requirement.txt /app/  

RUN pip install -r /app/requirement.txt

COPY . /app/

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]