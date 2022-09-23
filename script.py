from googletrans import Translator
import time, os, shutil
from art import *

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)

def getPathFile():
    allFiles = next(os.walk("./"), (None, None, []))[2]
    q = 0
    temp = []
    for poFiles in allFiles:
        if ".po" in poFiles:
            q += 1
            temp.append(poFiles)
            print(str(q) + ". " + poFiles + "")
            
    selectFile = input("\nChoose File: ")
    usersFile = temp[int(selectFile) - 1]
    return usersFile

def engine(usersFile):
    translator = Translator()
    counter = 0
    if os.path.exists('tr_TR.po'):
        os.remove('tr_TR.po')
    shutil.copyfile(usersFile, "tr_TR.po")
    with open('tr_TR.po', 'r+', encoding='utf-8') as poFile:
        file = poFile.readlines()
        for i in range(len(file)):
            if "msgid" in file[i]:
                nonTranslated = file[i].split('"',1)[1].replace('"', '').replace("\n", "")
                if "msgstr" in file[i+1]:
                    file.pop(i+1)
                    translated = translator.translate(nonTranslated, dest='tr')
                    file.insert(i+1, ('msgstr "' + str(translated.text) + '"\n'))
                    printProgressBar(i/len(file),1,prefix="Progress:", suffix="Complete", length=50)
        poFile.truncate(0)
        poFile.seek(0)
        poFile.writelines(file)
        print("\n\nComplete.")

tprint("HEKIR's  SIMPLE  TOOLS")
engine(getPathFile())



