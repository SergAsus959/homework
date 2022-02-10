while True:
    a = (input('Number A = '))
    if a.isdigit():
        a = float(a)
    else:
        print("Enter the number!")
        continue
    sign = input("Press(+, -, *, /) ")

    b = (input('Number B = '))
    if b.isdigit():
        b = float(b)
    else:
        print("Enter the number!")
        continue
    if sign == '+':
        print(('Answer'),(a + b))
    elif sign == '-':
        print(('Answer'),(a - b))
    elif sign == '*':
        print(('Answer'),(a * b))
    elif sign == '/':
        if b != 0:
            print(('Answer'), (a / b))
        else:
            print('Division by zero')
            break

