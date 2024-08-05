class class1:
    def m(self):
        print("in class1")
        
class class2(class1):
    pass

class class3(class1):
    def m(self):
        print("in class3"):
        
        
class class4(class2 , class3):
    pass

obj = class4()
obj.m()