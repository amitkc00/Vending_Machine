
from item import item
class catalog(object):

    def __init__(self):
        self.itemList = []
    
    def displayCatalog(self):
        for item in self.itemList:
            item.displayItem()
    
    def addItem(self, name, itemId, price, quantity):
        itemObj = item(name, itemId, price, quantity)
        self.itemList.append(itemObj)

    def checkCustomerChoice(self, itemIdChoice):
        for item in self.itemList:
            if item.getItemId() == itemIdChoice:
                return True
        return False
    
    def getItemPrice(self, itemIdChoice):
        for item in self.itemList:
            if item.getItemId() == itemIdChoice:
                return item.getItemPrice()
        return None
    
    def updateItem(self, itemIdChoice):
        for item in self.itemList:
            if item.getItemId() == itemIdChoice:
                return item.updateQuantity(item.getItemQuantity()-1)