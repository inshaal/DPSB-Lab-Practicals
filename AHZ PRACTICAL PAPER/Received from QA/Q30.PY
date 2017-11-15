"""This class is used to get the details of the item to be bought"""

class ITEMINFO(object):
   
    
    def __init__(self):
        """Initializing all the variables used"""
        self.ICode = 0
        self.Item = 0
        self.Price = 0
        self.Qty = 0
        self.Netprice = 0
        self.Discount = 0
        
    def FindDisc(self):
        """Finds the discount from the quantity entered"""
        if self.Qty >= 20:
            self.Discount = 20
        elif self.Qty > 10:
            self.Discount = 15
            
    def Buy(self):
        """Gets the information from the customer"""
        self.ICode = input("Enter the itemcode         :")
        self.Item = raw_input("Enter the item name        :")
        self.Price = input("Enter the price            :")
        self.Qty = input("Enter the quantity of items:")
        self.FindDisc()
        self.Netprice = self.Price*self.Qty*(1-(self.Discount/100.0))
        
    def ShowAll(self):
        """Prints all the details of the items along
        with the discount and price"""
        print
        print "The details of the item is as follows"
        print "The item code is        :",self.ICode
        print "The name of the item is :",self.Item
        print "The price of one item is:",self.Price
        print "The quantity of items is:",self.Qty
        print "The discount offered is :",self.Discount
        print "The netprice is         :",self.Netprice
    
item1 = ITEMINFO()
item1.Buy()
item1.ShowAll()


#The Output of the Program is :

Enter the itemcode         :1534
Enter the item name        :Parle G
Enter the price            :45
Enter the quantity of items:17

The details of the item is as follows
The item code is        : 1534
The name of the item is : Parle G
The price of one item is: 45
The quantity of items is: 17
The discount offered is : 15
The netprice is         : 650.25
