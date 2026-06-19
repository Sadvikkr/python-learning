# Machine Track - Day 10

# import json

# machine_name = input("Enter machine name: ")

# while True:
#     try:
#         start_time = int(input("Enter start time: "))
#         break
#     except ValueError:
#         print("Invalid input. Enter a number.")

# while True:
#     try:
#         stop_time = int(input("Enter stop time: "))
#         break
#     except ValueError:
#         print("Invalid input. Enter a number.")

# if stop_time < start_time:
#     print("Stop time cannot be less than start time")
# else:
#     usage = stop_time - start_time

#     print("Machine Name:", machine_name)
#     print("Usage:", usage, "hours")

#     record = {
#         "machine": machine_name,
#         "start": start_time,
#         "stop": stop_time,
#         "usage": usage
#     }

#     # Load old data
#     try:
#         with open("machine_usage.json", "r") as file:
#             data = json.load(file)
#     except FileNotFoundError:
#         data = []

#     # ALWAYS append (outside except)
#     data.append(record)

#     # Save full list
#     with open("machine_usage.json", "w") as file:
#         json.dump(data, file, indent=4)

#     print("Data saved successfully.")



# 4 June 2026... 

# import json


# student = {
#     "name": "Sadvik",
#     "age": 19
# }

# with open("student.json", "w") as file:
#     json.dump(student, file)

import json

# customer = {
#     "name": "Sadvik", 
#     "city": "Hyderabad",
#     "age": 19

# }
# with open("customer.json", "w") as file:
#     json.dump(customer, file)

# with open("customer.json", "r") as file:
#     data = json.load(file)
#     print(type(data["name"]))
    
students = [
    {"name": "Aman"},
    {"name": "Riya"}
]

with open("students.json", "w") as file:
    json.dump(students, file)

with open("students.json", "r") as file:
    data = json.load(file)

print(type(data))    