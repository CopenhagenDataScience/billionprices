import os
file = open("python_scripts.txt")

read = file.read().splitlines()

for i in read:
    string = "python " + i
    os.system(string)
