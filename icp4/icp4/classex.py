class student():
    def __init__(self,name,age):
        print("hai")
        self.studentname=name
        self.studentage=age
    def get_age(self):
        print("age of student {} is {}".format(self.studentname,self.studentage))
b=student("bob",21)##instance
b.get_age()
print (b.studentname)
##usedefined
class python(student):
    def __init__(self):
        print("student")
        student.__init__(self,"tom"23)
        print("stdent ()".format(studetn.__init))
s=python()