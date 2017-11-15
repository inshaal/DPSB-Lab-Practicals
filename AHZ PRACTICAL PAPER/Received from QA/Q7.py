
#Question-7

class Student:
      def __init__(self,roll,name):
            self.roll=roll
            self.name=name
      def Getdata(self):
            self.roll=input("Enter roll number:")
            self.name=raw_input("Enter name:")
      def Printdata(self):
            print "Name of student:", self.name
            print "Roll number of studnet:", self.roll

class Marks(Student):
      """Inheriting from STUDENT"""
      def __init__(self,roll,name,eng,phy,maths,chem,cs):
            Student(roll,name)
            self.eng=eng
            self.phy=phy
            self.maths=maths
            self.chem=chem
            self.cs=cs
      def Inputdata(self):
            Student.Getdata(self)
            self.eng=input("Enter English marks:")
            self.phy=input("Enter Physics marks:")
            self.chem=input("Enter Chemistry marks:")
            self.maths=input("Enter Maths marks:")
            self.cs=input("Enter CS marks:")
      def Outdata(self):
            Student.Printdata(self)
            print "English marks:", self.eng
            print "Physics marks:", self.phy
            print "Chemistry marks:", self.chem
            print "Maths marks:", self.maths
            print "Computer Science marks:", self.cs

a=Marks(42,"Yash",0,0,0,0,0)
a.Inputdata() #Calling function
a.Outdata()   #Calling function


#OUTPUT

#Enter roll number:42
#Enter name:Yash
#Enter English marks:78
#Enter Physics marks:98
#Enter Chemistry marks:98
#Enter Maths marks:62
#Enter CS marks:90
#Name of student: Yash
#Roll number of studnet: 42
#English marks: 78
#Physics marks: 98
#Chemistry marks: 98
#Maths marks: 62
#Computer Science marks: 90


