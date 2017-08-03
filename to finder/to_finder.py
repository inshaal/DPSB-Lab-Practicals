'''
Question: How many 'to' are there in a sentence provided by user entered in a text file.
'''
y=0
fobj=open("tofinder.txt",'r')
if not fobj:
    print "file doesn't exist"
else:
    a=fobj.readline()
    x=len(a)
    for i in range(x):
        if a[i]=='t' or a[i]=='T':
            if a[i+1]=='o' or a[i+1]=='O':
                y=y+1

print "Search completed."
fobj.close()
print 'Number of "to" are : ',y
