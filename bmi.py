weight = float(input("Enter Weight in Kg: "))
height = float(input("Enter Height in Meters: "))
bmi = weight/(height**2)
print("Your BMI: ",bmi)
if bmi<18.5:
    print("Category : Underweight")
elif bmi>=18.5 and bmi<=24.9:
    print("Category : Normal")
else:
    print("Category : Overweight")