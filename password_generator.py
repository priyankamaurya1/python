import random

print("welcome to pypassword genrator")
letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
         'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ,'A','B','C','D','E', 
         'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
         'U', 'V', 'W', 'X', 'Y', 'Z']

symbol=['!','@','#','$','%','^','&','*']
number=['0','1','2','3','4','5','6','7','8','9']

i_letters =int(input("how many letters do you like in your password"))
i_symbol=int(input("how many symbol would you like"))
i_number=int(input("how many number would you like"))
# password=''
password=[]


    # for i in range(0,i_letters):
    #     random_letter =random.choice(letters)
    #     password+=random_letter
    # # print(password)
    # for i in range(0,i_symbol):
    #     password +=random.choice(symbol)
    # for i in range(0,i_number):
    #     password +=random.choice(number)             
    # print(password)
    # password_i=random.choice(password)

for i in range(0,i_letters):
    password =random.choice(letters)
for i in range(0,i_symbol):
    password +=random.choice(symbol)
for i in range(0,i_number):
    password +=random.choice(number)
    
random.shuffle(password)
        

print("here your password:",password)
