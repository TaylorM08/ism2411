#Self Assessment Questions:
#1. Since 350 is less than 500 but greater than 200, the discount will be 10%.
#2. if total > 100 is true when any number greater then 100 is entered, total < 500 is true when any number less than 500 is entered. They are not garunteed to produce the same amount if the amount entered is between 100 and 500. The first statement will produce a discount of 10% while the second statement will produce a discount of 5%.
#3. Tiered conditional logic is often encountered when shopping online. Typically, the more you spend, the more of a discount you will receive. Knowing how this works in python, I can envision wht is happening behind the scenes when I see different discount levels applied based on the total amount.
#---Exercise 1---
# here is a new line
total = float(input("Enter the total amount: $"))

# Add your if/elif/ else here
if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.10
elif total >= 100:
    discount = 0.05
else:
    discount = 0

final = total * (1 - discount)
print(f"Discount: {discount*100:.0f}%")

#---Exercise 2---

if final > 1000:
    status = "manager_approval_required"
else:
    status = "auto_approved"
print(status)

#---Exercise 3---

region = "South"

if region == "South" and total >= 100:
    extra_discount = 0.02
    print("Region bonus applied: additional 2% off")

final = total * (1- (discount + extra_discount))
print(final)

#---Exercise 4---

customer_type = "wholesale"
if region == "South" and total > 100 and customer_type == "wholesale":
    extra_discount = 0.03
    

#---Exercise 5---

amount = 0
if amount <= 0:
    print("SUSPICIOUS")
elif amount < 10000:
    print("NORMAL")
else:
    print("LARGE -- REVIEW REQUIRED")

#---Exercise 6---

total_spent_this_year = 2500
orders_this_year = 6
has_outstanding_balance = False
vip_upgrade = True

if total_spent_this_year > 2000 or orders_this_year > 10:
    vip_upgrade = True
else:
    vip_upgrade = False

    # ---Stretch A---
