#---Self Assessment Questions---
#1. The first, and only, error i was able to identify and correct on my own was adding a colon after "for sale in sales" in Exercise 5. The rest I had to use AI so it shows my debugging instincts are at a very basic level.
#2. apply_discount(price, tier) function applies a discount based on the customer's tier (gold, silver, bronze, or none). Based on the tier, it returns the price after applying the corresponding discount.
#3. AI USED. I would say AI both shortcutted and built my understanding through the debugging process, simply because I relied on it to identify and correct errors that I couldn't figure out on my own.
#---Exercise 1---
def calculate_tax(price, rate):
    return price * rate
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")

#---Exercise 2---
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}") #conditional in function, function in loop

#---Exercise 3---
def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f"final_price(200, 0.07, 'gold'): ${final_price(200, 0.07, 'gold'):.2f}")

#---Exercise 4---
orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price}, Tier: {tier}, Total: ${total:.2f}")

#---Exercise 6---
x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)

#---Exercise 5---
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale # total = sales is just a variable assignment, it does not add the value of sale to total. I changed it to total += sale, which adds the value of sale to total.
print(f"Total: ${total}")

count = 0
for sale in sales: #python expects a colon at the end of the for loop, so I added it.
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales): # changed <= to < to avoid IndexError
    print(sales[i])
    i += 1