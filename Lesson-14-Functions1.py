def napechatat_privetstvie(name):
    """Печать приветствия"""
    print("Приветствую " + name + " ВАС!!!")
    print("Привет, привет, привет")


def summa(a, b):
    return a+b


def factorial(x):
    """Calculate Factorial of number X"""
    otvet = 1
    for i in range(1, x + 1):
        otvet = otvet * i
    return otvet


print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
napechatat_privetstvie("Vasya")
napechatat_privetstvie("Petya")
print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
x = summa(33, 22)
print(x)
print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

print(factorial(1))
print(factorial(5))

for i in range(1, 10+1):
    print((str(i)) + "!\t = " + str(factorial(i)))
