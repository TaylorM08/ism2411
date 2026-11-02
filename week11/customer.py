print("---Exercise 1---")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spending": 12400,  
    "Name": "Not Alice", 
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spending"])

print("---Exercise 2---")
customer['phone'] = '555-5555'
print(customer)
customer['tier'] = 'platinum'
print(customer)
del customer["Name"]
print(customer)

