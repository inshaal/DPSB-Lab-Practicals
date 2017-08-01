#SUPER METHOD (FOR MULTIPLE INHERITANCE)

class A(object):
    def __init__(self):
        pass

    def display(self):
        print 'In Class A'

class B():
    def __init__(self):
        print 'In class B'

class C(B,A):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)

    def display(self):
        print 'In Class C'
        super(C,self).display()

b=C()
b.display()
