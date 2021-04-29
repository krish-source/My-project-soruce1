from oopsdemo import Calculator


class ChildImp(Calculator):
    num2=200

    def __init__(self):
        Calculator.__init__(self, 456, 326)

    def getcompleteData(self):
        return self.num2 + self.num + self.Summation()


obj= ChildImp()
print(obj.getcompleteData())
