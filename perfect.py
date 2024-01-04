num=input("enter a number:")
sum_v=0
for i in range(1,num):
  if(num%i==0):
   sum_v=sum_v+i
if(sum_v==num):
  print("perfect number:")
else:
  print("not a perfect number:")

          
