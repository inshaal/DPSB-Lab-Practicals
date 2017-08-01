''' Define class "Applicant" specs -
Data members - ano, name, agg, grade
private member func. "grade_me" to find grade as per the aggregate marks.
80-100 --> A, 65-80--> B, 50-65 --> C, less than 50 --> D
Methods - "enter" to enter details for data members
"result" to display the result'''

class applicant:
    def __init__(self):
        self.ano=''
        self.name=''
        self.agg=0.0
        self.grade=''
        self.marks_maths=0.0
        self.marks_physics=0.0
        self.marks_chemistry=0.0
        self.marks_cs=0.0
        self.marks_english=0.0

    def agg_calc(self):
        self.agg=((self.marks_maths+self.marks_physics+self.marks_chemistry+self.marks_cs+self.marks_english)/5)

    def __grade_me(self):
        if self.agg>=80:
            self.grade='A'
        elif self.agg>=65 and self.agg<80:
            self.grade='B'
        elif self.agg>=50 and self.agg<65:
            self.grade='C'
        elif self.agg<50:
            self.grade='D'

    def enter(self):
        self.ano=raw_input("Enter Admission no. ")
        self.name=raw_input("Enter name ")
        #self.agg=input("Enter aggregate ")
        self.marks_maths=input("Enter maths marks: ")
        self.marks_physics=input("Enter physics marks: ")
        self.marks_chemistry=input("Enter chemistry marks: ")
        self.marks_cs=input("Enter CS marks: ")
        self.marks_english=input("Enter English marks: ")
        self.agg_calc()
        self.__grade_me()

    def result(self):
        print "Admission no.: ",self.ano
        print "Name: ",self.name
        print "Aggregate: ",self.agg
        print "Your grade is: ",self.grade

obj=applicant()
obj.enter()
obj.result()
obj.enter()
obj.result()
obj.enter()
obj.result()
