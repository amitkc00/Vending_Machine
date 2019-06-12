from payment import payment

class cardPayment(payment):
    def __init__(self):
        pass
    
    def processPayment(self, cardDetails, amount):
        return True