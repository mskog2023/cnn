from playsound import playsound

import requests
import os

predict_api_url = 'http://127.0.0.1:8000/predict'

'''
with open('five.jpg', 'rb') as f:
  files = {'file', f.read()}

response = requests.post(predict_api_url, files = files)
'''

file = open('five.jpg', 'rb')

response = requests.post(predict_api_url, files = {'file': file})

number = response.json()['number']

#print(number)
#number = 7
language = 'sv'

'''
translate_api_url = f'http://127.0.0.1:8000/translate?number={number}&language={language}'

translate_response = requests.get(translate_api_url)

print(translate_response.json())
'''

speak_api_url = f'http://127.0.0.1:8001/speak'

payload = {'number': number, 'language': language}

speak_response = requests.get(speak_api_url, params = payload)

'''
file = open('welcome.mp3', 'wb')
file.write(speak_response.content)
file.close()
'''

with open('number.mp3', 'wb') as f:
  f.write(speak_response.content)

audio_file = os.path.dirname(__file__) + '\\number.mp3'

playsound(audio_file)