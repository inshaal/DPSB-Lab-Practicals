'''
Write a program to store 1 to 100 in a file. Name of file is number.txt
'''

fobj=open("number.txt",'w') #change 'w' to 'a' to add more on next code run for same file
if not fobj:
    print "[ERROR!!] File doesn't exist"
else:
    for i in range(1,100):
        fobj.write(str(i)+"\n")
print "Process completed"
print "A text file containg 1 to 100 created with file name 'number.txt'"
fobj.close()
