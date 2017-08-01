#Static method - In which self parameter is not present.

class STATIC:
    @staticmethod #necessary to make a static function.
    def stmethod1():
        a,b=2,5
        _s=a+b
        print _s
    @staticmethod
    def stmethod2(x,y=5):
        a,b=x,y
        _s1=a+b
        print _s1
z=input("Enter a number for stmethod2 function : ")
STATIC.stmethod1()
STATIC.stmethod2(z)
    
