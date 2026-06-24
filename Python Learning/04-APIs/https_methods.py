# ==========================
# GET REQUEST
# ==========================

# GET is used to READ or FETCH data from a server.

# Examples:
# Show all students
# Show weather data
# Show user profile
# Show products

# Example:
# requests.get("weather_api")

# Flow:
# Client
# ↓
# GET Request
# ↓
# Server
# ↓
# Returns Data


# ==========================
# POST REQUEST
# ==========================

# POST is used to CREATE or SEND data to a server.

# Examples:
# Login Form
# Signup Form
# Create Student
# Create Order

# Example:
# requests.post("student_api")

# Flow:
# Client
# ↓
# Send Data
# ↓
# Server
# ↓
# Stores Data


# ==========================
# DIFFERENCE
# ==========================

# GET  -> Read Data
# POST -> Create/Send Data


# Examples

# GET
# Show Weather
# Show Students
# Show Products

# POST
# Create Student
# Create Account
# Create Order


# ==========================
# API FLOW
# ==========================

# Python
# ↓
# requests.get() / requests.post()
# ↓
# API Server
# ↓
# Response
# ↓
# response.json()
# ↓
# Python Dictionary


# ==========================
# PUT REQUEST
# ==========================

# PUT is used to UPDATE existing data.

# Examples:
# Update student marks
# Update profile
# Change password
# Update order status

# Example:
# requests.put("student_api")

# Flow:
# Client
# ↓
# Send Updated Data
# ↓
# Server
# ↓
# Updates Existing Record


# ==========================
# DELETE REQUEST
# ==========================

# DELETE is used to REMOVE data.

# Examples:
# Delete student
# Delete account
# Delete product
# Delete order

# Example:
# requests.delete("student_api")

# Flow:
# Client
# ↓
# Request Deletion
# ↓
# Server
# ↓
# Removes Record


# ==========================
# CRUD OPERATIONS
# ==========================

# Create -> POST
# Read   -> GET
# Update -> PUT
# Delete -> DELETE


# Student API Example

# POST   /students
# GET    /students
# PUT    /students
# DELETE /students


# Employee API Example

# Add Employee          -> POST
# View Employee Details -> GET
# Update Salary         -> PUT
# Remove Employee       -> DELETE