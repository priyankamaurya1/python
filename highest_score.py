student_score= input("enter the scores of student in class").split()
# print(student_score)
hightest_score=0
for marks in student_score:
     marks=int(marks)
     if(marks>hightest_score):
          hightest_score=int(marks)

print(f"your highest  score is:", hightest_score)