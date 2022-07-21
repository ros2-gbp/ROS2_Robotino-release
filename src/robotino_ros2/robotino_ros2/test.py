import requests
result = requests.get("http://10.42.0.148" + "/data/services").json()
for index in result:
    service_group = index["_children"]
    service_array = []
    for service in service_group:
        print(service)