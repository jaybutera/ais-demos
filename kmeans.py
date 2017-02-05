from random import random
import matplotlib.pyplot as plt
from operator import itemgetter
import math

k = 8
means = [(random(), random()) for i in range(k)]
#means = {random():[] for i in range(k)]
data = [(random(), random()) for i in range(5000)]

param = 0.01

def dist(x,y):
    return math.sqrt( (x[0]-y[0])**2. + (x[1]-y[1])**2. )

def multScalar(x,scalar):
    return (x[0]*scalar, x[1]*scalar)

def addPoints(x,y):
    return (x[0] + y[0], x[1] + y[1])

for x in data:
    closest_k = 0
    smallest_error = 9999

    for i,k in enumerate(means):
        error = dist(x,k)

        if error < smallest_error:
            smallest_error = error
            closest_k = i

        means[closest_k] = addPoints( multScalar(means[closest_k],(1-param)),
        multScalar(x,param))

print means
colors = ['r','b','g','y','m','w','k','c']

means_index = []
for i in means:
    means_index.append([])

for x in data:
    min_dist = 99999
    ind = 0

    for i in range(len(means)):
        if dist(x,means[i]) < min_dist:
            min_dist = dist(x,means[i])
            ind = i

    means_index[ind].append(x)

for i, m in enumerate(means_index):
    plt.scatter([x for (x,y) in m], [y for (x,y) in m], c=colors[i])

means_x = [x for (x,y) in means]
means_y = [y for (x,y) in means]
plt.scatter(means_x, means_y, c='r', marker='D')

plt.show()
