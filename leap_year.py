date=int(input("enter the date to check:"))
if(input_year%4==0):
    if(input_year%100==0):
        if(input_year%400==0):
            print("%d is a leap year"%input_year)
        else:
            print("%d is not a leap year"%inpuut_year)
    else:
        print("%d is a leap year"%input_year)
else:
     print("%d is not a leap year"%input_year)
x=input_year%4
if x!=0:
   print("previous leap year:",input_year-x)
else:
     print("next leap year:",input_year+4)
            
