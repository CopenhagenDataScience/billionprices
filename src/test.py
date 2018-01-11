import datetime, os
now = datetime.datetime.now()

if( not os.path.exists("output")):
    os.mkdir("output")

if (not os.path.exists("output/test.txt")):
    string = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
    with open("output/test.txt", "w") as myfile:
        myfile.write(string)
else:
    string = "\n" + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
    with open("output/test.txt", "a") as myfile:
        myfile.write(string)
