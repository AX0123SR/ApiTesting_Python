import requests

res = requests.get("https://reqres.in/api/users?page=2")
json_response = res.json()
print(json_response['page'])
assert json_response['page'] == 2

print(json_response['per_page'])
assert json_response['per_page'] == 6

print(json_response["data"][2]["email"])
assert (json_response["data"][2]["email"]).startswith("tobias")

print(json_response["support"]["url"])
