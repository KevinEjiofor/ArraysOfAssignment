price = int(input("Enter price:$ "))
credit_score = int(input("Enter credit score: "))
if credit_score == 1:
    product = (10*price)/100
    print("Discount price: ", product)
    payment = price - product
    print("Discount payment:$", payment)
elif credit_score == 2:
    payment = (25 * price)/100
    print("payment:$", payment)


