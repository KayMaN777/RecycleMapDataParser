import json

SRC_PATH = "data"
NUM = 33000
DST_PATH = "reformed_data"

for i in range(1, NUM+1):
    src_path = f"{SRC_PATH}/{i}.json"
    dst_path = f"{DST_PATH}/{i}.json"
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
            print(f"Обработали {i}.json")

    with open(dst_path, "w") as dst:
        json.dump(res, dst)