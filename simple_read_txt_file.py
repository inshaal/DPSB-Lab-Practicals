'''
Write a simple program to read the whole text file at once and print its content
'''

fobj=open("name.txt",'r')
if not fobj:
    print "The file you entered doesn't exist. [ERROR!!]"
else:
    a=fobj.read()
    print "The content of file is : "
    print a
fobj.close()
