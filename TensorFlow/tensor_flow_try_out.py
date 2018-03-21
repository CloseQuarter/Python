# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 02:45:45 2018

@author: sanooj
"""

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))