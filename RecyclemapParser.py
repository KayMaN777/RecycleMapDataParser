import requests
import json 
import time

BASE_URL = "https://recyclemap.ru/api/public/points"
NUM = 33000
DST_PATH = "data"

for i in range(1, NUM+1):
    url = f"{BASE_URL}/{i}"
    dst_path = f"{DST_PATH}/{i}.json"
    res = requests.get(url)
    with open(dst_path, "w") as dst:
        dst.write(json.dumps(res.json()))
    with open(dst_path, "r") as src:
        data = json.load(src)
        if (data["isSuccess"]):
            print(f"{i}.json DOWNLOADED SUCCESSFULLY")
        else:
            print(f"{i}.json NOT DOWNLOADED")
    if (i % 200 == 0):
        time.sleep(5)

i=1
url = f"{BASE_URL}/{i}"
dst_path = f"{DST_PATH}/{i}.json"
res = requests.get(url)
with open(dst_path, "w") as dst:
    #json.dump(res.json(), dst)
    #print(res.json())
    dst.write(json.dumps(res.json()))

with open(dst_path, "r") as src:
    data = json.load(src)
    print(data["data"]["pointDescription"])