
import requests

res = requests.get("https://reqres.in/api/users?page=2")
code = res.status_code
print(code)
assert code == 200, "Mission Passed"

#print(res.text)
#print(type(res))
#print(res.content)

print(res.json())
print(res.headers)
print(res.cookies)
print(res.encoding)
print(res.url)