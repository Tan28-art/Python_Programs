# program to calculate BMI
w = float(input("Enter weight here(in Kg):"))
h = float(input("Enter height here (in m):"))
bmi = w / (h ** 2)
print("Your BMI is:", bmi)
if bmi < 18.5:
    print("You are underweight")
elif 18.5 <= bmi < 24.9:
    print("You are normal")
elif 25 <= bmi < 29.9:
    print("You are overweight")
elif 30 <= bmi:
    print("You are obese")
