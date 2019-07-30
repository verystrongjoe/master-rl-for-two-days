from __future__ import absolute_import, division, print_function, unicode_literals

# Tensorflow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt


# todo : 텐서플로우 2.0 에 대한 간단한 소개를 같이 여기에다가 ex) session에 대한 관리와 eagar execution에 대한 장점등..
print(tf.__version__)
print(tf.executing_eagerly())
print("1 + 2 + 3 + 4 + 5 =", tf.reduce_sum([1, 2, 3, 4, 5]))
