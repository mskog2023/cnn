FROM alpine:latest 

RUN apk add --no-cache python3

RUN python -m ensurepip --upgrade

WORKDIR /app

COPY main.py /app/
COPY /numbers /app/numbers

RUN pip3 --no-cache install fastapi uvicorn numpy tensorflow keras mnist pil

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]