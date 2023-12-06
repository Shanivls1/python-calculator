def show_dashboard():
    print("Calculator:\n\t'+':addition \n\t'-':subtraction \n\t'*':multiplication \n\t'/':division \n\t'0':close")
    operation = input("enter your desired action: ")
    if operation == '0':
        print("exiting calculator...\n")
        return 0
    if not operation == '+' and not operation == '-' and not operation == '*' and not operation == '/':
        print("undefined operation!\n")
        return 1
    n1, n2 = input("enter first number:"), input("enter second number:")
    if not n1.isdigit() or not n2.isdigit():
        print("only numbers are allowed!\n")
        return 1
    if operation == '+':
        addition(int(n1), int(n2))
    elif operation == '-':
        subtraction(int(n1), int(n2))
    elif operation == '*':
        multiplication(int(n1), int(n2))
    elif operation == '/':
        division(int(n1), int(n2))
    return 1


def addition(n1, n2):
    print(n1 + n2)


def subtraction(n1, n2):
    print(n1 - n2)


def multiplication(n1, n2):
    print(n1 * n2)


def division(n1, n2):
    print(n1 / n2)


run = show_dashboard()
while run:
    run = show_dashboard()
