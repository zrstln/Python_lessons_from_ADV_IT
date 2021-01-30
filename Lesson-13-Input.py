# name = input("Ввести значение имени: ")
# print("Привет " + name)
# num1 = input("Enter x: ")
# num2 = input("Enter Y: ")
# summa = int(num1) + int(num2)
# print(summa)
# message = ""
# while True:
#     message = input("Enter password: ")
#     if message == 'secret':
#         break
#     print(message + " - password not correct")
# print("You password is: " + message)
mylist = []
msg = ''
while msg != 'stop':
    msg = input("Enter new item and stop for finish ")
    mylist.append(msg)
print(mylist)
