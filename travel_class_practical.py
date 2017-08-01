#ravel (visited, amount collected..) practical question.
class Travel:
    pv=0
    a=0
    def __init__(self):
        Travel.pv=Travel.pv+1
    def tick(self):
        d=raw_input('Do you want to buy the tickets? (Yes, No) : ')
        if d=='Yes' or d=='yes':
            Travel.a=Travel.a+50
    def display(self):
        print 'Total Visited : ',Travel.pv
        print 'Total amount : ',Travel.a
t1=Travel()
t2=Travel()
t1.tick()
t2.tick()
t1.display()
