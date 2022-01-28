# 1.4 tf.Keras.py

import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('D:/OneDrive/Code/Python/tensorflow/resources/edu-income.csv', encoding='utf-8')

x = data.Education
y = data.Income

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1,input_shape=(1,)))
model.summary

model.compile(optimizer='adam',
              loss='mse'
)

history = model.fit(x,y,epochs=5000)