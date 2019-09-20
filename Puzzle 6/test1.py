from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import numpy as np

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar100.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

x_dataset = np.concatenate((x_train, x_test))
y_dataset = np.concatenate((y_train, y_test))
print(x_train.shape, x_test.shape, x_dataset.shape)
print(y_train.shape, y_test.shape, y_dataset.shape)

new_y_dataset = np.zeros((y_dataset.shape[0], np.max(y_dataset) + 1), dtype=x_train.dtype)

for i in range(0, y_dataset.shape[0]):
    new_y_dataset[i][y_dataset[i]] = 1
    
print(y_dataset.shape, new_y_dataset.shape, y_dataset[0])
print(new_y_dataset[0])

split_x_dataset = np.split(x_dataset, 2)
split_y_dataset = np.split(new_y_dataset, 2)

x_training_half = split_x_dataset[0]
y_training_half = split_y_dataset[0]

x_testing_half = split_x_dataset[1]
y_testing_half = split_y_dataset[1]

print(x_training_half.shape, y_training_half.shape)
print(x_testing_half.shape, y_testing_half.shape)

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(64, (3, 3), input_shape=(x_dataset.shape[1], x_dataset.shape[2], x_dataset.shape[3]), padding="same"),
    tf.keras.layers.Conv2D(64, (3, 3), padding="valid"),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(new_y_dataset.shape[1], activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy',metrics=['accuracy'])

model.fit(x_training_half, y_training_half, epochs=15)

model.evaluate(x_testing_half, y_testing_half)