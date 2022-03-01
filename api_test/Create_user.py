import requests

payload= {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
print(payload)
print(type(payload))
res = requests.post("https://reqres.in/api/register",data=payload)
print(res)
print(res.json()['token'])
