import sys
from os.path import exists


practiceList = []


if(len(sys.argv) == 1):
    print("Practicing \"advanced\" commands")
    with open("adv-commands.conf") as advFile:
        advList = advFile.readlines()
        advList = [line.rstrip() for line in advList]
    with open("EVERYTHING.words") as everyFile:
        everyList = everyFile.readlines()
        everyList = [line.rstrip() for line in everyList]
    for conf in advList:
        if("zx" in conf):
            for word in everyList:
                newLine = conf.replace("zx", word)
                practiceList.append(newLine)
        else:
            practiceList.append(conf)
elif(len(sys.argv) == 2):
    print("Practicing local "+sys.argv[1])
    if(exists(sys.argv[1])):
        with open(sys.argv[1]) as giveFile:
            practiceList = giveFile.readlines()
            practiceList = [line.rstrip() for line in practiceList]
    else:
        print("File \""+sys.argv[1]+"\" does not exist")
        sys.exit()
else:
    print("Too many arguments given")
    sys.exit()

print(practiceList)
