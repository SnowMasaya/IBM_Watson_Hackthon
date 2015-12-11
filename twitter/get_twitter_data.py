import json
import urllib.request

results = json.loads(urllib.request.urlopen("https://www.kimonolabs.com/api/2v4qsiw4?apikey=xLxRmAAkTbJ5khJovgtRfCPwxbgOdKpv").read().decode("utf-8"))
print(results)
