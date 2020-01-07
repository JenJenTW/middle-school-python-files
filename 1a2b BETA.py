# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 13:45:46 2020

@author: 捲捲
"""
from random import randrange
gueestime = 0
numberrepeat = 0
stop =0
def compare(guess,answer):
    a = 0
    b = 0
    for compartime in range(4):
        if (answer[compartime] == guess[compartime]):
            a += 1
        else:
            if (answer[compartime] == guess[0]):
                b += 1
            if (answer[compartime] == guess[1]):
                b += 1
            if (answer[compartime] == guess[2]):
                b += 1
            if (answer[compartime] == guess[3]):
                b += 1
    return a,b
def repeat(numberinput):
    repeattrue = 0
    for repeatnumber in range(4):
        for repeat2 in range(4):
            if repeatnumber !=	repeat2:
                if(numberinput[repeatnumber] == numberinput[repeat2]):
                    repeattrue +=1
    return repeattrue
#number is already string don't change it
while numberrepeat == 0:        
    number1 = randrange(9999)
    number = str(number1).zfill(4)
    repeatyes = repeat(number.zfill(4))
    if repeatyes == 0:
        numberrepeat = 1
        
        
        
        
        
        
while stop == 0:
    x = str(input("請輸入你猜的數字(不準給我打重複的): "))
    AB = compare(str(x).zfill(4),number.zfill(4))
    print(str(AB[0]) + 'A' + str(AB[1]) + 'B')
    gueestime += 1
    if AB[0] == 4:
        print("你猜對了,正確答案是" + str(number))
        print("你總共花了" + str(gueestime+1) + "次答對")
        stop = 1