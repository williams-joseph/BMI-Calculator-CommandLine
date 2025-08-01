"""BMI Calculator 2.0"""

print("Welcome To Body Mass Index(BMI) Calculator 2.0")
height = float(input("Enter your Height in m: \n"))
weight = float(input("Enter your Weight in kg: \n"))

bmi = float(round(weight / height ** 2, 2))

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you're underweight.")
elif 25 > bmi > 18.5:
    print(f"Your bmi is {bmi}, you have normal weight.")
elif  30 > bmi > 25:
    print(f"Your bmi is {bmi}, you're overweight.")
elif 35 > bmi > 30:
    print(f"Your bmi is {bmi}, you're obese.")
else:
    print(f"Your bmi is {bmi}, you're clinically obese.")
