class complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def shownumber(self):
        print(f"{self.real}i+{self.imag}j")
    def add(self,num2):
        newreal=self.real+num2.real
        newimag=self.imag+num2.imag
        return complex(newreal,newimag)
num1=complex(1,6)
num1.shownumber()
num2=complex(2,5)
num2.shownumber()
num3=num1.add(num2)
num3.shownumber()
