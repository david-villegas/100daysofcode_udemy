# print('Welcome to de tip calculator.')
# bill = float(input('What was the total bill? $'))
# tip = int(input('What percentage tip would you like to give? 10, 12 or 15? '))
# people = int(input('How many people to split the bill? '))

# total = ((bill * (tip / 100 + 1)) / people)
# print(f'Each person should pay: ${round(total, 2)}')

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / height**2)

if bmi <= 18.5:
    print(f'Your BMI is {bmi}, you are underweight.')
elif bmi <= 25:
    print(f'Your BMI is {bmi}, you have a normal weight.')
elif bmi <= 30:
    print(f'Your BMI is {bmi}, you are slightly overweight.')
elif bmi <= 35:
    print(f'Your BMI is {bmi}, you are obese.')
else:
    print(f'Your BMI is {round(bmi)}, you are clinically obese.')
