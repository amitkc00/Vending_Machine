from catalog import catalog
from cashPayment import cashPayment
from cardPayment import cardPayment
from pdb import set_trace
from enum import Enum
import os
#####

class PAYMENT_TYPE(Enum):
    CASH = 1
    CARD = 2

class Vending(object):

    def __init__(self):
        self.myCatalog = catalog()
        
    @staticmethod
    def processPayment(amount):
        paymentChoice = input("Pay by CASH or CARD. Enter 1 for CASH, 2 for CARD = ")
        paymentChoice = int(paymentChoice)

        #set_trace()
        if paymentChoice == PAYMENT_TYPE.CASH.value:
            input("Press any key to Confirm Cash Payment")
            payment = cashPayment(amount)
        elif paymentChoice == PAYMENT_TYPE.CARD.value:
            payment = cardPayment(amount)
        else:
            print("Wrong Payment ")
            return False
        
        if payment.processPayment():
            print("Payment Successful. Item ready to be dispatched.")
            return True

    def welcomeScreen(self):
        os.system('clear')
        print("\n **** Welcome to Amit Vending Machine. ****")
        print("Please select the Item from below list \n")
        print("\nName \t\t\t Price \t\t\t Quantity \t\t\t ItemID ")
        self.myCatalog.displayCatalog()

        itemIdChoice = input("Enter the Item Id = ")
        itemIdChoice = int(itemIdChoice)

        if not self.myCatalog.checkCustomerChoice(itemIdChoice):
            print("**** Error : Wrong Item Selected *****") 
        else:
            itemPrice = self.myCatalog.getItemPrice(itemIdChoice)
            paymentOk = Vending.processPayment(itemPrice)
            if paymentOk:
                self.dispatchItem(itemIdChoice)
    
    def stockVending(self):
        self.myCatalog.addItem('TWIX',11,1,10)
        self.myCatalog.addItem('WATER',12,.5,10)
        self.myCatalog.addItem('MINT',13,.25,20)
    
    def dispatchItem(self, itemIdChoice):
        #Reduce Item Quantity by 1.
        self.myCatalog.updateItem(itemIdChoice)
        print("**** Succcess : Item Dispatched ****")