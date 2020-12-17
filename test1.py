class test1:

     def __init__(self,num1,num2):
          self.num1 = num1
          self.num2 = num2

     def cal(self):
          self.add = float(self.num1) + float(self.num2)
          self.sub = float(self.num1) - float(self.num2)
          self.mul = float(self.num1) * float(self.num2)
          self.div = float(self.num1) / float(self.num2)

     def display(self):
          print("Added Answer      : "+str(self.add))
          print("Subtracted Answer : "+str(self.sub))
          print("Multiplied Answer : "+str(self.mul))
          print("Divided Answer    : "+str(self.div))

try:
     obj = test1(input("Enter Num1\n>> "),input("Enter Num2\n>> "))
     obj.cal()
     obj.display()
except:
     print("Error")
finally:
     print("\nEjected")