# coding:utf-8
"""
desc：验证tensorflow的编程特点
"""
import tensorflow as tf
tf.compat.v1.disable_eager_execution()


a = 3
b = 4
c = 5
y = tf.add(a*b, c)
print(y)

a = tf.constant(3, tf.int32)
b = tf.constant(4, tf.int32)
c = tf.constant(5, tf.int32)
y = tf.add(a*b, c)
print(y)
session = tf.compat.v1.Session()
print(session.run(y))
session.close()
