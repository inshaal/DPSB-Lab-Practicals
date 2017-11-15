'''  
programme on directory'''

myfile=open('PHONE.DAT','w')
for a in range(5):
    name=raw_input('enter name:')
    number=raw_input('enter telephone number:')
    myfile.write(name+'-'+number+'\n')
myfile.close()

ofile=open('PHONE.DAT','r')#file for reading 
l=ofile.readlines()#the lines are taken in a list
l2=[]

'''list of lists of name and phonenumbers is created'''

for a in l:
    l2.append((a.strip()).split('-'))

'''list of names and their numbers formed'''

d={}#dictionary for names and their numbers

for a in l2:
    
    '''dictionary is formed'''
    d[a[0]]=a[1]

print

name=raw_input('enter name to be found:')

if name in d:
    print 'the no to be found is:',d[name]
else:
    print 'NOT FOUND'

'''output:

enter name:rohan
enter telephone number:7587116563
enter name:nitin
enter telephone number:9999985819
enter name:aditya
enter telephone number:7587116569
enter name:pushpak
enter telephone number:4587169535
enter name:harsh
enter telephone number:3545285132

enter name to be found:rohan
the no to be found is: 7587116563'''
