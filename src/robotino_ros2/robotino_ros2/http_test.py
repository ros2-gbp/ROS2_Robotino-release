import requests
x = requests.get("http://10.42.0.148/data/powermanagement")
print (x.json())
