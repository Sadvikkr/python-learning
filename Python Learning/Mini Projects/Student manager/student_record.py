# import json
# try: 
#     with open("student_record.json","r") as file:
#         students = json.load(file)   # loads old students
# except FileNotFoundError:
#     students =[]   #empty list

# name = input("Enter student name: ")
# marks = int(input("Enter marks: "))

# new_student = {
#     "name" : name,
#     "marks" : marks
# }

# students.append(new_student)  #This is the line that preserves old data.

# with open("student_record.json", "w") as file: 
#     json.dump(students, file, indent=4)
#  #Jab hum json.load() karte hain, toh JSON file ka pura data memory (RAM) me students variable ke andar aa jata hai.
#  #Phir jab hum students.append(new_student) karte hain, toh naya student bhi usi memory wale list me add ho jata hai.
#  #Ab students variable ke paas old data + new data dono hote hain. 
#  #Jab hum "w" mode se file open karte hain, toh file ka purana content delete ho jata hai,
#  #lekin data lost nahi hota kyunki wo already memory me students variable ke andar pada hua hai. 
#  #Fir json.dump(students, file) memory me jo updated list hai usko dobara file me likh deta hai. 
#  #Isliye file erase hone ke baad bhi saara data wapas aa jata hai, aur naya student bhi add ho jata hai

# print("All Students:")

# for student in students:
#     print(student)


# import json
# try:
#     with open("student_record.json", "r") as file:
#         students = json.load(file)

# except FileNotFoundError:
#     students =[]

# name = input("Enter name: ")
# marks = int(input("Enter marks: "))

# new_student = {
#     "name" : name,
#     "marks" : marks,
# }
   
# students.append(new_student)

# with open("student_record.json","w") as file:
#     json.dump(students, file, indent = 4)

# print("All students: ")

# for student in students:
#     print(student)
     

#import json

#  def load_students():

#     try:
#         with open("student_record.json", "r") as file:
#             students = json.load(file)

#     except FileNotFoundError:
#         students = []

#     return students 

#  def save_students(students):
    
#     with open("student_record.json", "w") as file:
#         json.dump(students, file, indent = 4)



#  def add_students(students, name, marks):

#     new_student = {
#     "name" : name,
#     "marks" : marks
#     }
#     students.append(new_student)

#  def view_students(students):
#     print("All students:")
#     for student in students:
#      print(student)


#  students = load_students() 
#  name = input("Enter student name: ")
#  marks = int(input("Enter marks: "))
#  add_students(students, name, marks)
#  save_students(students)
#  view_students(students)





import json

def load_students():

    try:
        with open("student_record.json", "r") as file:
            students = json.load(file)

    except FileNotFoundError:
        students = []

    return students 

def save_students(students):
    
    with open("student_record.json", "w") as file:
        json.dump(students, file, indent = 4)



def add_students(students, name, marks):

    new_student = {
    "name" : name,
    "marks" : marks
    }
    students.append(new_student)

def view_students(students):
    print("All students:")
    for student in students:
     print(student)     

def search_students(students):

    search_student = input("Enter student name to search: ")
    found = False
    for student in students:
        
       

        if student["name"] == search_student:
            print(student)

            found = True

    if not found: 
            print("Student Not found")   

def delete_students(students):

    delete_student = input("Enter student name to delete: ")
    found = False
    for student in students:

        if student["name"] == delete_student:
            students.remove(student)
            print(student)

            found = True
    if not found:
           print("Student Not found")






while True:     # Added Menu based into it 

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")



    choice = input("Enter choice: ")

    if choice == "1":
        
            students = load_students()
            name = input("Enter student name: ")
            marks = int(input("Enter marks: "))
            add_students(students, name, marks)
            save_students(students)
         
           

    elif choice == "2":
        students = load_students()
        view_students(students)

    elif choice == "3":
        students = load_students()
        search_students(students)

    elif choice == "4":
        students = load_students()
        delete_students(students)
        save_students(students)

    elif choice == "5": 
        break

    else: 
        print("Invalid choice:")
        


# students = load_students() 
# name = input("Enter student name: ")
# marks = int(input("Enter marks: "))
# add_students(students, name, marks)
# save_students(students)
# view_students(students)



