import datetime
import re

storeName = "SEMICOLON STORE"
Branch = "MAIN BRANCH"
Address = "312, HERBERT MACAULAY WAY, SABO YABA, LAGOS STATE."
number = "03293828343"
dateTime = datetime.datetime.now()

customerName = " "
cashierName = " "
product = []
productNumber = []
productNumberAmount = []
totalProductNumber = []
discountInput = 0
amountPaid = 0



def CustomerNameEntry():
    global customerName
    user = input("What is the customer's Name: ")

    if re.search("^(?!$)\D+$",user):
        customerName = user
        listOfItems()
    else:
     print("\ninvalid entry")
    CustomerNameEntry()

def listOfItems():
    global product
    items = input("\nWhat did the user buy? ")
    if re.search("^(?!$)\D+$",items):
        product.append(items)
        unitOfItems()
    else:
        print("invalid entry")
        listOfItems()

def unitOfItems():
    global  productNumber
    numberOfItems = input("\nHow many pieces? ")

    if numberOfItems.isdigit():
        productNumber.append(int(numberOfItems))
        unitPerItemsAmount()

    else:
        print("\nInvalid entry")
        unitOfItems()


def unitPerItemsAmount():
    global productNumberAmount
    amount =input("\nHow much per unit? ")

    if amount.isdigit():
        productNumberAmount.append(int(amount))
        conditionForItems()

    else:
        print("Invalid entry")
        unitPerItemsAmount()


def conditionForItems():
    global discountInput
    mayBe = input("\nAdd more items?"+
                "\nif yes enter \"Yes\"  else enter \" No\" ")
    if re.search("^(?!$)\D+$", mayBe):
        if mayBe.casefold() == "yes":
         listOfItems()

        if mayBe.casefold() == "no":
            CashierNameEntry()
    else:
         print("\nInvalid entry")
         conditionForItems()


def CashierNameEntry():
    global cashierName
    user = input("\nWhat is  your Name: ")


    if re.search("^(?!$)\D+$",user):
        cashierName = user
        discount()

    else:
            print("invalid entry")
            CashierNameEntry()

def discount():
    global discountInput
    discountT = input("\nHow much discount will the customer get \n don't give more than 10% discount ")
    print(productNumberAmount)



    if discountT.isdigit() and int(discountT) <= 10:
        discountInput = int(discountT)
        StoreInfo()

    else:
        print("\n Kindly reduce the discount , don't give any more than 10% ")
        discount()

def StoreInfo():

    global cashierName
    global customerName

    print(f"\n{storeName}\n{Branch }\nLocation : {Address}\nTel : {number}\nDate : {dateTime}\ncashier : {cashierName} \nCustomer Name : {customerName}")
    storeReceiptHead()

def storeReceiptHead():

    global  discountInput, totalProductNumber

    print(f"""\n{"=" * 60}\n\tITEM  \tQTY         PRICE   \t\tTOTAL(NGN)\n{"-" * 60 }""")
    num = 0
    subTotal = 0.0


    for index in range(len(product)):
        num = productNumber[index]* productNumberAmount[index]
        totalProductNumber.append(num)

    subTotal += num
    for index in range(len(product)):
        print(f"""
    {product[index]:<10}{productNumber[index]:<10}{productNumberAmount[index]:<14.2f}   {totalProductNumber[index]:<14.2f}""")
    discount_t = subTotal * (discountInput / 100)
    vat = subTotal * 0.175
    bill = subTotal + vat - discount_t

    print(f"""{"-" * 60}\n\t\t\t\t Sub Total: {subTotal:.2f} \n\n\t\t\t\t Discount: {discount_t:.2f} \n\n\t\t\t\t VAT @ 17.50: {vat:.2f} 
    \n{ "=" * 60} \n\t\t\t\t Bill Total: {bill:.2f}\n{"=" * 60 }\n\tTHIS IS NOT A RECEIPT KINDLY PAY {bill:.2f}\n{"=" * 60} """)
    amountFromCustomer()
def amountFromCustomer():
    global amountPaid
    amount = input("\n\nHow much did the customer give you? ")
    amountPaid = float(amount)
    if amount.isdigit():
        customerReceipt()
    else:
        print("invalid entry")
        amountFromCustomer()

def customerReceipt():

    global discountInput, totalProductNumber,amountPaid

    print(f"""\n{"=" * 60}\n\tITEM  \tQTY         PRICE   \t\tTOTAL(NGN)\n{"-" * 60}""")
    num = 0
    subTotal = 0.0

    for index in range(len(product)):
        num = productNumber[index] * productNumberAmount[index]
        totalProductNumber.append(num)

    subTotal += num
    for index in range(len(product)):
        print(f"""
        {product[index]:<10}{productNumber[index]:<10}{productNumberAmount[index]:<14.2f}   {totalProductNumber[index]:<14.2f}""")
    discount_t = subTotal * (discountInput / 100)
    vat = subTotal * 0.175
    bill = subTotal + vat - discount_t
    total =  amountPaid - bill


    print(
        f"""{"-" * 60}\n\t\t\t\tSub Total: {subTotal:.2f} \n\n\t\t\t\t Discount: {discount_t:.2f} \n\n\t\t\t\t VAT @ 17.50: {vat:.2f} 
        \n{"=" * 60} \n\t\t\t\t Bill Total: {bill:.2f}\n\n\t\t\t\tAmount Paid: {amountPaid} \n\n\t\t\t\t Balance: {total}\n{"=" * 60}\n
            THANK YOU FOR YOUR PATRONAGE\n{"=" * 60}""")


if __name__ == '__main__':
    CustomerNameEntry()
