def show_dashboard():
    print("Calculator:\n\t'+':addition \n\t'-':subtraction \n\t'*':multiplication \n\t'/':division \n\t'0':close")
    operation = input("enter your desired action: ")
    # exit application
    if operation == '0':
        return 0
    # check if operation is undefined
    if not operation == '+' and not operation == '-' and not operation == '*' and not operation == '/':
        print("undefined operation!\n")
        return 1
    # input the two numbers
    n1, n2 = input("enter first number:"), input("enter second number:")
    # check if the inputs are numbers
    if not is_float(n1) or not is_float(n2):
        print("only numbers are allowed!\n")
        return 1
    # find operation
    if operation == '+':
        addition(float(n1), float(n2))
    elif operation == '-':
        subtraction(float(n1), float(n2))
    elif operation == '*':
        multiplication(float(n1), float(n2))
    elif operation == '/':
        division(float(n1), float(n2))
    return 1


def addition(n1, n2):
    print(n1 + n2)


def subtraction(n1, n2):
    print(n1 - n2)


def multiplication(n1, n2):
    print(n1 * n2)


def division(n1, n2):
    print(n1 / n2)


def is_float(s):
    if s[0] == '-':
        s = s[1:]
    return s.replace(".", "").isnumeric()


# run contains 1 if continue and 0 if we need to exit the app
run = show_dashboard()
while run:
    run = show_dashboard()
print("closing the calculator...")
