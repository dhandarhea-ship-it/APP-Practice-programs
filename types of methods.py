class method:
    def show(self):
        print("This is instance method")

    @staticmethod
    def hello():
        print("this is static method")

    def __str__(self):
        return"this is magic method"
obj=method()
obj.show()
method.hello()
print(obj)
