# Write a Python program to demonstrate the use of public, protected, and private access specifiers.

class Private:
    __privatVar=12
    _protected=13
    public=14
    def __privateM(self):
        print("private methode")
        print(self.__privatVar)
    def _protectedM(self):
        print("protected methode")
        print(self._protected)
    def publicM(self):
        print("public methode")
        print(self.public)
o=Private()
o._protectedM()
# o.__privateM()
o._Private__privateM()
o.publicM()