print("welcome to pizza order service")
size =(input('what size do you want "S","M","L"')).upper()
add_pepperoni=input("do you want add pepperoni 'Y', 'N'",).upper()
extra_chease=input("do you want to add extra chease'Y','N'").upper()
bill=0
if("S"==size):
    bill+=15
    

elif(size=="M"):
     bill+=20
else:
     bill+=25

if(add_pepperoni=="Y"):
     if(size=="S"):
          bill+=2
     else:
          bill+=3

if(extra_chease=="Y"):
    bill+=1

print(f"your total bill is,{bill}")
      
