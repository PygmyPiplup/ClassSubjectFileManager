import os
import shutil
import tkinter as tk
from tkinter import filedialog as fd


currentDir = os.getcwd()
classesDir = ""
startingDir = ""
filesInDir = os.listdir(currentDir)
isFirstRun = True
root = tk.Tk()
root.withdraw()


def createFiles(_firstRun):
    if _firstRun == True:
        classesDirectory = open("ClassDirectory.txt", "w")
        classesDirectory.write(fd.askdirectory(title="Where do you want the class folders?"))
        classesDirectory.close()

        startingDirectory = open("StartingDirectory.txt", "w")
        startingDirectory.write(fd.askdirectory(title="Where are the files orginating?"))
        startingDirectory.close()
        addClasses()

def addClasses():
    while True:
        className = input("What is the name of your class? \n Type done when you have put in all your classes\n").lower()
        if className != "done":
            f = open("ClassList.txt", "a")
            f.write(className + "\n")
            f.close()
        else:
            createFolders()
            return False

def createFolders():
    f = open("ClassList.txt", "r")
    for item in f:
        newfolder = f"{classesDir}/{item.strip().title()}"
        if not os.path.exists(newfolder):
            os.makedirs(newfolder)
            print(f"Made new folder {newfolder}")


def manipulateFiles():
    files = os.listdir(startingDir)
    f = open("ClassList.txt", "r")
    for subject in f:
        for file in files:
            lowerfile = file.lower()
            if lowerfile.find(subject.lower().strip()) != -1:
                shutil.move(f"{startingDir}/{file}", f"{classesDir}/{subject.title().strip()}/")


for file in filesInDir:
    if file == "ClassDirectory.txt":
        f = open("ClassDirectory.txt", "r")
        classesDir = f.read()
        f.close()
        sd = open("StartingDirectory.txt", "r")
        startingDir = sd.read()
        sd.close
        isFirstRun = False
        manipulateFiles()
    else:
        createFiles(isFirstRun)

