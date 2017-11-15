
"""program to accept 10 values, make a list and then sort in descending order
using bubble sort"""

#function to accept 10 values and make a list
def accept():  
    l=[]
    for x in range(0,10):
        y= input("enter number")
        l=l+[y]
    return l

#function to sort list
def bubble_sort(l):
    for x in range (0, len(l)):
        for y in range(0, len(l)-1-x):
            if l[y]<l[y+1]:
                l[y],l[y+1]=l[y+1], l[y]
    return l

#function to print list
def print_data(l):
    return l

#main function to call previous three functions
def sort():
    l= accept()
    l1= bubble_sort(l)
    l2= print_data(l1)
    print l2

#calling main function
sort()

#output

enter number6
enter number6
enter number4
enter number1
enter number7
enter number5
enter number1
enter number2
enter number0
enter number1
[7, 6, 6, 5, 4, 2, 1, 1, 1, 0]

