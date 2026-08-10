from abc import ABC, abstractmethod

class Test(ABC):

    @abstractmethod
    def show(self):
        pass

class Demo(Test):

    def show(self):
        print("Hello")

obj = Demo()
obj.show()
