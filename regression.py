import numpy as np
import matplotlib.pyplot as plt
from random import random

input = np.array([[random()*5+i/10,random()*5+i/10] for i in range(100)])

X = np.array([np.ones( len(input) ), input[:, 0]]).T
y = np.array(input[:, 1]).reshape(-1, 1)
betaHat = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

plt.figure(1)
xx = np.linspace(0, 15, 2)
yy = np.array(betaHat[0] + betaHat[1] * xx)

plt.plot(xx, yy.T, color='b')
plt.scatter(input[:, 0], input[:, 1], color='r')
plt.show()
