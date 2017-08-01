#function overloading in class
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        pass
stu=student('Ins',0)
if hasattr(stu,'age'):
    print 'Age attribute is present '
else:
    print 'No age attribute'
print 'value of attr is ', getattr(stu,"name")
setattr(stu,'name','LOL')
print 'value of attribute name is :', getattr(stu,'name')
delattr(stu,'name')
if hasattr(stu,'name'):
    print "Name attribute is present "
else:
    print 'No name attribute '
