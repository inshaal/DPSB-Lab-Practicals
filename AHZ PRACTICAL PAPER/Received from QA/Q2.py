class time:
    '''class time created'''
    def __init__(self,hour,minute):
        #constructor created
        self.hour=0
        self.minute=0
        if not 0<hour<=24:
             print "hour_error" 
        if not 0<minute<60:
             print "minute_error" 
        else:
            self.hour=hour
            self.minute=minute
class myerror(Exception):
    '''class myrror created'''
    pass

#main_program
input_hr=input("ENTER HOURS:")
input_min=input("ENTER MINUTES:")
hours_error=myerror("Hours not in range 0-24..!!")
minutes_error=myerror("Minutes not in range 0-59..!!")
obj=time(input_hr,input_min)


#output-1
ENTER HOURS:99
ENTER MINUTES:32
hour_error
#output-2
ENTER HOURS:12
ENTER MINUTES:99
minute_error
#output-3
ENTER HOURS:98
ENTER MINUTES:99
hour_error
minute_error 
                                 *******************

 
  
        
