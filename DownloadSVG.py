import requests


res = requests.get("https://recyclemap.ru/api/public/fractions")
data = res.json()
for elem in data["data"]:
    url = "https://recyclemap.ru/assets/icons/ui/fractions/{}".format(elem["icon"])
    opa = requests.get(url)
    dst_path = "fractions/{}".format(elem["icon"])
    with open(dst_path, "wb") as dst:
        dst.write(opa.content)
