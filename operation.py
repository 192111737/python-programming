a=float(input("enter the first number:"))
b=float(input("enter the second number:"))

operation=input("enter the operation(+,-,*,/):")

if operation == "+":
   result=a+b
elif operation == "-":                      
   result=a-b
elif operation == "*":
   result=a*b
elif operation== "/":
   result=a/b
else:
    print("invalid operation:")
print("result:",result)
