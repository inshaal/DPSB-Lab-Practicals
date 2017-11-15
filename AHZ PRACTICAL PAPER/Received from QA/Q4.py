#program to demonstrate use of single inheritence
#using class STUDENT(name,house)and class MARKS
#(eng,phy,chem,maths,cs)
class STUDENT():
    def __init__(self):
        self.name=''
        self.house=''
    def input_detail(self):
        self.name=raw_input('enter name of student')
        self.house=raw_input('enter name of house')
    def output_detail(self):
        print 'NAME=',self.name
        print 'HOUSE=',self.house

class MARKS(STUDENT):
    def __init__(self):
        STUDENT.__init__(self)#inherit func. to initialize name and house
        self.eng=0
        self.phy=0
        self.chem=0
        self.maths=0
        self.cs=0
    def input_marks(self):
        self.input_detail()#inherit func. to input name and house
        self.eng=input('enter marks in english')
        self.phy=input('enter marks in physics')
        self.chem=input('enter marks in chemistry')
        self.maths=input('enter marks in maths')
        self.cs=input('enter marks in cs')
    def output_marks(self):
        self.output_detail()#inherit func. to display name and house
        print 'MARKS IN ENG.=',self.eng
        print 'MARKS IN phy=',self.phy
        print 'MARKS IN chem=',self.chem
        print 'MARKS IN maths=',self.maths
        print 'MARKS IN cs=',self.cs

m=MARKS()
choice=raw_input('enter your choice')
if choice=='1':
    m.input_detail()
    m.output_detail()
elif choice=='2':
    m.input_marks()
    m.output_marks()


#OUTPUT
enter your choice1
enter name of studentPUNJ PRAKASH ANAND
enter name of houseKAVERI
NAME= PUNJ PRAKASH ANAND
HOUSE= KAVERI
>>> ================================ RESTART ================================
>>> 
enter your choice2
enter name of studentPUNJ PRAKASH ANAND
enter name of houseKAVERI
enter marks in english92
enter marks in physics97
enter marks in chemistry98
enter marks in maths99
enter marks in cs100
NAME= PUNJ PRAKASH ANAND
HOUSE= KAVERI
MARKS IN ENG.= 92
MARKS IN phy= 97
MARKS IN chem= 98
MARKS IN maths= 99
MARKS IN cs= 100
