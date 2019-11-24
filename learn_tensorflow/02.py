# coding:utf-8
"""
基本概念
"""
import tensorflow as tf
tf.compat.v1.disable_eager_execution()

# 变量
tensor = tf.ones([1, 3])
test_var = tf.Variable(tensor)
init_op = tf.compat.v1.global_variables_initializer()
session = tf.compat.v1.Session()
with session:
    print("tensor is ", session.run(tensor))
    # print("test_var is ", session.run(test_var))
    session.run(init_op)
    print("after init, test_var is", session.run(test_var))


# 占位符
x = tf.compat.v1.placeholder(tf.int32)
y = tf.compat.v1.placeholder(tf.int32)
z = tf.add(x, y)
session = tf.compat.v1.Session()
with session:
    print(session.run([z], feed_dict={x: [1, 2], y: [2, 3]}))


# 队列
# FIFOQUEUE
fifo_queue = tf.compat.v1.FIFOQueue(10, 'int32')
init = fifo_queue.enqueue_many(([1, 2, 3, 4, 5, 6], ))
with tf.compat.v1.Session() as session:
    session.run(init)
    queue_size = session.run(fifo_queue.size())
    for item in range(queue_size):
        print('fifo_queue', session.run(fifo_queue.dequeue()))

# RandomShuffleQueue
rs_queue = tf.compat.v1.RandomShuffleQueue(capacity=5, min_after_dequeue=0, dtypes='int32')
init = rs_queue.enqueue_many(([1, 2, 3, 4, 5], ))
with tf.compat.v1.Session() as session:
    session.run(init)
    queue_size = session.run(rs_queue.size())
    for i in range(queue_size):
        print('rs_queue', session.run(rs_queue.dequeue()))
