import requests
import json
payload = {
    "name": "morpheus",
    "job": "zion resident"
}
#res= requests.put("https://reqres.in/api/users/2", data=payload)
res= requests.patch("https://reqres.in/api/users/2", data=payload)
print(res)
print(res.json())