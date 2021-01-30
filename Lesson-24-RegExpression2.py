# https://regex101.com конструктор регулярных выражений

import re

input_filename = "../emails.txt"
result_filename = "../result.txt"

inputfile = open(input_filename, mode='r', encoding='Latin-1')
resultfile = open(result_filename, mode='w', encoding='Latin-1')
mytext = inputfile.read()

# найти все адреса согласно выражению
# lockfor = r"[a-zA-Z-_.\d]+@\w+.\w+"

# исключить из поиска GOOGLE.COM
lockfor = r"[a-zA-Z-_.\d]+@(?!GOOGLE\.COM)+\d+.\w+.\w+"

results = re.findall(lockfor, mytext)

for item in results:
    print(item)
    resultfile.write(item + "\n")

print("Total: " + str(len(results)))
