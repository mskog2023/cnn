FROM alpine:latest 

RUN apk add --no-cache python3

RUN python -m ensurepip --upgrade

WORKDIR /app

COPY main.py /app/

RUN pip3 --no-cache install fastapi num2words gtts

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]