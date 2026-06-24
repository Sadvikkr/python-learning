# API (Application Programming Interface)= Communication between systems

# Why APIs exist ? - Backend should not --> access frontend files , read user screens , guess user actions 
# Instead --> frontend sends a request , backend sends a response.

# Remember : API = Communication layer 
#           Functions = Business Logics
#           Separation = reuse + maintainability


# requests.get() = Sends request to server

# response = Stores server reply

# 200 = Success , Request was successful , Server found the endpoint , Server returned data successfully.
# 404 = Not Found , 404 is an HTTP error.
# 401 = Unauthorized 🔒
# 500 = Server Error 💥 


# response.json() = Converts JSON response into Python dictionary

# dictionary.get() = Safe dictionary access



# EXAMPLE 

# response = requests.get("weather_api")

# data = response.json()