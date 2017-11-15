
#Program to calculate electricity bill
fh=open('cgeb.txt','w')    #opening a file 
for i in range(5):         #taking input for data calculation
    name=raw_input('Enter consumer name:')
    prev=float(raw_input('Enter previous reading:'))
    curr=float(raw_input('Enter current reading:'))
    unit=curr-prev
    
# bill calculation as per unit 
    if unit<100:
        bill=unit*0.75
    if unit>=100 and unit<200:
        bill=unit*1.25
    if unit>=200 and unit<300:
        bill=unit*1.75
    if unit>=300:
        bill=unit*2.25
    fh.write(name+'~'+str(curr)+'~'+str(prev)+'~'+str(unit)+'~'+str(bill)+'\n')
fh.close()
# End of data input

print '----------------------------------------------------------------------'
l1=['Consumer name','  Current Reading','  Prev_reading','  Consumed_unit','  Bill amount']
print '%-10s%-5s%-5s%-5s%-5s'%(l1[0],l1[1],l1[2],l1[3],l1[4])
print '----------------------------------------------------------------------'
print '----------------------------------------------------------------------'

#--output-----
fh=open('cgeb.txt','r')
l=fh.readlines()
for x in range (len(l)):         #printing individual data
    l[x]=l[x].strip('\n')
    l[x]=l[x].split('~')
    print '%-10s%15s%15s%14s%12s%5s'%(l[x][0],l[x][1],l[x][2],l[x][3],'Rs',l[x][4])
#output
#----------------------------------------------------------------------
#Consumer name  Current Reading  Prev_reading  Consumed_unit  Bill amount
#----------------------------------------------------------------------
#----------------------------------------------------------------------
#Ritu                 56.0           34.0          22.0          Rs 16.5
#Bitu                278.0          156.0         122.0          Rs152.5
#Kitu                789.0          345.0         444.0          Rs999.0
#Situ                112.0           12.0         100.0          Rs125.0
#Titu                654.0          334.0         320.0          Rs720.0
    
