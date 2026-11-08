#1. The difference between using .get() and brackets is that when using .get(), the information you are trying to retrive may not be there and returns none instead of crashing the code. Brackets are for recieving data you know the information of. I would use .get() if i were checking if i had someones information and brackets if i were trying to pull up at a specific location. 
#2 The summarized dictionary reminds me of a pivot table on excel except python would be much easier to use when having a lot of data due to the reusability of the code.
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

print("---Exercise 3---")

print(customer.get("email", "no email on file"))
try:
    print(customer["email"])
except KeyError as error:
    print("KeyError caught:", error)

print("---Exercise 4---")

for key, value in customer.items():
    print(f"{key}: {value}")
for something in customer:
    print(something, customer[something])

print("---Exercise 5---")
tier_discounts = {
                  "bronze": 0, 
                  "silver": 0.05, 
                  "gold": 0.10, 
                  "platinum": 0.15
}
purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer['tier']}")
print(f"Discount rate: {discount_rate*100:.0f}%")
print(f"Final price: ${final_price:.2f}")

print("---Exercise 6---")
customers = [
    {"name": "Bob", "tier": "silver", "ytd_spending": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spending": 8750},
    {"name": "David", "tier": "bronze", "ytd_spending": 450},
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}): ${discount:.2f}")

print("---Exercise 7---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
} 
for name, details in catalog.items():
    if details["stock"] < 20:
        print(f"Low stock alert for {name}: only {details['stock']} left!")

print("---Exercise 8---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    amount = sale["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount
print(sales_by_region)

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")