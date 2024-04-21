import requests
import json 
import time

BASE_URL = "https://recyclemap.ru/api/images"
NUM = 33000
SRC_PATH = "data"
DST_PATH = "images"

with_fotos = 0
no_fotos = 0

for i in range(1, NUM+1):
    src_path = f"{SRC_PATH}/{i}.json"
    with open(src_path, "r") as src:
        data = json.load(src)
        if (data["isSuccess"]):
            try:
                for elem in data["data"]["photos"]:
                    index = elem["path"]
                    url = f"{BASE_URL}/{index}"
                    res = requests.get(url)
                    dst_path = f"{DST_PATH}/{index}"
                    with open(dst_path, "wb") as dst:
                        dst.write(res.content)
                print(f"FOTOS FOR {i}.json DOWNLOADED SUCCESSFULLY")
                with_fotos += 1
            except Exception as e:
                print(f"NO FOTOS FOR {i}.json")
                no_fotos += 1
    time.sleep(0.5)

print(f"Puncts with fotos {with_fotos}")
print(f"Puncts without fotos {no_fotos}")