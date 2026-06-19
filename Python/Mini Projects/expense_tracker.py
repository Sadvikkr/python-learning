import json
try:
    with open("expense_tracker.json", "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses =[]

name = input("Enter expense name: ")
amount = float(input("Enter expense amount: "))

new_expense = {
    "expense_name" : name,
    "expense_amount" : amount,

}    

expenses.append(new_expense)

with open("expense_tracker.json", "w") as file:
    json.dump(expenses, file, indent = 4)

print("All expenses: ")

for expense in expenses:
    print(expense)
