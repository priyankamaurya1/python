print("welcome to love calculator")
name =input("enter your first name").lower()
name_2=input("enter your second name").lower()
name_1 = ( name+name_2)
T=name_1.count("t")
R=name_1.count("r")
U=name_1.count("u")
E=name_1.count("e")
l=name_1.count("l")
O=name_1.count("o")
V=name_1.count("v")
E=name_1.count("e")

true=int(T+R+U+E)
love=int(l+O+V+E)
true_love= int(str(true)+str(love))
# print(true_love)

if(true_love<10 or true_love>90):
    print(f"your score is{true_love},you are together like coke and mentos")
elif(true_love>40 and true_love<50):
    print(f"your score is{true_love},you are alright together")
else:
    print(f"your score is{true_love}")


