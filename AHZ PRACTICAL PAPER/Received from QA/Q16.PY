""" Accept date and print it in the given format."""


day={1:"st",2:"nd",3:"rd",4:"th",5:"th",6:"th",7:"th",8:"th",9:"th",10:"th",11:"th",12:"th",13:"th",14:"th",15:"th",16:"th",17:"th",18:"th",19:"th",20:"th",21:"st",22:"nd",23:"rd",25:"th",26:"th",27:"th",28:"th",29:"th",30:"th",31:"st"}
month={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July", 8:"August",9:"September",10:"October",11:"November",12:"December"}

#------------MAIN------------

date=raw_input("Enter date: ")
day_date=int(date[0:2])
year=int(date[-4:])
date=date[:-4]                                          #To remove year
month_date=int(date[2:])

print  str(day_date) + str(day[day_date]) , month[month_date], year

#------------OUTPUT-----------

"""Enter date: 10112006
   10th November 2006

   Enter date: 0122006
   1st February 2006

   Enter date: 2252007
   22nd May 2007

   Enter date: 2352007
   23rd May 2007"""
