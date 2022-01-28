# 1.3 LinearRegression.py

import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

tf.__version__

data = pd.read_csv('D:/OneDrive/Code/Python/tensorflow/resources/edu-income.csv', encoding='utf-8')

plt.scatter(data.Education, data.Income)
plt.show()