
class Travel:
    def __init__(self):
        self.people=0
        self.amt=0
    def check(self):
        self.choi="y"
        self.conti="y"
        self.check="y"
        while self.check=="y":
            self.choi=raw_input("Do you have the ticket:") #check whether you have the ticket or not
            if self.choi.lower()=="y":
                self.people+=1
                self.conti=raw_input("Do you want to continue:") #ask whether you want to continue or not
            elif self.choi.lower()=="n":
                while True:
                    self.ticket=raw_input("Do you want to buy the ticket:") #ask whether you want to buy the ticket or not
                    if self.ticket.lower()=="y":
                        self.amt+=50
                        self.people+=1
                        self.conti=raw_input("Do you want to continue:")
                        break
                    elif self.ticket.lower()=="n":
                        self.check="n"
                        break
                    else:
                        print "Invalid input.Enter again."
            else:
                print "Invalid input.Enter again."
            if self.conti.lower()=="y":
                continue
            elif self.conti.lower()=="n":
                break
            else:
                print "Invalid input.Enter again."
                self.conti=raw_input("Do you want to continue:")
    def display_data(self):
        print "NUMBER OF PEOPLE VISITED:",self.people
        print "TOTAL AMOUNT COLLECTED:",self.amt

#MAIN PROGRAM

print "y-YES,n-NO"
obj=Travel()
obj.check()
obj.display_data()

#OUTPUT

y-YES,n-NO
Do you have the ticket:y
Do you want to continue:y
Do you have the ticket:y
Do you want to continue:y
Do you have the ticket:n
Do you want to buy the ticket:y
Do you want to continue:y
Do you have the ticket:n
Do you want to buy the ticket:y
Do you want to continue:y
Do you have the ticket:n
Do you want to buy the ticket:n
NUMBER OF PEOPLE VISITED: 4
TOTAL AMOUNT COLLECTED: 100
                
                
            
                
                
            
