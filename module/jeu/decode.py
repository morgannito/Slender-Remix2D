import json
import requests

# fonction appelé pour obtenir la matrice d'un niveau via l'api
def decode(niveau):
    # prepare le json
    dic = {"niveau": niveau }
    jsondata = json.dumps(dic).encode("utf8")
    # url de l'api
    url = 'http://morgannito.com/apiSlender/niveau.php'
    x = requests.post(url, data=jsondata)
    x = json.loads(x.text)
    # retourne la matrice obtenu par l'api
    lab = x['matrice']
    return lab

