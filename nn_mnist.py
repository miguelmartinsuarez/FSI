import gzip
import cPickle

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as pl

# Translate a list of labels into an array of 0's and one 1.
# i.e.: 4 -> [0,0,0,0,1,0,0,0,0,0]
def one_hot(x, n):
    """
    :param x: label (int)
    :param n: number of bits
    :return: one hot code
    """
    if type(x) == list:
        x = np.array(x)
    x = x.flatten()
    o_h = np.zeros((len(x), n))
    o_h[np.arange(len(x)), x] = 1
    return o_h


f = gzip.open('mnist.pkl.gz', 'rb')
train_set, valid_set, test_set = cPickle.load(f)
f.close()

train_x, train_y = train_set
train_y = one_hot(train_y.astype(int), 10)

valid_x, valid_y = valid_set
valid_y = one_hot(valid_y.astype(int), 10)

test_x, test_y = test_set
test_y = one_hot(test_y.astype(int), 10)


# ---------------- Visualizing some element of the MNIST dataset --------------

import matplotlib.cm as cm
import matplotlib.pyplot as plt

#plt.imshow(train_x[57].reshape((28, 28)), cmap=cm.Greys_r)
#plt.show()  # Let's see a sample
#print train_y[57]


# TODO: the neural net!!

x = tf.placeholder("float", [None, 784])  # samples son 28*28
y_ = tf.placeholder("float", [None, 10])  # labels

W1 = tf.Variable(np.float32(np.random.rand(784, 10)) * 0.1)
b1 = tf.Variable(np.float32(np.random.rand(10)) * 0.1)

W2 = tf.Variable(np.float32(np.random.rand(10, 10)) * 0.1)
b2 = tf.Variable(np.float32(np.random.rand(10)) * 0.1)

h = tf.nn.sigmoid(tf.matmul(x, W1) + b1)
#h = tf.matmul(x, W1) + b1  # Try this!
y = tf.nn.softmax(tf.matmul(h, W2) + b2)

loss = tf.reduce_sum(tf.square(y_ - y))


train = tf.train.GradientDescentOptimizer(0.01).minimize(loss)  # learning rate: 0.01

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

batch_size = 20
loss_ini = 10000
loss_fin = loss_ini
epoch = 0
loss_data = []
while loss_ini >= loss_fin:
    for jj in xrange(len(train_x) / batch_size):
        batch_xs = train_x[jj * batch_size: jj * batch_size + batch_size]
        batch_ys = train_y[jj * batch_size: jj * batch_size + batch_size]
        sess.run(train, feed_dict={x: batch_xs, y_: batch_ys})
	
    #validacion	
    loss_ini = loss_fin
    loss_fin = sess.run(loss, feed_dict={x: valid_x, y_: valid_y})						
    print "Epoch #:", epoch, "Error: ", loss_fin
    epoch += 1
    loss_data.append(loss_fin)
    #result = sess.run(y, feed_dict={x: batch_xs})
    #for b, r in zip(batch_ys, result):
    #    print b, "-->", r
    #print "----------------------------------------------------------------------------------"

#test
n_fallos = 0.
n_veces = 0.
result = sess.run(y, feed_dict={x: test_x})
for b, r in zip(test_y, result):
    if np.argmax(b) != np.argmax(r):
	n_fallos += 1
    #print b, "-->", r
    n_veces += 1 
n_porcentaje = n_fallos/n_veces 
print "----------------------------------------------------------------------------------"
print "Elementos:", n_veces 
print "Fallos:", n_fallos
print "Porcentaje de error %f" % (n_porcentaje*100) 
pl.plot(loss_data)
pl.show()         		
