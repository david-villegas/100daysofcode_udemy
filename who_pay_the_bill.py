import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
choice = random.randint(0, len(names)-1)
bill = names[choice]
print(f'{bill} is going to buy the meal today!')
print(bill[::-1])
#print(pay_bill)
#print(len(names))

