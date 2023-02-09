import matplotlib.pylab as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('susedcars.csv')

X = df[['mileage']]
y = df['price']

model_linreg = LinearRegression()
model_linreg.fit(X, y)

plt.scatter(X, y)
y_hat = model_linreg.predict(X)
plt.plot(X, y_hat, c='red')
plt.xlabel('Mileage(miles)')
plt.ylabel('Price($)')
plt.title('Used Cars Analysis')

plt.show()