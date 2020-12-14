import json
import requests

def decode(niveau):
    dic = {"niveau": niveau }
    jsondata = json.dumps(dic).encode("utf8")
    url = 'http://morgannito.com/apiSlender/niveau.php'
    x = requests.post(url, data=jsondata)
    x = json.loads(x.text)
    lab = x['matrice']
    return lab

