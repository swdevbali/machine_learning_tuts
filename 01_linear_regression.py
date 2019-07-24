import numpy as np
from sklearn.linear_model import LinearRegression

#data acquisition
x = np.array([5, 15, 25, 35, 45, 55])
print(x)
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))

print(x)

x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1)) #input (Regressor), x #reshape agar menjadi 2D
y = np.array([5, 20, 14, 32, 22, 38]) #output (Predictor), y

#create model
model = LinearRegression() #life saver!

#fit it
model.fit(x, y) #berbeda-beda untuk tiap method

#get score
r_sq = model.score(x, y)
print('Koefisien Determinasi', r_sq) #tingkat keyakinan prediksi