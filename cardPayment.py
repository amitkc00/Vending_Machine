from payment import payment

class cardPayment(payment):
    def __init__(self, itemPrice):
        self.itemPrice = itemPrice
        
    
    def processPayment(self):
        self.getCustomerCardDetails()
        result = self.authorizePayment()
        return result
    
    def getCustomerCardDetails(self):
        print("Please Enter your Card Details")
        self.cardNumber = input("Enter the Card Number = ")
        self.cardExpiry = input("Enter Expiry in MMYY format = ")
        self.cardCvv = input("Enter the CVV code = ")
        input("Press any key to Confirm Card Payment")

    
    def authorizePayment(self):
        return True