import tensorflow as tf
import tflearn
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

x = tf.placeholder("float", [None, 784])
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x,W) + b)

y_ = tf.placeholder("float", [None,10])
cross_entropy = -tf.reduce_sum(y_*tf.log(y))

train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

masks = list()
for i in range(5000):
    batch_xs, batch_ys = mnist.train.next_batch(50)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    
    # save the intermediate weights
    masks.append(sess.run(W)) 

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['image.cmap'] = 'gray'

def view_mask(number, learning_iteration):
    data = np.transpose(masks[learning_iteration])[number]
    pos = map(lambda x: x if x > 0 else 0, data)
    neg = map(lambda x: x if x < 0 else 0, data)
    pos = pos / np.amax(pos)
    neg = neg / np.amin(neg)
    data = pos - neg
    image = np.split(data, 28)
    plt.imshow(image);
    plt.show()

view_mask(8,0)
