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