pennies = 1
dime = 10
quarters = 25

cost_price = int(input("Enter item price: "))
amount = int(input("Enter amount paid: "))
balance = amount - cost_price
if balance >= 25:
    quarters = balance / quarters
    balance % quarters
elif balance >= 10:
    dime = balance / dime
    balance % dime
elif balance >= 1:
    pennies = balance / pennies
    balance = 1

print(f"""quarters:{quarters }
 dimes: {dime}
 pennies: {pennies} """)



