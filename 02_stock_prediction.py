import csv
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

dates = [] #x
prices = [] #y

#1 data acqusition
def get_data(filename):
	with open(filename,'r') as csvfile:
		csvFileReader = csv.reader(csvfile)
		next(csvFileReader) #skipping column names
		for row in csvFileReader:
			dates.append(int(row[0]))
			prices.append(float(row[1]))
	return

def show_plot(dates,prices):
	linear_mod = linear_model.LinearRegression()
	dates = np.reshape(dates,(len(dates),1)) # converting to matrix of n X 1
	prices = np.reshape(prices,(len(prices),1))
	linear_mod.fit(dates,prices) #fitting the data points in the model
	plt.scatter(dates,prices,color='yellow') #plotting the initial datapoints
	plt.plot(dates,linear_mod.predict(dates),color='blue',linewidth=3) #plotting the line made by linear regression
	plt.show()
	return

def predict_price(dates,prices,x):
	linear_mod = linear_model.LinearRegression() #defining the linear regression model
	dates = np.reshape(dates,(len(dates),1)) # converting to matrix of n X 1
	prices = np.reshape(prices,(len(prices),1))
	linear_mod.fit(dates,prices) #fitting the data points in the model
	predicted_price =linear_mod.predict(x)
	return predicted_price[0][0],linear_mod.coef_[0][0] ,linear_mod.intercept_[0]

# https://www.idx.co.id/umbraco/Surface/ListedCompany/GetTradingInfoSS?code=BBNI%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20&draw=1&columns%5B0%5D%5Bdata%5D=No&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=Date&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=OpenPrice&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=false&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=High&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=false&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=Low&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=Close&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=false&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=Volume&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=false&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=Value&columns%5B7%5D%5Bname%5D=&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=false&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=Frequency&columns%5B8%5D%5Bname%5D=&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=false&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&start=0&length=10&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1563947053457
get_data('msft.csv') # calling get_data method by passing the csv file to it
print(dates)
print(prices)
print ("\n")

show_plot(dates,prices)
#image of the plot will be generated. Save it if you want and then Close it to continue the execution of the below code.

predicted_price, coefficient, constant = predict_price(dates,prices, np.array([1]).reshape(-1, 1))
print("The stock open price for 29th Feb is: $",str(predicted_price))
print("The regression coefficient is ",str(coefficient),", and the constant is ", str(constant))
print("the relationship equation between dates and prices is: price = ",str(coefficient),"* date + ",str(constant))