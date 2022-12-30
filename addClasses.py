import os

def addClasses():
    while True:
        className = input("What is the name of your class you want to add to the filter list? \n Type done when you have put in all your classes\n").lower()
        if className != "done":
            f = open("ClassList.txt", "a")
            f.write(className + "\n")
            f.close()
        else:
            createFolders()
            return False

def createFolders():
    f = open("ClassDirectory.txt", "r")
    classesDir = f.read()
    print(classesDir)
    f.close()
    f = open("ClassList.txt", "r")
    for item in f:
        newfolder = f"{classesDir}/{item.strip().title()}"
        print(newfolder)
        if not os.path.exists(newfolder):
            os.makedirs(newfolder)

addClasses()