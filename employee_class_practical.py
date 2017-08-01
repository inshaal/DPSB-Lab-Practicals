#employee ques. from practicals list, (hra,da calculations.. )
class employee:
    def __init__(self):
        self.name=''
        self.basic=0.0
        self.DA=0.0
        self.HRA=0.0
        self.GP=0.0
        self.PF=0.0
        self.tax=0.0

    def Input1(self):
        self.name=raw_input("Enter your name : ")
        self.basic=input("Enter Basic pay : ")
        self.DA=0.15*self.basic
        self.HRA=0.30*self.basic
        self.PF=0.12*self.basic
        self.GP=self.DA+self.HRA+self.basic
        return self.GP

    def calctax(self):
        if self.GP<35000:
            self.tax=0
        if self.GP>=35000 and self.GP<=60000:
            self.tax=0.30*self.GP
        if self.GP>60000 and self.GP<120000:
            self.tax=0.35*self.GP
        if self.GP>120000:
            self.tax=0.40*self.GP
        return self.tax

    def dis(self):
        print self.name
        print self.basic, ': BASIC PAY'
        print self.DA, ': DA'
        print self.HRA, ': HOUSE RENT ALLOWANCE'
        print self.GP, ': GP'
        print self.PF, ': PF'
        print self.tax, ': TAX'

obj=employee()
obj.Input1()
obj.calctax()
obj.dis()





