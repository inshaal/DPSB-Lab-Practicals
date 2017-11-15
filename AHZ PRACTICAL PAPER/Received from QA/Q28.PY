 
class date:
    def __init__(self):
	self.dd=0                    #date
	self.mm=0                    #month
	self.yyyy=0                  #year
	self.months=[31,28,31,30,31,30,31,31,30,31,30,31]

    # to update for leap year

    def leap_update(self):
	y=self.yyyy
	if y%4==0 or y%100==0 or y%400==0:
	    self.months[1]=29
	else:
	    self.months[1]=28

    #To enter date, month,year

    def input_date(self):
	self.dd=input('Enter dd:')          #input date
	self.mm=input('Enter mm:')          #input month
	self.yyyy=input('Enter yyyy:')      #input year
	self.leap_update()

    #To add days to the given date

    def add_days(self,num=10):
	self.dd+=num
	while self.dd>self.months[self.mm-1]:
	    self.dd=self.dd-self.months[self.mm-1]
	    self.mm+=1
	    if self.mm>12:
		self.mm=1
		self.yyyy+=1
	    self.leap_update()

    # To display the date

    def disp_date(self):
	print 'Entered date + 10:'
	print self.dd,'/',self.mm,'/',self.yyyy

#Main part of the program

obj=date()
obj.input_date()
obj.add_days(10)
obj.disp_date()


#OUTPUT
Enter dd:23
Enter mm:11
Enter yyyy:2016
Entered date + 10:
3 / 12 / 2016

