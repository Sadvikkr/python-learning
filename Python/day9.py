# Files + JSON

# Basic syntax 
# file = open("data.txt", "w") # "w" → write mode (overwrites file) , "a" → append mode (adds to end of file), "r" → read mode

# file.write("Hello Sadvik") # write content to the file

# file.close()

# with open("data.txt", "w") as file:
#     file.write("Hello Sadvik") # write content to the file

# # Reading from a file
# with open("data.txt", "r") as file:
#     content = file.read() # read the entire content of the file
#     print(content)

# # append mode
# with open("data.txt", "a") as file:
#     file.write("\nNew line") # append content to the file


# # Writing JSON data to a file
# import json
# data = {
#     "name" : "Sadvik",
#     "age" : "20",
# }

# with open("data.json", "w") as file:
#     json.dump(data, file) # write JSON data to the file



# with open("data.json", "r") as file:
#     data = json.load(file) # read JSON data from the file and convert it to a Python dictionary

# print(data)


# with open("notes.txt", "w") as file:
#     file.write("Hello Sadvik")

# with open("notes.txt", "r") as file:
#     content = file.read()

# print(content)

# with open("notes.txt", "w") as file:
#     file.write("My name is Sadvik\nI am learning Pyhton")
# with open("notes.txt", "r") as file:
#     content = file.read()
# print(content) 

# try:
#     with open("notes.txt", "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File does not exist")        

with open("notes.txt", "a") as file:
    file.write("\nHey this is the append fucntion")