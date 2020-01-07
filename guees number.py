# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 13:45:46 2020

@author: 捲捲
"""
from random import randrange
gueestime = 0
number = randrange(1000)
time = 0
while stop < 10:
    x = int(input("Please enter the number you guees: "))
    if x < number:
        print("太小了喔")
        gueestime += 1
    elif x == number:
        print("你答對了YEAH!!")
        print("你總共花了" + str(gueestime+1) + "就答對了ㄟ")
        stop = 100
    else:
        print("太大了喔")
        gueestime += 1
        