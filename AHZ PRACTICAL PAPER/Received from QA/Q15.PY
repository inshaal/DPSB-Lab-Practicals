

def queue():
    """This function takes a linear queue and performs the following functions:
	  1)Add 2)Delete 3)View 4)Quit"""

    list1=eval(raw_input("Enter any 10 numbers in desired format"))   #takes the list
    if len(list1)!=10:
	#checks if the length of the list is equal to 10.Else Terminates the program

	print "The length of the given queue is not equal to 10.Please try again! Bye Program Terminated"
	exit()
    #Menu

    input1=raw_input( """Press '1' to Add any element\nPress '2' To Delete an element
Press '3' To View the queue\nPress '4' To Quit\n""")
    if input1=="1":
	#Option no.1 to add an element to the list entered

	element=int(raw_input("Enter the element to be added"))
	list1.append(element)
	print "The new queue is",list1
    elif input1=="2":
	#Option no.2 to remove an element from the given list.If not found returns an error

	element=int(raw_input("Enter the element to be removed"))
	if element in list1:
		list1.remove(element)
	else:
		print "Sorry,the entered element was not found in the given list"
	print "The new queue is:",list1
    elif input1=="3":
	#Option no.3 to print the given list

	print "The queue is",list1
    elif input1=="4":
	#Option no.4 to exit the program
	exit()
    else:
	#Prints "Invalid input" if invalid option is entered

	print "Invalid Input"
queue()    #Calling the function

"""Run 1:
Enter any 10 numbers in desired format[1,2,3,4,5,6,7,8,9,10]
Press '1' to Add any element
Press '2' To Delete an element
Press '3' To View the queue
Press '4' To Quit
1
Enter the element to be added11
The new queue is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]"""
"""Run 2:
Enter any 10 numbers in desired format[1,2,3,4,5,6,7,8,9,10]
Press '1' to Add any element
Press '2' To Delete an element
Press '3' To View the queue
Press '4' To Quit
2
Enter the element to be removed9
The new queue is: [1, 2, 3, 4, 5, 6, 7, 8, 10]"""
"""Run 3:
Enter any 10 numbers in desired format[1,2,3,4,5,6,7,8,9,10]
Press '1' to Add any element
Press '2' To Delete an element
Press '3' To View the queue
Press '4' To Quit
3
The queue is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"""
"""Run 4:
Enter any 10 numbers in desired format[1,2,3,4,5,6,7,8,9,10]
Press '1' to Add any element
Press '2' To Delete an element
Press '3' To View the queue
Press '4' To Quit
4
>>> """
