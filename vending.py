from catalog import catalog
from cashPayment import cashPayment
from cardPayment import cardPayment
import os 

from pdb import set_trace

myCatalog = catalog()
cashPayment = cashPayment()
cardPayment = cardPayment()

myCatalog.addItem('TWIX',11,1,10)
myCatalog.addItem('WATER',12,.5,10)
myCatalog.addItem('MINT',13,.25,20)

condition = True

while(condition):
    
    os.system('clear')
    print("\n **** Welcome to Amit Vending Machine. ****")
    print("Please select the Item from below list \n")
    print("\nName \t\t\t Price \t\t\t ItemID ")
    myCatalog.displayCatalog()
    
    itemIdChoice = input("Enter the Item Id = ")
    itemIdChoice = int(itemIdChoice)

    paymentChoice = input("Pay by CASH or CARD. Enter 1 for CASH, 2 for CARD = ")
    paymentChoice = int(paymentChoice)

    if not myCatalog.checkCustomerChoice(itemIdChoice):
        print("**** Error : Wrong Item Selected *****")
    else:
        amountToPay = myCatalog.getItemPrice(itemIdChoice)
        if paymentChoice == 1:
            if cashPayment.processPayment(amountToPay):
                print("Cash Payment Successfull")

        elif paymentChoice == 2:
            if cardPayment.processPayment({},amountToPay):
                print("Card Payment Successful")
        
        else:
            print("**** Error : Wrong Payment Type Selected")

        myCatalog.updateItem(itemIdChoice,('quantity', -1))

    input("Press Any Key to Continue")
    condition = True