# watch on terminal
from datetime import *
from clint.textui import *
from clint.textui.colored import *
import sys
import os
import os.path

def Isfile(f):
    if os.path.isfile(f):
        return 1
    return -1
def Am(h):
    if h > 12:
        return h - 12
    return h
def Weekdays(n):
    list = ['월', '화', '수', '목', '금', '토', '일']
    return list[n]
def LeapYear(y):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return 1
    return -1
def Time_12():
    print(colored.cyan("%s요일"%(Weekdays(datetime.now().today().weekday()))))
    print(colored.blue("%s시 %s분 %s초"%(\
    Am(datetime.now().hour), datetime.now().minute, datetime.now().second)))
    print(colored.green("%s년"%datetime.now().year), colored.magenta("%s월"%datetime.now().month), colored.magenta("%s일"%datetime.now().day))
def Print():
    print(colored.yellow("시계"))
    Time_12()
def NowDir():
    return os.path.dirname(os.path.abspath(__file__))
def ManVer():
    now = NowDir()
    ver_file = now + "/doc/version.md"
    isfile = Isfile(ver_file)
    if isfile == -1:
        print("Error: No version.md file")
        return -1
    file = open(ver_file, "rb")
    load = file.read()
    file.close()
    print(colored.green(load.decode(encoding="utf-8")[:5]) + ' ' + load.decode(encoding="utf-8")[6:]) # Prints
def ManHelp():
    ManVer()
    now = NowDir()
    help_file = now + "/doc/help.md"
    isfile = Isfile(help_file)
    if isfile == -1:
        print("Error: No help.md file")
        return -1
    file = open(help_file, "rb")
    load = file.read()
    file.close()
    print(load.decode(encoding="utf-8"))
def Flags(f):
    for i in range(1, 3):
        if i == 1:
            f = f.lower()
        if i == 2:
            f = f.upper()
        if (f.find('-h')==0 or f.find('--h')==0):
            ManHelp()
            sys.exit(0)
        if (f.find('-v')==0 or f.find('--v')==0):
            ManVer()
            sys.exit(0)
try:
    Flags(sys.argv[1])
except IndexError:
    Print()