from calculator_art import logo

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return('No se puede dividir entre cero 0')
    else:
        return n1 / n2

def calculator():
    print(logo)
    operations = {
        '+' : add,
        '-' : substract,
        '*' : multiply,
        '/' : divide
    }
    n1 = float(input('Type Num 1: '))
    for operator in operations:
        print(operator)
    select = False
    while not select:
        option = input('Select an option from the line above: ')
        n2 = float(input('Type Next Num: '))
        calc = operations[option]
        result = calc(n1,n2)
        print(f'{n1} {option} {n2} = {result}')
        if input(f'Type "y" to continue calculating with {result}, or type "n" to exit: ') == 'n':
            select = True
        else:
            n1 = result
            calculator()
calculator()
