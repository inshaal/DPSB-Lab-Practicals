#Single Inheritance ques. base

#Build : failing

class school:
    def __init__(self,n,a,add):
        self.basename=n
        self.baseage=a
        self.baseadd=add #add here is address
    def display(self):
        print "Name of base ",self.basename
        print "Age of base ",self.baseage
        print "Address of base ",self.baseadd

class student(school): #format to use inheritance...
    def __init__(self,n,a,add,marks):
        self.marks=marks

   # def diplay1(self): #removed this part temporarily (to find the error)

s1=student('Someone','add',88,0)
s1.display()
s1.display1()
            
