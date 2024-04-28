import requests
import json 
import time
#import logging

BASE_URL = "https://recyclemap.ru/api/public/points"
NUM = 33000
DST_PATH = "data"
REFORMED_DST_PATH = "reformed_data"

def download_json():
    for i in range(1, NUM+1):
        url = f"{BASE_URL}/{i}"
        dst_path = f"{DST_PATH}/{i}.json"
        res = requests.get(url)
        with open(dst_path, "w") as dst:
            dst.write(json.dumps(res.json()))
        time.sleep(1)
        if (i % 200 == 0):
            time.sleep(5)

def refomat_json(src_dir, dst_dir):
    for i in range(1, NUM+1):
        src_path = f"{src_dir}/{i}.json"
        dst_path = f"{dst_dir}/{i}.json"
        res = dict()
        with open(src_path, "r") as src:
            data = json.load(src)
            if (data["isSuccess"]):
                res["isSuccess"] = data["isSuccess"]
                res["pointId"] = data["data"]["pointId"]
                res["address"] = data["data"]["address"]
                res["addressDescription"] = data["data"]["addressDescription"]
                res["pointDescription"] = data["data"]["pointDescription"]
                res["title"] = data["data"]["title"]
                res["scheduleDescription"] = data["data"]["scheduleDescription"]
                tmp = data["data"]["geom"][6:-2].split(' ')
                res["lat"] = tmp[0]
                res["lon"] = tmp[1]
                fractions = ""
                for elem in data["data"]["fractions"]:
                    fractions += str(elem["id"])
                    fractions += " "
                fractions = fractions[:-1]
                res["fractions"] = fractions
                photos = ""
                for elem in data["data"]["photos"]:
                    photos += elem["path"]
                    photos + " "
                photos = photos[:-1]
                res["photos"] = photos
                schedule = ""
                for elem in data["data"]["schedule"]:
                    schedule += (elem["opens"][0] + '-' + elem["closes"][-1])
                    schedule += " "
                schedule = schedule[:-1]
                res["schedule"] = schedule
                
        with open(dst_path, "w") as dst:
            json.dump(res, dst)




