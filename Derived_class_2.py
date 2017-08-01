#Ques ic

#BUILD: FAILING

class student:
    def __init__(self,n,admn,marks):
        self.name=n
        self.admn=admission
        self.marks=marks

    def display(self):
        print self.name
        print self.admn
        print self.marks

class fees:
    def __init__(self,c,f):
        self.Class=c #C
        self.fee=f

    def display1(self):
        print self.Class
        print self.fee

class school(student,fees):
    def __init__(self,n,admn,marks,c,f,add):
        school.__init__(self,n,admn,marks)
        fees.__init__(self,c,f)
        self.add=add

    def display2(self):
        print self.add

s1=school('Saurabh','B-7654',123,12,"test","test")
s1.display()
s1.display1()
s1.display2()
