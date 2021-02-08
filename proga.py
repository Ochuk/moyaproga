def plus(x, y):
   return x + y

def minus(x, y):
   return x - y

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1,"+",num2,"=", plus(num1,num2))
print(num1,"-",num2,"=", minus(num1,num2))