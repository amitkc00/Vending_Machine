from payment import payment

class cashPayment(payment):
    def __init__(self, itemPrice):
        self.itemPrice = itemPrice
        
    
    def processPayment(self):
        return True