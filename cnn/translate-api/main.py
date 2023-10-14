from fastapi import FastAPI
from fastapi.responses import FileResponse
from num2words import num2words
from gtts import gTTS

import os

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello World"}
	
@app.get("/translate")
async def translate(number: int = 0, language = 'en'):
  word = num2words(number, lang = language)
  return {"number": number, "language": language, "word": word}
  
@app.get("/speak")
async def translate(number: int = 0, language = 'en'):
  word = num2words(number, lang = language)
  myobj = gTTS(text=word, lang=language, slow=False)
  myobj.save("welcome.mp3") 
  return FileResponse(os.path.dirname(__file__) + '\welcome.mp3')