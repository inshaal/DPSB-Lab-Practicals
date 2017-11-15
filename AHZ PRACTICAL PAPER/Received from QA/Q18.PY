
# A fibonacci series is generated with desired number of terms
def fibonacci(i):
     """ yields the value and returns to the object"""
     yield i
          

          
limit=input("Enter the maximum number of terms in the fibonacci series:")
i=0
j=1
ch=0 #number of terms
while ch<limit:
     obj=fibonacci(i)
     print obj.next(),  #prints the values one by one
     i,j=j,i+j 
     ch+=1


#OUTPUT
>>> 
Enter the maximum number of terms in the fibonacci series:10
0 1 1 2 3 5 8 13 21 34
>>> 





     



