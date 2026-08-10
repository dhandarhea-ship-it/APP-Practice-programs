a=10
class student:
  b=20

  def __init__(self):
    self.d=40

  def show(self):
    c=30
    print("global=",a)
    print("static=",student.b)
    print("Instance=",self.d)
    print("local=",c)

obj=student()
obj.show()
