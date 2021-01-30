import sys
filename = "../output.txt1"

# попробуем выполнить myfile = open(filename, mode='r', encoding='cp-1251'), если есть ошибка переход к блоку
# except Exception: иначе, если ошибки нет, то переход к блоку else:

while True:
    try:
        print("Inside TRY")
        myfile = open(filename, mode='r', encoding='cp1251')
    except Exception:
        print("Inside Except")
        print("Error Found")
        print(sys.exc_info()[1])
        filename = input("!!!Input correct file name: ")
    else:
        print("Inside Else")
        print(myfile.read())
        sys.exit()

print("===========================EOF=====================")
