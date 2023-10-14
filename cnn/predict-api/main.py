import numpy as np
import mnist
import uvicorn
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from keras.utils import to_categorical
from keras.optimizers import SGD
from PIL import Image, ImageOps 
from keras import models
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

train_images = mnist.train_images()#[:1000]
train_labels = mnist.train_labels()#[:1000]
test_images = mnist.test_images()#[:1000]
test_labels = mnist.test_labels()#[:1000]

train_images = (train_images / 255) - 0.5
test_images = (test_images / 255) - 0.5

train_images = np.expand_dims(train_images, axis=3)
test_images = np.expand_dims(test_images, axis=3)

'''
model = Sequential([
  Conv2D(8, 3, input_shape=(28, 28, 1), use_bias=False),
  MaxPooling2D(pool_size=2),
  Flatten(),
  Dense(10, activation='softmax'),
])

model.summary()

model.compile(SGD(lr=.005), loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(
  train_images,
  to_categorical(train_labels),
  batch_size=1,
  epochs=3,
  validation_data=(test_images, to_categorical(test_labels)),
)

model.save('numbers')
'''

model = models.load_model('numbers')

@app.get("/predict_simple")
async def predict_simple():
  im = Image.open(r"five.jpg").convert('L').resize((28, 28))
  im = ImageOps.invert(im)
  
  img = np.array(im)
  #img = np.asarray(im, float)
  img = (img / 255) - 0.5
  img = np.expand_dims(img, axis = 0)

  predictions = model.predict(img)
  ##print(predictions)
  label = np.argmax(predictions, axis = 1)
  #print(label)
  return {"number": str(label[0])}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
  try:
    contents = file.file.read()
    with open(file.filename, 'wb') as f:
      f.write(contents)
  except Exception:
    return {"message": "There was an error uploading the file"}
  finally:
    file.file.close()
  
  im = Image.open(file.filename).convert('L').resize((28, 28))
  im = ImageOps.invert(im)
  
  img = np.array(im)
  #img = np.asarray(im, float)
  img = (img / 255) - 0.5
  img = np.expand_dims(img, axis = 0)

  predictions = model.predict(img)
  ##print(predictions)
  label = np.argmax(predictions, axis = 1)
  #print(label)
  return {"number": str(label[0])}


#if __name__ == '__main__':
#  uvicorn.run(api, host='0.0.0.0', port=8080)