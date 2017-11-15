 
''' Swapping of all evenly located elements of list  with following odd locations using a
user defined function named swap....      eg-list=[0,1,2,3,4,5] , swapped list=[1,0,3,2,5,4]'''

def swap(lst,sz):                                  #arguments- lst means list and sz means it's size
      for i in range(0,sz-1,2):                 #increment of 2 given for accessing even locations
            lst[i],lst[i+1]=lst[i+1],lst[i]       #swapping of elements 
      print lst


#  -----MAIN-------
l=list(input("Enter a list:"))
sze=input("Enter size of the list:")
print "Output after swapping data"
swap(l,sze)                                          #calling of the user defined function


#-----Output--------
'''Enter a list:[1,2,3,4,5]
Enter size of the list:5
Output after swapping data
[2, 1, 4, 3, 5]
'''
