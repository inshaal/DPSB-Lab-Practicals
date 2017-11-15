


def login_store():
    """This function stores 5 login names
       along with corresponding passwords"""

    t=()  # Empty tuple (will store login name and password)

    print "Enter 5 login names and password!"
    for i in range(5):
        ask1=raw_input("Enter Login Name:") #asks user to enter  login name
        ask2=raw_input("Enter Password:")   #asks user to provide a login password
        t+=(ask1,ask2)

        
    print "Login Names and passwords saved succesfuly!"
    
    return t  #returns the tuple storing login name and password

def login(t):
    """This function checks if both login name
       and login password is correct """
    print "Welcome! Please provide the following details! \n"
    ask3=raw_input("Enter your Login Name:")     #asks user to enter his/her login name
    ask4=raw_input("Enter your Login Password:") #asks user to provide the login password

    if ask3 not in t: #checking whether user has an account
        print "User does not exist!"

    else:             #if user exists , password is checked
        for i in range(9):
            if t[i]==ask3: 
                if t[i+1]==ask4:
                    print "Access allowed"
                else:
                    print "Access denied"

#_____________________function is called_____________________
login(login_store())
#---OUTPUT---
>>>
Enter 5 login names and password!
Enter Login Name:Nayan
Enter Password:1605
Enter Login Name:Pi
Enter Password:3.141592653589793
Enter Login Name:Harsh
Enter Password:hjrs
Enter Login Name:Rohan
Enter Password:1717
Enter Login Name:Rishabh
Enter Password:chakunslap
Login Names and passwords saved succesfuly!
Welcome! Please provide the following details! 

Enter your Login Name:Nayan
Enter your Login Password:1605
Access allowed
                
