# Customer Profile
import json
while True:

   customer = input("Enter Customer name:")
   if customer.isdigit():
      print("Name cannot be only numbers")
      
    
   city = input("Enter City:")
   if city.isdigit():
      print("City cannnot be only numbers")

   customer_profile = {
    "customer_name": customer,
    "city_name": city
}

   with open("customer_record.json", "w") as file:
    json.dump(customer_profile , file)

   with open("customer_record.json", "r") as file:
    data = json.load(file)
    print(data)    

    


