#Prime numbers
#Write your code below this line 👇
def prime_checker(number):
    contador = 0
    for n in range(1, number + 1):
        if number % n == 0:
            contador += 1
    if contador > 2:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


'''
Otra manera fácil:

def prime_checker(number):
    is_prime = True
    for n in range(2, number):
        if number % n == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
'''
