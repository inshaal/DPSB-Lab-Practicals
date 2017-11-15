#to accept employee's name and his basic salary of any five employees and
#store in a file EMP1.TXT and print the output


#to input employees name and basic salary

ofile = open('EMP1.TXT','w')

for i in range(5):
    name = raw_input('enter employee name:')
    basic = input('enter basic salary:')
    ofile.write(name+'~'+str(basic)+'\n')

ofile.close()

#to print the given output

infile = open('EMP1.TXT','r')

print '\t\t\t\tSALARY REGISTER'
print '-'*75
print 'S.NO. NAME   BASIC\tDA\tHra\t  Total\t    PF\t    Net-pay'
print '-'*75

for i in range(5):          #for reading name and basic
    L = infile.readline().split('~')

    name = L[0]
    basic = int(L[1])
    DA = 0.30*basic
    HRA = 0.10*basic
    Total = basic+DA+HRA
    PF = 0.10*(basic+DA)
    Net = Total-PF
    print i+1,'  ',name,' ',basic,' ',DA,'  ',HRA,' ',Total,' ',PF,' ',Net 

print '-'*75
infile.close()

#output
'''
enter employee name:arohi
enter basic salary:60000
enter employee name:harsh
enter basic salary:70000
enter employee name:arpit
enter basic salary:50000
enter employee name:akash
enter basic salary:40000
enter employee name:nidhi
enter basic salary:45000
				SALARY REGISTER
---------------------------------------------------------------------------
S.NO. NAME   BASIC	DA	Hra	  Total	    PF	    Net-pay
---------------------------------------------------------------------------
1    arohi   60000   18000.0    6000.0   84000.0   7800.0   76200.0
2    harsh   70000   21000.0    7000.0   98000.0   9100.0   88900.0
3    arpit   50000   15000.0    5000.0   70000.0   6500.0   63500.0
4    akash   40000   12000.0    4000.0   56000.0   5200.0   50800.0
5    nidhi   45000   13500.0    4500.0   63000.0   5850.0   57150.0
---------------------------------------------------------------------------

'''
