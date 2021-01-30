#           0      1        2        3         4
cars = ['mazda', 'bmv', 'shkoda', 'suzuki', 'audi']
for x in cars:
    print(x.upper())
for x in range(1, 6):
    print(x)

mynumber_list = list(range(0, 10))
print(mynumber_list)

print("________________________________________")
for x in mynumber_list:
    x = x * 2
    print(x)
mynumber_list.sort(reverse=True)
print(mynumber_list)
print("Максимальный номер = " + str(max(mynumber_list)))
print("Минимальный номер = " + str(min(mynumber_list)))
print("Сумма " + str(sum(mynumber_list)))

print("________________________________________")
#           0      1        2        3         4
cars = ['mazda', 'bmv', 'shkoda', 'suzuki', 'audi']
mycarc = cars[1:4]
print(mycarc)
mycarc = cars[:4]
print(mycarc)
mycarc = cars[-3:]
print(mycarc)
mycarc = cars[-3:-1]
print(mycarc)

# Клонировать массив
print("________________________________________")
#           0      1        2        3         4
cars = ['mazda', 'bmv', 'shkoda', 'suzuki', 'audi']
mycarc = cars[:]
