
def enter_data():
    '''Function to enter data'''

    datafile = open("data.txt", 'w')
    for i in range(5):
	name = raw_input("Name: ")
	cls = raw_input("Class: ")
	cat = raw_input("Category(BSP/NBSP): ")
	sex = raw_input("Sex: ")
	print

	datafile.write(name+'~'+cls+'~'+cat+'~'+sex+'\n')

    datafile.close()

def drawLine():
    '''Draws a line on the screen.'''
    print "-"* 96

def drawBoldLine():
    '''Draws a bold line on the screen.'''
    print "=" * 96

def print_data():
    #Required Variables
    bsp_count = 0
    nbsp_count = 0
    boy_count = 0
    girl_count = 0

    #Opening File
    datafile = open("data.txt", 'r')

    #Print structure

    drawBoldLine()
    print "%-24s%-24s%-24s%-24s" % ("Name", "Class", "Cat(NBSP/BSP)", "Sex")
    drawBoldLine()

    #Getting and printing data
    for record in datafile:
	name,cls, cat, sex = record.strip().split('~')

	#Boy, girl count
	if sex == 'M':
	    boy_count +=1
	elif sex == 'F':
	    girl_count += 1

	#BSP, NBSP count
	if cat == 'BSP':
	    bsp_count += 1
	elif cat == 'NBSP':
	    nbsp_count += 1

	#Print
	print "%-24s%-24s%-24s%-24s" % (name,cls, cat, sex)


    drawLine()

    print "%-15s%-15s" % ("Total BSP:", str(bsp_count))
    print "%-15s%-15s" % ("Total NBSP:", str(nbsp_count))
    print "%-15s%-15s" % ("Total Boys:", str(boy_count))
    print "%-15s%-15s" % ("Total Girls:", str(girl_count))

    #Closing file
    datafile.close()


enter_data()
print_data()



#output
Name: Rohan
Class: 12
Category(BSP/NBSP): BSP
Sex: M

Name: Manish
Class: 12
Category(BSP/NBSP): NBSP
Sex: M

Name: Nandita
Class: 12
Category(BSP/NBSP): NBSP
Sex: F

Name: Tanmay
Class: 12
Category(BSP/NBSP): BSP
Sex: M

Name: Aarohi
Class: 12
Category(BSP/NBSP): NBSP
Sex: F

=============================================================================
Name                 Class                   Cat(NBSP/BSP)           Sex
=============================================================================
Rohan                 12                        BSP                   M
Manish                12                        NBS                   M
Nandita               12                        NBS                   F
Tanmay                12                        BSP                   M
Aarohi                12                        NBS                   F
-----------------------------------------------------------------------------
Total BSP:     2
Total NBSP:    3
Total Boys:    3
Total Girls:   2
