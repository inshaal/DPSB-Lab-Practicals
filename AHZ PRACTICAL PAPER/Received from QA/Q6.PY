#file input

def input_phone():

    '''Function to enter the records in the file STD.TXT
    '''

    ofile=open('STD.TXT','a')
    for i in range(5):
        name=raw_input("Enter the name: ").upper()
        phone=raw_input("Enter the phone no.:")
        ofile.write(name+'~'+phone+'\n')
        print "Data written into the file"
    ofile.close()

def output_phone():

    '''Function to print the phone no. and name if found otherwise print
       'Not Found in directory'
    '''

    ofile=open('STD.TXT','r')
    i_name=raw_input("Enter the name :").upper()
    rec=ofile.readline().strip()
    while rec!='':
        l_rec=rec.split('~')
        if l_rec[0]==i_name:
            print 'Name'+'\t'+'\t'+'Phone NO.'
            print l_rec[0]+'\t'+'\t'+l_rec[1]
            break
        rec=ofile.readline().strip()
    else:
        print "The Phone Number Not Found In The Directory"
    ofile.close()
#-----------------------------------------------------------------------------------    

count=input("Enter the no.of names to view:")
for i in range(count):
    output_phone()

#OUTPUT    
'''
Enter the name: XYZ
Enter the phone no.:1234567890
Data written into the file
Enter the name: ABC
Enter the phone no.:1987654321
Data written into the file
Enter the name: RED
Enter the phone no.:1243658709
Data written into the file
Enter the name: TYU
Enter the phone no.:2314576890
Data written into the file
Enter the name: POP
Enter the phone no.:2314756089
Data written into the file

--------------------------------

Enter the no.of names to view:3
Enter the name :xyz
Name		Phone NO.
XYZ		1234567890
Enter the name :abc
Name		Phone NO.
ABC		1987654321
Enter the name :red
Name		Phone NO.
RED		1243658709
Enter the name :afg
The Phone Number Not Found In The Directory
'''
