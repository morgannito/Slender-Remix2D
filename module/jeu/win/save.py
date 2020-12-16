import json
import requests

def save(pseudo):
    dic = {"pseudo": pseudo }
    jsondata = json.dumps(dic).encode("utf8")
    url = 'http://morgannito.com/apiSlender/save.php'
    x = requests.post(url, data=jsondata)
    x = json.loads(x.text)
    lvl = x['lvl']
    return lvl