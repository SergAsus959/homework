a = 1
b = 1
c = input("Введите число: ")
c = int(c)
i = 0
while i < c - 2:
    a_b = a + b
    a = b
    b = a_b
    i = i + 1
    print("Ответ:", b)