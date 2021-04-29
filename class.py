class Calculator:
    num = 56 #Class variables

    #default constuctor

    def _init_(self, a, b):
        self.firstnumber = a
        self.secondnumber = b
        print("I'm calld auto when object is called")

    def getData(self):
        print("Executing class function")

    def Summation(self):
        return self.firstnumber + self.secondnumber + self.num  # we can use self for caclulator for only class variable
        


obj = Calculator(4, 3)  #syntax to create objects
obj.getData()
print(obj.Summation())



obj1 = Calculator(12, 45)  #syntax to create objects
obj.getData()
print(obj.Summation())
