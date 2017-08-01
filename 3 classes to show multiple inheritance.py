#WAP to demonstrate multiple inheritance using 3 classes

class person:
    def __init__(self):
        self.pname=''
        self.page=0.0
        
    def p_input(self):
        self.pname=raw_input("Enter name : ")
        self.page=input("Enter age : ")

    def p_display(self):
        print self.pname,self.page

class employee:
    def __init__(self):
        self.empcode=0.0
        self.empdesign=''
        self.empsalary=0.0

    def e_input(self):
        self.empcode=input("Enter the code : ")
        self.empdesign=raw_input("Enter designation : ")
        self.empsalary=input("Enter the salary : ")

    def e_display(self):
        print self.empcode,self.empdesign,self.empsalary

class teacher(person,employee):
    def __init__(self):
        person.__init__(self)
        employee.__init__(self)

    def getdata(self):
        person.p_input(self)
        employee.e_input(self)

    def showdata(self):
        person.p_display(self)
        employee.e_display(self)

t=teacher()
t.getdata()
t.showdata()
