##Question 27
 

def input_data():
    """Takes names and capitals of any five countries provided
       by the user and stores it in QUIZ.DBF"""

    ofile = open("QUIZ.DBF","w")
    for i in range(5):
	country = raw_input("Enter country: ").strip()
	capital = raw_input("Enter capital: ").strip()
	print
	ofile.write(country+","+capital+"\n")
    ofile.close()

def View_data():
    """User enters the country and the computer shows the capital"""
    ofile = open("QUIZ.DBF","r")

    country = raw_input("Enter country to find its capital: ").strip()
    ##Asks user for the country.
    readline = ofile.readline().strip()
    rdl_lst = readline.split(",")

    while readline!="":
	##rdl_lst[0] is the country name stored in the QUIZ.DBF
	##rdl_lst[1] is the capital name stored in the file QUIZ.DBF
	if rdl_lst[0]== country:
	    print "Capital of the country is %s." % (rdl_lst[1])
	    break
	else:
	    pass
	readline = ofile.readline().strip()
	rdl_lst = readline.split(",")
    else:
	print "Country is not stored in QUIZ.DBF."
    ofile.close()
##Run the functions.
input_data()
View_data()


"""
#OUTPUT
Enter country: India
Enter capital: New Delhi

Enter country: Japan
Enter capital: Tokyo

Enter country: USA
Enter capital: Washington DC

Enter country: China
Enter capital: Beijing

Enter country: France
Enter capital: Paris

Enter country to find its capital: USA
Capital of the country is Washington DC.
"""
