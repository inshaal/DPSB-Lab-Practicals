'''
Question - Write a short program to write 5 names in a file. Name of file is name.txt
'''
fobj=open("name.txt",'w')
if not fobj:
    print "file doesn't exist"
else:
    fobj.write("Alex \n")
    fobj.write("John \n")
    fobj.write("Ron \n")
    fobj.write("Davis \n")
    fobj.write("Inshaal :p \n")
print "Process completed."
print "File created. Contains 5 names and name of the file is name.txt"
fobj.close()
