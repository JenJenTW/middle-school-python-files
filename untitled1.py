# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 11:39:07 2020

@author: 捲捲
"""

import math

x = 1235

xhaha = x /10
xnew = math.floor(xhaha)
y = x - xnew*10
print(xnew)
print(y)
z = [2, 4, 6 ,8 ,0]
if y in z:
    print("yeah,我是偶數")
else:
    print("yeah,我是奇數")