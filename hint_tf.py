import tensorflow as tf

# x=2
# y=2

# op1=tf.add(x,y)
# op2=tf.multiply(x,y)
# op3=tf.pow(op2,op1)

# with tf.Session() as sess:
#    op3= sess.run(op3)

# print(op3)


# g=tf.Graph()

# with g.as_default():
#     xy=tf.add(4,5)
# print(xy)

###Visuzile the tensorflow
# python [yourprogram].py 
# tensorboard --logdir="./graphs" --port 6006 
# Then open your browser and  go to http://localhost:6006/


a=tf.constant(2)
b=tf.constant(3)
x= tf.add(a,b)

with tf.Session() as sess:
    writer = tf.summary.FileWriter("./graphs", sess.graph)
    print(sess.run(x))


b=tf.Variable(2,name="scalar")
print(b)