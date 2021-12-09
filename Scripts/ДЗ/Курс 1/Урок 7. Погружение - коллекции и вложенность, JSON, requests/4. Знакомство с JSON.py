import json

profile = {
    "name": "Alice",
    "is_online": True,
    "hobbies" : {
        1: "cryptography",
        2: "coding",
        3: "outdoor activities",
    },
 }

raw_json = json.dumps(profile)
print(raw_json)

with open('data.txt', 'w') as f:
  f.write(raw_json)