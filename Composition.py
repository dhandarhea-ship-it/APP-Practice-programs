class Engine:
    def start(self):
        print("Engine Started")

class Car:
    def __init__(self):
        self.engine = Engine()   

    def drive(self):
        self.engine.start()
        print("Car is Running")

obj = Car()
obj.drive()
