student_height= input("enter your height ").split()
# print(student_height) 

total_len=0
for len in student_height:
    total_len+=1
# print(total_len)

total_height=0
for sum in student_height:
    total_height += int(sum)
# print(total_height)

average_height=round(total_height/total_len)
print(average_height)