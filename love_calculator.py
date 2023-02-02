# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
full_name = name1 + name2
lower_full_name = full_name.lower()
t = lower_full_name.count('t')
r = lower_full_name.count('r')
u = lower_full_name.count('u')
e1 = lower_full_name.count('e')
l = lower_full_name.count('l')
o = lower_full_name.count('o')
v = lower_full_name.count('v')
e2 = lower_full_name.count('e')

true_var = t + r + u + e1
love_var = l + o + v + e2
true_love = int(str(true_var)+str(love_var))

if true_love < 10 or true_love > 90:
    print(f'Your score is {true_love}, you go together like coke and mentos.')
elif true_love >= 40 and true_love <= 50:
    print(f'Your score is {true_love}, you are alright together.')
else:
    print(f'Your score is {true_love}.')
