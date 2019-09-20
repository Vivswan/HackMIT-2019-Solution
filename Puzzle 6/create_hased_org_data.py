from __future__ import absolute_import, division, print_function, unicode_literals

import base64
import hashlib
import json
import os
from os.path import join

import tensorflow as tf
import numpy as np
import cv2

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar100.load_data()

x_dataset = np.concatenate((x_train, x_test))
y_dataset = np.concatenate((y_train, y_test))


for i in range(0, len(x_dataset)):
    new_img = cv2.cvtColor(x_dataset[i], cv2.COLOR_BGR2RGB)

    cv2.imwrite("temp.png", new_img)
    with open("temp.png", "rb") as image_file:
        img_base64 = str(base64.b64encode(image_file.read()))[2:-1]
        name = hashlib.sha224(img_base64.encode('utf-8')).hexdigest()
        cv2.imwrite(join("org_hash_img", f"{name}.png"), new_img)
        j = json.dumps({
            "image": img_base64,
            "label": int(y_dataset[i][0])
        })
        open(join("org_data_hash", name), "w").write(j)
    os.remove("temp.png")

    if i % 100 == 0:
        print(int((i / len(x_dataset)) * 10000) / 100)
    # cv2.imshow('image', cv2.resize(new_img, (128, 128), interpolation=cv2.INTER_AREA))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

print("Done")