import tensorflow as tf
from keras.models import Model
from keras.layers import Input, Flatten, Dense, Dropout

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

input = Input(shape=(28,28))
h = Flatten()(input)
h = Dense(28, activation='relu')(h)
h = Dropout(0.2)(h)
output = Dense(10, activation='softmax')(h)

model = Model(inputs=[input],outputs=[output])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test,y_test)
