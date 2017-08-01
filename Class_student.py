'''Define a class 'Student' with these specs...
instance data members - Admission number, Name, Percentage.
Member functions - get data to enter the values of admission no. , name and %age
Display details of students on the screen.'''

class student:
    def __init__(self):
        self.adm_no=''
        self.name=''
        self.percent=0.0

    def get_data(self):
        self.adm_no=raw_input("Enter admission number ")
        self.name=raw_input("Enter name ")
        self.percent=input("Enter percentage % ")

    def display(self):
        print "admisssion no. : ", self.adm_no
        print "Name : ",self.name
        print "percentage : ",self.percent

obj=student()
obj.get_data()
obj.display()
