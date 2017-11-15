
#PROGRAM TO ACCEPT ANY 10 INTEGERS AND SEARCH ANY GIVEN NUMBER USING BINARY SEARCH METHOD.
#WRITE USER DEFINED FUNCTIONS TO input_data() to search data.

def input_data(): #initialization
  Lst = [] #Input list in ascending order
  for a in range (10):
      Lst.append(input("enter a number"))#entering number
  Lst.sort()
  ask=input("Enter no to be searched")#searching number
  print Lst
  print Bsearch(Lst,ask)
def Bsearch(Lst,item):
    beg=0
    last=len(Lst)-1
    #print last
    while beg <= last:
        mid =(beg+last)/2 #Sets the middle element
        if item == Lst[mid]:
            return mid #Checking the middle element
        elif item > Lst[mid]:
            beg = mid+1  #If ELEMENT greater than middle element then shifts the middle element
        else:
            last = mid-1 #If ELEMENT less than middle element then shifts the middle element
"""Output:
input_data()
enter a number1
enter a number3
enter a number5
enter a number6
enter a number7
enter a number8
enter a number9
enter a number10
enter a number2
enter a number4
Enter no to be searched5
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
4
"""
