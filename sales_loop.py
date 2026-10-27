#---Self Assessment Questions---
#1 An accumulator pattern keeps a running total of a value as it is updated in a loop. Its three steps are to initialize the accumulator variable, update it in a loop, and then use it after the loop is finished.
#2 I noticed the code length was much shorter, but it is much more difficult to read and understand.
#3. A summary statistic loop would have been useful if i wanted to caulculate the hours i worked in a month of my summer job. I could use a loop to add up the hours worked each day and then divide by the number of days to get an average.

#---Exercise 1---
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

#---Exercise 2---
total = 0
count = 0
for sale in sales:
    total += sale
    count += 1

average = total / count
print(f"Total: ${total}")
print(f"Count: {count}")
print(f"Average: ${average:.2f}")

#---Exercise 3---
current_max = 0
for sale in sales:
    if sale > current_max:
        current_max = sale

print(f"Largest sale: ${current_max}")

#---Exercise 4---
count_over_100 = 0
total_over_100 = 0
for sale in sales:
    if sale > 100:
        count_over_100 += 1
        total_over_100 += sale

print(f"Sales over $100: {count_over_100}")
print(f"Total of those sales: ${total_over_100}")

#---Exercise 5---
for sale in sales:
    if sale > 400:
        print(f"Alert: outlier found - ${sale}. Stopping.")
        break
    if sale <= 100:
        continue
    print(f"${sale}")

#---Exercise 6---
total = 0
i = 0
while i < len(sales):
    total += sales[i]
    i += 1

print(f"Total(while loop): ${total}")

#---Exercise 7---
for sale in sales:
    if sale >= 200:
        discount = 0.10
    elif sale >= 100:
        discount = 0.05
    else:
        discount = 0.0

    discounted_price = sale * (1 - discount)
    print(f"{sale} -> {discount*100:.0f}% discount -> " f"${discounted_price:.2f}")