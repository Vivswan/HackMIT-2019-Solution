import csv
import json
from os import listdir
from os.path import isfile, join

import numpy as np

data_files = [f for f in listdir("data_label") if isfile(join("data_label", f))]
o_id = []

for i in data_files:
    with open(join("data_label", i), "r") as file:
        j = json.loads(file.read())

        # print(np.max(j["prediction"]), j["prediction"].index(np.max(j["prediction"])), j["label"])

        if j["prediction"].index(np.max(j["prediction"])) == j["label"] and np.max(j["prediction"]) > 0.995:
            print(np.max(j["prediction"]))
            o_id.append(j["objectid"])
            # print(j["objectid"])

        if len(o_id) >= 1000:
            break

print(len(o_id), len(data_files), len(o_id) * 100 / len(data_files))

with open('ids.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(o_id)
