 
def List_palindrome(l):
    global ans_l
    ans_l=[]
    for word in l:                              #For loop
        string=""                               #empty string
        for i in range((len(word)-1),-1,-1):    #For loop
            string+=word[i]                     #reversing word
        if string==word:                        #if condition
            ans_l.append(word)

mfile=open("WORDS.TXT","w")                     #opening a file
cont="y"        
lines=0
while cont.lower() =="y":                        #while loop
        st=raw_input("Enter a word:")
        cont=raw_input("Do you want to continue?(y/n):")
        mfile.write(st+"\n")                    #writing in file
        lines+=1                                #counting lines of file
mfile.close()                                   #closing a file

L=[]                                            #empty list         
ofile=open("WORDS.TXT","r")                     #opening a file
for i in range(0,lines):                        #for loop
    unit=ofile.readline().strip()               #reading words from file
    L.append(unit)
ofile.close()                                   #closing a file
List_palindrome(L)                              #calling a function
if ans_l==[]:
    print "There are no words which are palindrome"
else:
    print "The words which are palindrome are:"
    for ans in ans_l:
        print ans
#OUTPUT
"""
Enter a word:SIDHANT
Do you want to continue?(y/n):Y
Enter a word:HELLO
Do you want to continue?(y/n):Y
Enter a word:MADAM
Do you want to continue?(y/n):Y
Enter a word:NAYAN
Do you want to continue?(y/n):N

The words which are palindrome are:
MADAM
NAYAN
"""
