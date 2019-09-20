import base64
import io
import json
import os
from os import listdir
from os.path import join

import numpy as np
import tensorflow as tf
from PIL import Image

FOLDER = "data2"
DESTINATION = "data_label"

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar100.load_data()

x_dataset = np.concatenate((x_train, x_test))
y_dataset = np.concatenate((y_train, y_test))


def decode_img(_msg):
    _msg = base64.b64decode(_msg)
    _buf = io.BytesIO(_msg)
    _img = Image.open(_buf)
    return np.asarray(_img)


for i in listdir(FOLDER):
    c = False
    with open(join(FOLDER, i), "r") as file:
        j = json.loads(file.read())
        img = decode_img(j["image"])
        for k in range(0, x_dataset.shape[0]):
            if np.array_equal(x_dataset[k], img):
                j["index"] = k
                j["label"] = int(y_dataset[k][0])
                with open(join(DESTINATION, i), "w") as out_file:
                    out_file.write(json.dumps(j))
                print(i)
                c = True

    if c:
        os.remove(join(FOLDER, i))
