# Example 1 - Gym Workout Tracker 

workouts = [
    {"name": "Bench Press", "reps": 10, "weight": 80, "completed": True},
    {"name": "Squats", "reps": 12, "weight": 100, "completed": True},
    {"name": "Deadlift", "reps": 5, "weight": 140, "completed": False},
]

completed_count = 0
total_weight = 0

for workout in workouts:
    # Calculate how many exercises were completed
    status = workout["completed"]

    if status == True:
        completed_count += 1 
        total_weight += workout["reps"] * workout["weight"]

print(f"Exercise Completed : {completed_count}")
print("Total Weight Lifted:", total_weight)

# Example 2 -   Daily Temperature Analysis

temperatures = [
    {"city": "Delhi", "temp": 38, "raining": False},
    {"city": "Mumbai", "temp": 32, "raining": True},
    {"city": "Jaipur", "temp": 41, "raining": False},
    {"city": "Bangalore", "temp": 28, "raining": True},
]

hot_count = 0
rain_count = 0
total_temp = 0

for temp in temperatures:
    total_temp += temp["temp"]

# Calculate how many cities are hot and how many are raining
    if temp["temp"] >= 35:
      hot_count += 1
    if temp["raining"] == True:
      rain_count += 1   

average = total_temp / len(temperatures)
print("Number of Hot Cities:", hot_count)
print("Number of Raining Cites:", rain_count)
print("Average temperature:", average)


# Example 3 - College Elibility System

students = [
    {"name": "Aman", "attendance": 82, "assignment": True},
    {"name": "Riya", "attendance": 68, "assignment": True},
    {"name": "Kabir", "attendance": 90, "assignment": False},
    {"name": "Sneha", "attendance": 76, "assignment": True},
]
eligible_count = 0
non_eligible_count = 0

for student in students:
    if student["attendance"] >= 75 and student["assignment"]:
       print(student['name'], "- Eligible for Exam")
       eligible_count += 1
    else:
       print(student['name'], "- Not Eligible for Exam")
       non_eligible_count += 1

print("Eligible Students:", eligible_count)
print("Non-Eligible Students:", non_eligible_count)
