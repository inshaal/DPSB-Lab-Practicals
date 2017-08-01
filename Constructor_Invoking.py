'''Constructor Invoking - To understand how constructors are invoked from classes and their invoke sequence.
 Made using Sublime Text (Windows xP) '''

class A:
	def __init__(self):
		print "Constructor A invoked"

class B(A):
	def __init__(self):
		A.__init__(self)
		print 'Constructor B invoked'

class C(B):
	def __init__(self):
		B.__init__(self)
		print 'Constructor C invoked'

x=C()
