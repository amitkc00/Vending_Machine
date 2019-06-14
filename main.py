from vending import Vending
from catalog import catalog

def main():
    myVending = Vending()
    myVending.stockVending()
    myVending.welcomeScreen()


if __name__ == '__main__':
    main()
