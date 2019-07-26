from __future__ import absolute_import, division, print_function, unicode_literals

# Tensorflow and tf.keras
import tensorflow as tf

# Helper libraries
# import numpy as np
# import matplotlib.pyplot as plt

print(tf.__version__)

# ## gradient tape
# import tensorflow as tf
# import numpy as np
# a = tf.keras.layers.Dense(32)
# b = tf.keras.layers.Dense(32)
#
# inputs = tf.keras.layers.Input(10)
#
# # inputs = np.arange(10).reshape(1, 10)
#
# #
# # with tf.GradientTape(watch_accessed_variables=False) as tape:
# #   tape.watch(a.variables)  # Since `a.build` has not been called at this point
# #                            # `a.variables` will return an empty list and the
# #                            # tape will not be watching anything.
# #   result = b(a(inputs))
# #   tape.gradient(result, a.variables)  # The result of this computation will be
# #                                       # a list of `None`s since a's variables
# #                                       # are not being watched.


