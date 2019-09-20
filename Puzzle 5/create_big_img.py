import os
import sys

import cv2
import numpy as np

dim = (10, 76)
FOLDER = "shards-Vivswan_dfe32d"

for i in range(0, dim[0]):
    combined = cv2.imread(os.path.join(FOLDER, f"shard-{i * dim[1]}.png"), cv2.IMREAD_UNCHANGED)
    for j in range(1, dim[1]):
        combined = np.concatenate(
            (combined,  cv2.imread(os.path.join(FOLDER, f"shard-{i * dim[1] + j}.png"), cv2.IMREAD_UNCHANGED)),
            axis=1)

    cv2.imwrite(f"temp_{i}.png", combined)

sys.stdout.flush()
combined = cv2.imread("temp_0.png", cv2.IMREAD_UNCHANGED)
os.remove(f"temp_0.png")
for i in range(1, dim[0]):
    combined = np.concatenate((combined, cv2.imread(f"temp_{i}.png", cv2.IMREAD_UNCHANGED)), axis=0)
    os.remove(f"temp_{i}.png")
cv2.imwrite(f"puzzle-{dim[0]}x{dim[1]}.png", combined)

print("Done")
