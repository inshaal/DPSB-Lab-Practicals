'''Destructor invoking - To understand how destructors are invoked.
 Made using Sublime Text for Windows xP'''

class A:
	def __del__(self):
		print "Destructor A removed"

class B(A):
	def __del__(self):
		z=A()
		print "Desctructor B removed"

class C(B):
	def __del__(self):
		y=B()
		print "Destructor C removed"

x=C()
del(x)