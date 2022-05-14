import json
import os

def readJson(path, default = None):
    if not os.path.exists(path) or os.stat(path).st_size == 0:
        return default

    with open(path, "r") as f:
        return json.load(f)

def writeJson(path, data):
    with open(path, "w") as f:
        json.dump(data, f)