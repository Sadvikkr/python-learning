# # Query Parameters

# ## Definition

# Query Parameters are used to filter, search or customize the data returned by an API.

# Syntax:

# GET /students?age=19

# ---

# ## Path Parameter vs Query Parameter

# ### Path Parameter
# - Identifies one specific resource.
# - Usually unique.

# Examples:
# GET /students/1
# GET /products/25

# ### Query Parameter
# - Filters or searches resources.
# - Can return zero, one or many results.

# Examples:
# GET /students?age=19
# GET /students?name=Sadvik
# GET /students?age=19&name=Sadvik

# ---

# ## Optional Query Parameters

# ```python
# def get_students(age: int = None):
# ```

# If no query parameter is provided:

# ```
# /students
# ```

# ```
# age = None
# ```

# If provided:

# ```
# /students?age=19
# ```

# ```
# age = 19
# ```

# ---

# ## Filtering Pattern

# ```
# Create Empty List
#         ↓
# Loop Through Data
#         ↓
# Check Condition
#         ↓
# Append Matching Items
#         ↓
# Return Filtered List
# ```

# Example:

# ```python
# filtered_students = []

# for student in students:
#     if student["age"] == age:
#         filtered_students.append(student)

# return filtered_students
# ```

# ---

# ## Search vs Filter

# ### Search One

# Used when the field is unique.

# Examples:

# - Student ID
# - Email
# - Roll Number

# Pattern:

# ```
# Loop
# ↓
# Found?
# ↓
# Return Immediately
# ```

# ---

# ### Filter Many

# Used when the field is not unique.

# Examples:

# - Age
# - Name
# - City
# - Department

# Pattern:

# ```
# Empty List
# ↓
# Loop
# ↓
# Condition
# ↓
# Append
# ↓
# Return After Loop
# ```

# ---

# ## Multiple Query Parameters

# ```
# /students?age=19&name=Sadvik
# ```

# Both conditions must be true.

# ```python
# student["age"] == age and student["name"] == name
# ```

# ---

# ## Common Mistakes

# ### Returning inside the loop

# ❌ Wrong

# ```python
# for student in students:
#     if condition:
#         return filtered_students
# ```

# ✅ Correct

# ```python
# for student in students:
#     if condition:
#         filtered_students.append(student)

# return filtered_students
# ```

# ---

# ### Using loop variable outside the loop

# ❌ Wrong

# ```python
# if student["age"] == age:
# ```

# before

# ```python
# for student in students:
# ```

# ---

# ## Key Takeaways

# - Path Parameters identify one resource.
# - Query Parameters filter multiple resources.
# - Query Parameters are optional using default values.
# - Filtering requires a new list.
# - Return after the loop when filtering.
# - Evaluate boolean conditions carefully (`and` vs `or`).