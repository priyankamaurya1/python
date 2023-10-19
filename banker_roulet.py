import random

names_of_member =input("give everybodys name separated by commas")
names =names_of_member.split(',')
names_len = len(names)
choice =random.randint(0,names_len-1)
who_pays=names[choice]


print(names)
print(names_len)
print(f"{who_pays},you pay the bill")