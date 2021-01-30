import sys
import os

x = len(sys.argv)

if x > 1:
    if sys.argv[1] == "/?":
        print("\nHelp requested\n")
        print("Usage of this program is: python.exe python.py argv1 argv2")
    print("\nArguments entered: " + str(sys.argv[1:]))
else:
    print("Arguments NOT PROVIDED")
os.system("dir > test.txt")
# os.mkdir("new dir")
