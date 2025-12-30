class MethodOverride1:
    def display(self):
        print("method invoked from base class")
class MethoOverride2(MethodOverride1):
    def display(self):
        print("method invoked from derived class")
ob=MethoOverride2()
ob.display()