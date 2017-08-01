#Public Protected & Private members.

class DATAnCap:
    def __init__(self,n1,n2,n3):
        self.public=n1
        self._protected=n2
        self.__private=n3

obj=DATAnCap(10,20,30)
print 'Public member : ',obj.public
print 'protected member : ',obj._protected
print 'Private member : ',obj._DATAnCap__private #notice the command to call the private member is different.
