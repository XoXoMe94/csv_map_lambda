# -*- coding: utf-8 -*-
"""


@author: sara
"""

import csv 

with open(r'C:\Users\sara\Desktop\office 2021\data.csv') as csvfile:
    data=list(csv.DictReader(csvfile))
data[:3] 
len(data) 
print(data[0].keys()) #show column




#ex map() 

def double(a):
    return a*2  #تابع دوبرابر کردن

x=[1,2,3]  #a list
y=list(map(double, x))  #we cant see map cause it is object, we use list
                        #map تابع را روی لیست نگاشت کن
print(y)  #[2, 4, 6]



#ex lambda
g=lambda a:a*5  #input:fuction on input
print(g(4)) #20

g=lambda a,b:a*b
print(g(100,2)) #200



#ex map and lambda
x=[1,2,3]
y=list(map(lambda a:a*2, x))
print(y)  #[2, 4, 6]







