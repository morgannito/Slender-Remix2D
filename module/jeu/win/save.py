import json
import requests

# fonction qui va communiquer avec l'api pour actualiser le niveau de l'utilisateur
def save(pseudo):
    # formate le json qui va etre post
    dic = {"pseudo": pseudo }
    jsondata = json.dumps(dic).encode("utf8")
    # url de l'api
    url = 'http://morgannito.com/apiSlender/save.php'
    # requete post
    x = requests.post(url, data=jsondata)
    x = json.loads(x.text)
    # charge le retour du niveau de l'utilisateur
    lvl = x['lvl']
    return lvl