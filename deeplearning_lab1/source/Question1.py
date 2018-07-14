import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#importing dataset which has 569 rows and 30 columns
from sklearn.datasets import load_breast_cancer
#tf.Tensor.get_shape().ndims

#loading data set
dataset = load_breast_cancer()

#setting the data and labels
data = dataset.data
labels = dataset.target

#Reshape the dataset as it fits the model here it considers all 569 rows
labels = np.array(labels).reshape(569,1)

#placeholders need to be set as they need to be fit during runtime
X = tf.placeholder(tf.float32, shape=[None,30])
y = tf.placeholder(tf.float32, shape=[None,1])

#seed value is set as it generates the same random values everytime
tf.set_random_seed(1)

#Weights and bases are intiliazed
weights = tf.Variable(tf.zeros([30, 1]))
base = tf.Variable(0.0)

#Activation function
myLogReg = tf.nn.sigmoid(tf.add(tf.matmul(X, weights), base))

#loss function
loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=myLogReg, labels=y))

#Gradient descent optimizer
optmizer = tf.train.AdagradOptimizer(learning_rate=0.0001).minimize(loss)

#initializing global variables
init = tf.global_variables_initializer()

def predc(X, parameters):
    parameters = tf.convert_to_tensor(parameters)
    x = tf.placeholder(tf.float32, [None, 30])
    z = tf.nn.sigmoid(tf.matmul(x, parameters))
    sess = tf.Session()
    prediction = sess.run(z, feed_dict={x: X})
    return prediction

# session initialization
with tf.Session() as session:
    session.run(init)
    writer = tf.summary.FileWriter("./graphs", session.graph)
#range is for 400 rows
    for i in range(400):

        _, acc = session.run([optmizer, loss], feed_dict={X:data, y:labels})

        if i%40==0:
            print("Epoch "+str(acc))
#closing the session
    writer.close()
    parameters = session.run(weights)
outs = predc(data, parameters) #Calling the function
#Calculating accuracy score for the regression model
print("Accuracy Score is: {} %".format(100 - np.mean(np.abs(outs - labels)) * 100))


# plot the results
#X, y = data.T[0], data.T[1]
#plt.plot(X, y, 'bo', label='Real data')
#plt.plot(X, 'r', label='Predicted data')
#plt.legend()
#plt.show()