import json


book = {"title": "1984",
 "author": "George Orwell",
  "isbn": "978-0451524935"
}
json_string = json.dumps(book)

print(type(json_string))
print(json_string)