def add ():
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    return a+b
def sub ():
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    return a-b
def multiply ():
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    return a*b
def division ():
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    try:
        print(a/b)
    except ZeroDivisionError:
        print("division by zero is not allowed")
def rem ():
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    return a%b
def fdivision ():
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    try:
        print(a//b)
    except ZeroDivisionError:
        print("division by zero is not allowed")
def exponent ():
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    return a**b
def sqroot ():
    a=int(input("enter a:"))
    return a**0.5
def max ():
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    if a>b:
        print(f"{a} is maximum")
    else:
        print(f"{b} is maximum")
def min ():
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    if a<b:
        print(f"{a} is minimum")
    else:
        print(f"{b} is minimum")

print("---------the operations available in calculator:----------" )
print('''       
                1.Addition
                2.subtraction
                3.multiplication
                4.division
                5.floor division
                6.modulus
                7.square root
                8.max
                9.min
                10.exponent     ''')
n=int(input("enter the choice number(1-10):"))
if(n<=10):
    if n==1:
        print("the addition is:",add())
    elif n==2:
        print("the subtraction is:",sub())
    elif n==3:
        print("the multiplication is:",multiply())
    elif n==4:
        division()
    elif n==5:
        fdivision()
    elif n==6:
        print("the reminder is:",rem())
    elif n==7:
        print(f"the square root is:",sqroot())
    elif n==8:
        max()
    elif n==9:
        min()
    else:
        exponent()
else:
    print("invalid choice")
    