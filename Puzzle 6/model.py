import tensorflow as tf

model = tf.keras.models.Sequential([
    tf.keras.layers.InputLayer(name="image", input_shape=(32, 32, 3)),
    tf.keras.layers.Conv2D(64, (3, 3), padding="same"),
    tf.keras.layers.Conv2D(64, (3, 3), padding="valid"),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512),
    tf.keras.layers.Dense(256),
    tf.keras.layers.Dense(100)
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()
