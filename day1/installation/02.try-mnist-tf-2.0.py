import tensorflow as tf
import datetime
import os

#os.sep = '/'

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

input = tf.keras.layers.Input(shape=(28,28))
h = tf.keras.layers.Flatten()(input)
h = tf.keras.layers.Dense(28, activation='relu')(h)
h = tf.keras.layers.Dropout(0.2)(h)
output = tf.keras.layers.Dense(10, activation='softmax')(h)

model = tf.keras.models.Model(inputs=[input],outputs=[output])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

log_dir = 'logs/fit/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

cb_tensorboad = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

model.fit(x_train, y_train, epochs=5, callbacks=[cb_tensorboad])

model.evaluate(x_test, y_test)


train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
test_dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test))

train_dataset = train_dataset.shuffle(60000).batch(64)
test_dataset = test_dataset.batch(64)