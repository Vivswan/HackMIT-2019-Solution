import hashlib
import json
from os import listdir
from os.path import isfile, join


data_files = [f for f in listdir("data") if isfile(join("data", f))]
ids = []

# print(np.add.reduce(j["prediction"]), np.mean(j["prediction"]), np.std(j["prediction"]), np.max(j["prediction"]))
for f in data_files:
    with open(join("data", f), "r") as file:
        j = json.loads(file.read())
        name = hashlib.sha224(j["image"].encode('utf-8')).hexdigest()
        with open(join("data_hash", name), "w") as w:
            w.write(json.dumps(j))

print("Done")
