#Recursive funtionc example!
def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
n=input("Enter any number ")
print fact(n)

'''
extra

recursive function to find the sum of 1 to n

def sum(n):
    if(n==0):
        return 0
    else:
        return n+(sum(n-1))
n=input("Enter any no. ")
print
'''
