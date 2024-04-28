import json
import csv
import random
'''
MAKING DATABASE SUCH FORMAT:
POINTID|LANTITUDE|LONTITUDE|FRACTION_CODE
'''

NUM = 33000
SRC_PATH = "data"

def make_database():
    baza = []
    for i in range(1, NUM+1):
        src_path = f"{SRC_PATH}/{i}.json"
        with open(src_path, "r") as src:
            data = json.load(src)
            if (data["isSuccess"]):
                try:
                    lst = [data["data"]["pointId"]]
                    res = data["data"]["geom"]
                    res = res[6:-1]
                    lst += res.split(" ")
                    opa = 0
                    for elem in data["data"]["fractions"]:
                        #print(elem["id"])
                        opa += 2**elem["id"]
                    lst.append(opa)
                    #print(lst)
                    baza.append(lst)
                    print(f"{i}.json обработан успешно")
                except Exception as e:
                    print(f"Во время обработки {i}.json произошла ошибка {e}")

    #print(baza)
    random.shuffle(baza)
    baza = baza[0:16001]
    baza[0] = ["pointId", "lat", "lon", "mask"]
    with open("database.csv", "w") as dst:
        mywriter = csv.writer(dst, delimiter=',')
        mywriter.writerows(baza)