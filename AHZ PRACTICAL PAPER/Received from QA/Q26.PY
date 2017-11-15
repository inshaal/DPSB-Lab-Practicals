
#function to accept a queue in form of list
def accept():
    l=[]
    choice="yes"
    while choice=="yes":
        city_name=raw_input("enter name of city:")
        l.append(city_name)
        choice=raw_input("enter yes to continue:")
    return l
#function to add item in the queue
def add_queue(lst):
    item=raw_input("enter name to add")
    lst.append(item)
    print item,"inserted"
#function to pop from the queue
def delete_queue(lst):
    if len(lst)==0:
        print "underflow"
    else:
        item=lst.pop(0)
        print "item deleted:",item
#function to view the queue 
def view_queue(lst):
    print "queue:",lst
#----------------------------main-------------------------------
queue=accept()
print
print
print
print "-"*30,"MAIN MENU","-"*30
print "\t\t\t\t1.add\n\t\t\t\t2.delete\n\t\t\t\t3.view\n\t\t\t\t4.exit"
#loop to run the main program
ch=0
while ch!=4:
    ch=int(raw_input("enter choice:"))
    if ch==1:
        add_queue(queue)
    if ch==2:
        delete_queue(queue)
    if ch==3:
        view_queue(queue)
else:
    print "Thank you"
##output
""" 
enter name of city:Delhi
enter yes to continue:yes
enter name of city:mumbai
enter yes to continue:yes
enter name of city:kolkata
enter yes to continue:no



------------------------------ MAIN MENU ------------------------------
				1.add
				2.delete
				3.view
				4.exit
enter choice:1
enter name to add:chennai
chennai inserted
enter choice:3
queue: ['Delhi', 'mumbai', 'kolkata', 'chennai']
enter choice:2
item deleted: Delhi
enter choice:3
queue: ['mumbai', 'kolkata', 'chennai']
enter choice:2
item deleted: mumbai
enter choice:2
item deleted: kolkata
enter choice:3
queue: ['chennai']
enter choice:2
item deleted: chennai
enter choice:3
queue: []
enter choice:2
underflow
enter choice:4
Thank you'''

    
        
        
    
