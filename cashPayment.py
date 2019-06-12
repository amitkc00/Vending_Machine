from payment import payment

class cashPayment(payment):
    def __init__(self):
        pass
    
    def processPayment(self, itemPrice):
        return True