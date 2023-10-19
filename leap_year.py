year=int(input("enter the year want to check"))
if(year%4==0):
     if(year%100!=0):
       print("it is a leap year")
     else:
         print("not a leap year")
elif(year%400==0):
    print("it is a leap year") 
else:
    print("not a leap year")