from JsonParser import download_json, refomat_json, DST_PATH, REFORMED_DST_PATH
from DatabaseMaker import make_database
import time

while (1):
    download_json()
    refomat_json(DST_PATH, REFORMED_DST_PATH)
    make_database()
    time.sleep(60*60*24*3)