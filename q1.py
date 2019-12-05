# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:35:03 2019

@author: User
"""

from collections import Counter

name='words.txt'
with open(name) as f:
    a=f.read()
s=a.split()
count=Counter(s)
c=list(count.values())
Q1=open("Q1.txt",'w+')
for i,j in enumerate(count):
    print(j,i,c[i],file=Q1)
Q1.close()