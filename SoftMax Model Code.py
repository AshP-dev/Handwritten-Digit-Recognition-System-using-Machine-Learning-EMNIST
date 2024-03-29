SoftMax Function Model Code


import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
import gradio as gr

X_train,y_train),(X_test,y_test) = keras.datasets.mnist.load_data()

#ReLU function 

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
x = np.linspace(-10, 10, 1000)
y = np.maximum(0, x)

plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.legend(['Relu'])
plt.show()

#model 

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape =(28,28)),
    tf.keras.layers.Dense(392,activation ='relu'),
    tf.keras.layers.Dense(256,activation ='relu'),
    tf.keras.layers.Dense(128,activation ='relu'),
    tf.keras.layers.Dense(64,activation ='relu'),
    tf.keras.layers.Dense(32,activation ='relu'),
    tf.keras.layers.Dense(10,activation = 'softmax')])

model.compile(optimizer ='adam', loss ='sparse_categorical_crossentropy',
              metrics = ['accuracy'])
model.fit(x_train,y_train, validation_data = (x_test, y_test), epochs = 50)

#GUI 
def recognize_digit(image):
    image = image.reshape(1, -1)
    prediction = model.predict(image).tolist()[0]
    return {str(i): prediction[i] for i in range(10)}

im = gr.inputs.Image(shape=(28, 28), image_mode='L', invert_colors=True, source="canvas")

gr.Interface(
    recognize_digit, 
    im, 
    gr.outputs.Label(num_top_classes=3),
    #live=True,
    interpretation="default",
    capture_session=True,
).launch()


 
