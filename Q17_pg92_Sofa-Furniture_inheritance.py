'''
Question 17 Page 92 NCERT
Furniture Sofa classes (inheritance)
'''

class furniture:
    def __init__(self):
        self.type=''
        self.model=''

    def getType(self):
        self.type=raw_input("Enter Type : ")

    def getModel(self):
        self.model=raw_input("Enter model : ")

    def show(self):
        print self.type,self.model

class sofa(furniture):
    def __init__(self):
        furniture.__init__(self)
        self.no_seats=0
        self.cost=0.0

    def getseats(self):
        furniture.getType(self)
        furniture.getModel(self)
        self.no_seats=input("Enter number of seats : ")

    def getcost(self):
        self.cost=input("Enter cost ")

    def show(self):
        furniture.show(self)
        print self.no_seats
        print self.cost #Not printing cost

obj=sofa()
obj.getseats()
obj.getcost()
obj.show()
