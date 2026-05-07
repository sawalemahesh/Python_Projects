data  = {
  "page": 1,
  "totalUsers": 3,
  "users": [
    {
      "id": 1,
      "name": "Amit",
      "age": 25,
      "email": "amit@test.com",
      "isActive": True,
      "roles": ["user"]
    },
    {
      "id": 2,
      "name": "Priya",
      "age": 30,
      "email": "priya@test.com",
      "isActive": False,
      "roles": ["admin", "user"]
    },
    {
      "id": 3,
      "name": "Rahul",
      "age": 22,
      "email": "rahul@test.com",
      "isActive": True,
      "roles": ["user"]
    }
  ]
}
total_users = len(data["users"])
print(total_users)

for char in data['users']:
    if char['isActive'] == True:
        print(char['email'])
    assert '@' in char['email']

for user in data["users"]:
    assert isinstance(user["id"], int)
    assert isinstance(user["name"], str)
    assert isinstance(user["age"], int)
    assert isinstance(user["email"], str)
    assert isinstance(user["isActive"], bool)
    assert isinstance(user["roles"], list)