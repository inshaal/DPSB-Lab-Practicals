
""" TO CREATE A FILE STUDENTT.TXT AND STORE NAMES,HOUSESAND
AMOUNT COLLECTED"""

ofile=open("student.txt","w")

for i in range(5):
     name=raw_input("Enter your name:")
     house=raw_input("Enter your house:")
     amount=input("Enter Amount Collected:")
     ofile.write(name+"~"+house+"~"+str(amount)+"\n")
ofile.close()     

""" File is created and data are stored"""

ifile=open("student.txt","r")
stri=" "
c=0
""" File is open in read mode"""
while stri:              
     r=ifile.readline()
     """ After storeing student details we will read it from text file and print it"""
     if r=="":
          break
     a=r.split("~")
     """ a is a list  whose elements are name,house,amount collected"""
     if c==0:
          print "----------------------------------------------------------------------------------------------------------"
          print "%25s%25s%25s"%("NAME","HOUSE","AMOUNT COLLECTED")
          print "-----------------------------------------------------------------------------------------------------------"
     print "%25s%25s%30.2f"%(a[0],a[1],float(a[2]))
     """ output displayed"""
     c+=1
ifile.close()     
print "-----------------------------------------------------------------------------------------------------------"

 #OUTPUT
Enter your name:mohan
Enter your house:chenab
Enter Amount Collected:500.0
Enter your name:rishab
Enter your house:ganges
Enter Amount Collected:250.0
Enter your name:rishii
Enter your house:jhelum
Enter Amount Collected:210.0
Enter your name:eshan
Enter your house:chenab
Enter Amount Collected:200.0
Enter your name:mohit
Enter your house:jhelum
Enter Amount Collected:350.0
-----------------------------------------------------------------------------
		 NAME                   HOUSE           AMOUNT COLLECTED
-----------------------------------------------------------------------------
		 mohan                  chenab               500.00
		 rishab                 ganges               250.00
		 rishii                 jhelum               210.00
		 eshan                  chenab               200.00
		 mohit                  jhelum               350.00
-----------------------------------------------------------------------------
>>> 

     
