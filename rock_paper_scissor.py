import random
print("welcome to rock paper scissor game")
rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  

'''
paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''
scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''
choices= [rock, paper, scissors]         
computer_choice =random.randint(0,2)
user_choice=int(input("enter 0 for rock,1for paper,2forscissors"))
print("you choose",choices[user_choice])
print( "computer choice",choices[computer_choice])

if(user_choice==0):
       if(computer_choice==1):
         print("lose")
       elif(computer_choice==2):
         print("winner")
       else:
         print("draw")
elif(user_choice==1):
       if(computer_choice==0):
         print("winer")
       elif(computer_choice==2):
         print("lose")
       else:
         print("draw")
elif(user_choice==2):
        if(computer_choice==1):
         print("winer")
        elif(computer_choice==0):
         print("lose")
        else:
         print("draw")
else:
    print("choice doesn't exist")
   