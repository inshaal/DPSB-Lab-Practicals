""" 
A program to store any 10 names in the list and print all names in alphabetical order
using selection sort"""
def selection_sort(lst):
    #Sorting a list using selection sort
    length=len(lst)
    for i in range(length):
        for j in range(i+1, length):
            if lst[i]>lst[j]:
                lst[i], lst[j]=lst[j], lst[i]
            else:
                continue
    #List sorted

#-------Main--------
name=' '
lst=[]

for i in range(10):
    name=raw_input("Enter the name of the person to be stored: ")
    lst.append(name.lower())
print 'Initially the list is ', lst               #Printing the initial list

selection_sort(lst)

print "Printing the sorted list", lst               #Printing the sorted list

        #Output

"""Enter the name of the person to be stored: Rishabh
Enter the name of the person to be stored: Roahn
Enter the name of the person to be stored: Aditya
Enter the name of the person to be stored: Pushpak
Enter the name of the person to be stored: Singh
Enter the name of the person to be stored: Vaibhav
Enter the name of the person to be stored: Sahu
Enter the name of the person to be stored: Roy
Enter the name of the person to be stored: Sanjeet
Enter the name of the person to be stored: Maiti
Initially the list is  ['rishabh', 'roahn', 'aditya', 'pushpak', 'singh', 'vaibhav', 'sahu', 'roy', 'sanjeet', 'maiti']
Printing the sorted list ['aditya', 'maiti', 'pushpak', 'rishabh', 'roahn', 'roy', 'sahu', 'sanjeet', 'singh', 'vaibhav']
"""


