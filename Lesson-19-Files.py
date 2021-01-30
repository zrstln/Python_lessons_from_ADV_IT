inputfile = "../почта acl.txt"
outputfile = "../output.txt"

words_find = "!Общие документы"

myfile1 = open(inputfile, mode='r', encoding='cp1251')
# myfile2 = open(outputfile, mode='w', encoding='cp1251')
myfile2 = open(outputfile, mode='a', encoding='cp1251')

# print(myfile.read())
# for line in myfile:
#     print("Hello " + line.strip())
for num, line in enumerate(myfile1, 1):
    if words_find in line:
        print("Line №: " + str(num) + " : " + line.rstrip())
        myfile2.write("Found words " + line.lstrip())

myfile1.close()
myfile2.close()
