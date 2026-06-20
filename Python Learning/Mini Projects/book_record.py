import json
try:
    with open("book_record.json", "r") as file:
        books = json.load(file)
except FileNotFoundError:
    books =[]

name = input("Enter book name: ")
author = input("Enter author name: ")

new_record = {
    "book_name" : name,
    "author" : author,

}

books.append(new_record)

with open("book_record.json", "w") as file:
    json.dump(books, file, indent = 4)

print("All book records: ")

for record in books:
    print("Book:", record["book_name"])
    print("Author:", record["author"])