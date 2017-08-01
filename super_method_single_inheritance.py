# Super method (Single Inheritance)

class A(object): #Imp. for 'object' to be added for super method to work.
    def __init__(self):
        pass

    def display(self):
        print "in base class"

class B(A):
    def __init__(self):
        A.__init__(self)

    def display(self):
        print "In derived class "
        super(B,self).display() #This will print 'in base class'

b=B()
b.display()
