
#Program to accept the data and print stream according to given conditions
class STUDENT:
    def __init__(self,name='',rno=0,marks=[]):
	self.name = name
	self.rno = rno
	self.marks = marks

    def inp(self): #to input name,marks and roll number of student
	self.name = raw_input("Enter name: ")
	self.rno = input("Enter roll no.: ")
	self.marks = list(input("Enter marks list (separated by comma): "))

	msum = sum(self.marks)

	perc = ((msum/5))

	print "Name:", self.name #to print name,roll number and stream
	print "Roll no.: ", self.rno

	if perc >= 96:
	    print "Stream: Computer Science"

	elif perc >= 91:
	    print "Stream: Electronics"

	elif perc >= 86:
	    print "Stream: Mechanical"

	elif perc >= 81:
	    print "Stream: Electrical"

	elif perc >= 76:
	    print "Stream: Chemical"

	elif perc >= 71:
	    print "Stream: Civil"

	else:
	    print "Stream: Not alloted"

#-------------------------------MainProgram---------------------------------

stud1 = STUDENT()
stud1.inp()

#-------------------------------Output---------------------------------------

Enter name: srishti
Enter roll no.: 744
Enter marks list (separated by comma): [90,90,90,90,90]
Name: srishti
Roll no.:  744
Stream: Mechanical
>>> ================================ RESTART ================================
>>>
Enter name: holo
Enter roll no.: 555
Enter marks list (separated by comma): [35,35,35,35,35]
Name: holo
Roll no.:  555
Stream: Not alloted
>>>

