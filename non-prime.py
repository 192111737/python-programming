a=int(input("enter a value:"))
b=int(input("enter b value:"))
for x in range (a,b+1):
    if x > 1:
        for i in range(2, x):
            if(x % i) == 0:
                print(x,end=" ")
                break
            else:
                print(x)
