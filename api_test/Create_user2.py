import requests
import json

mydata = open("data.json",'r').read()
res = requests.post("https://reqres.in/api/users", data=json.loads(mydata))
print(type(res))
print(res.json())
