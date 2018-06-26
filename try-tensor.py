import tensorflow as tf
import numpy as np

SAMPLES = 4096
EPOCH = 500

x_data = np.random.rand(SAMPLES).astype(np.float32)
y_data = np.random.rand(SAMPLES).astype(np.float32)
z_data = np.random.rand(SAMPLES).astype(np.float32)
out_data = x_data*0.375 + y_data*0.059 + z_data*(-0.963) + 0.004

Wx = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
Wy = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
Wz = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
delta = tf.Variable(tf.zeros([1]))

out = Wx*x_data + Wy*y_data + Wz*z_data + delta

loss = tf.reduce_mean(tf.square(out - out_data))
optimizer = tf.train.GradientDescentOptimizer(0.2)

train = optimizer.minimize(loss)
init = tf.global_variables_initializer()

sess = tf.Session()

sess.run(init)
for step in range(EPOCH):
	sess.run(train)
	if step%10 == 0:
		print(step, sess.run(Wx), sess.run(Wy), sess.run(Wz), sess.run(delta))
		
