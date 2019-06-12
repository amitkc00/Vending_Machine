class item(object):

    def __init__(self, name, itemId, price, quantity):
        self.name = name
        self.itemId = itemId
        self.price = price
        self.quantity = quantity
    
    def displayItem(self):
        print("Name = {0} \t\t Price = {1} \t\t Quantity = {2} \t\t ItemId = {3}".format(self.name, self.price, self.quantity, self.itemId))
    
    def getItemId(self):
        return self.itemId
    
    def getItemPrice(self):
        return self.price
    
    def getItemQuantity(self):
        return self.quantity
    
    def updateQuantity(self, newQuantity):
        self.quantity = newQuantity
    

