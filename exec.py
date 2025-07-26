# watch on terminal
from datetime import *

# global variable
am_pm = 0
# functions
def Am(h):
    global am_pm
    if h > 12:
        am_pm = 1
        return h - 12 # 오후 1~11시까지
    if h == 0:
        am_pm = 0
        return 12 # 오전 12시 표현
    if h == 12:
        am_pm = 1
        return 12 # 오후 12시 표현
    am_pm = 0
    return h # 오전 1~11시까지
def Weekdays(n):
    list = ['월', '화', '수', '목', '금', '토', '일']
    return list[n]
def Time_12():
    global am_pm
    print("%s요일"%\
    (Weekdays(datetime.now().today().weekday())), "☁️")
    hour = Am(datetime.now().hour)
    if am_pm == 1:
        print('오후 ', end='')
    else:
        print('오전 ', end='')
    print("%s시 "% hour, "%s분" % datetime.now().minute, "%s초" % datetime.now().second)
    print("%s년" % datetime.now().year, "%s월" % datetime.now().month, "%s일" % datetime.now().day)
def Print():
    Time_12()

Print()