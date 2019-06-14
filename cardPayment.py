from payment import payment

class cardPayment(payment):
    def __init__(self, cardNumber, cardExpiry, cardCvv):
        pass
    
    def processPayment(self, itemPrice):
        return True