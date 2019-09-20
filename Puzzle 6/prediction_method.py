import csv
import json
import os
from os import listdir
from os.path import isfile, join

import numpy as np

data_files = [f for f in listdir("data") if isfile(join("data", f))]
ids = []

# print(np.add.reduce(j["prediction"]), np.mean(j["prediction"]), np.std(j["prediction"]), np.max(j["prediction"]))
for f in data_files:
    with open(os.path.join("data", f), "r") as file:
        j = json.loads(file.read())
        if np.max(j["prediction"]) > 0.99995:
            print(np.max(j["prediction"]))
            ids.append(j["objectid"])
            print(len(ids))

        if len(ids) >= 1000:
            break

print(len(ids))
with open('ids.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(ids)


# with open(os.path.join("data", "0bdc14188f"), "r") as file:
#     j = json.loads(file.read())
#     print(np.std(j["prediction"]))

