# Import `tensorflow`
import tensorflow as tf
#tensor flow object / creating a node
a = tf.constant(4,name="input_a")
b = tf.constant(3,name="input_b")
c = tf.add(a , b , name="add_c")
d = tf.multiply(a , b , name="mul_d")
e = tf.multiply(c , d , name="mul_e")
sess= tf.Session()
writer = tf.summary.FileWriter("./my_graph", sess.graph)
print(sess.run(e))
