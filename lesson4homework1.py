def check(a, b = None):
    if b is None:
        b = a - 1
    while b >= 2:
        if a % b == 0:
            print("Число составное")
            return False
        else:
            return check(a, b-1)
    else:
        print("Число простое")
        return True
a = int(input("Введите число: "))
check(a)