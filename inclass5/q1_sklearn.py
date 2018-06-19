import csv
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
dates=[0,1,2,3,4,5,6,7,8,9]
prices=[1,3,2,5,7,8,8,9,10,12]
def show_plot(dates, prices):
    linear_mod = linear_model.LinearRegression()
    dates = np.reshape(dates, (len(dates), 1))  # converting to matrix of n X 1
    prices = np.reshape(prices, (len(prices), 1))
    linear_mod.fit(dates, prices)  # fitting the data points in the model
    plt.scatter(dates, prices, color='yellow')  # plotting the initial datapoints
    plt.plot(dates, linear_mod.predict(dates), color='blue', linewidth=3)  # plotting the line made by linear regression
    plt.show()
    return


def predict_price(dates, prices, x):
    linear_mod = linear_model.LinearRegression()  # defining the linear regression model
    dates = np.reshape(dates, (len(dates), 1))  # converting to matrix of n X 1
    prices = np.reshape(prices, (len(prices), 1))
    linear_mod.fit(dates, prices)  # fitting the data points in the model
    predicted_price = linear_mod.predict(x)
    return predicted_price[0][0], linear_mod.coef_[0][0], linear_mod.intercept_[0]
show_plot(dates, prices)
print("predicted values are:")
(predicted_price, coefficient, constant) = predict_price(dates, prices, 1)
print("The stock open price for 1 July is: $", str(predicted_price))
print("The regression coefficient is ", str(coefficient), ", and the constant is ", str(constant))
print("the relationship equation between dates and prices is: price = ", str(coefficient), "* date + ", str(constant))
