height=float(input("enter your height in m"))
weight =float(input("enter your weight"))
bmi =(weight/height**2)
bmi_as_round=int(bmi)
print(bmi_as_round)
if(bmi_as_round< 16):
    print("Severe Thinness")
elif(bmi_as_round<17):
    print("Moderate Thinness")
elif(bmi_as_round<18.5 ):
    print("Mild Thinness")
elif(bmi_as_round< 25):
    print("Normal")
elif(bmi_as_round<30):
    print("Overweight")
elif(bmi_as_round<35):
    print("Obese Class I")
elif(bmi_as_round<40 ):
     print("Obese Class II	")
else:
    print("Obese Class III")