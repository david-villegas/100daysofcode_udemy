# Calcular año biciesto
# Primera condición = Debe ser divisible entre 4
# Segunda condición = No debe ser divisible entre 4
# Tercera condición = Debe ser divisible entre 4

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print('Leap year.')
    else:
        print('Not leap year.')
else:
    print('Not leap year.')
