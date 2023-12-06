def show_dashboard():
    dashboard = "Calculator:\n '+':addition \n '-':substraction \n '*':multiplication \n '/':division \n '0':close"
    print(dashboard)
    action = input("enter your desired action: ")


def addition(n1, n2):
    print(n1 + n2)


def subtraction(n1, n2):
    print(n1 - n2)


def multiplication(n1, n2):
    print(n1 * n2)


def division(n1, n2):
    print(n1 / n2)


show_dashboard()
