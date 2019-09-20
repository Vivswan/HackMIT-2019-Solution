import json
import os

import requests

URL = "https://partition.hackvengers.dev/api/Vivswan_8834c3/prediction"

for j in range(0, 10000):
    try:
        r = requests.get(url=URL).json()
        if not os.path.exists(os.path.join("data", f"{r['objectid']}.json")):
            print(r["objectid"])
            with open(os.path.join("data", r["objectid"]), "w") as file:
                file.write(json.dumps(r))
    except:
        pass
