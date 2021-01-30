x = 25
if x == 27:
    print("Да, все верно")
else:
    print("Нет не верно")
print("---------------------------")
age = 25
if age <= 4:
    print("You are baby")
elif (age > 4) and age < 12:
    print("You are kid")
elif (age > 12) and age < 19:
    print("You are teenager")
else:
    print("You are old")
print("----------END----------------")
all_cars = ['mazda', 'shevrole', 'lada', 'bmv', 'kraisler', 'honda']
japan_cars = ['mazda', 'honda']
for x in all_cars:
    if x in japan_cars:
        print(x + " is a Japan cars")
    else:
        print(x + " Is not a Japan cars")
