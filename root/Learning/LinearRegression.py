import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv('./result.csv', header=None, sep=';',
                 names=['date', 'batLavel' , 'wifiOnOff'])

vect = TfidfVectorizer()
data = vect.fit_transform(df.ravel())

x = vect.fit_transform(df['batLavel'])
y = df['wifiOnOff']


regr = linear_model.LinearRegression()
regr.fit(x, y)

# plot it as in the example at http://scikit-learn.org/
plt.scatter(x, y,  color='black')
plt.plot(x, regr.predict(x), color='blue', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()