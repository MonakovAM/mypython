# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 21:44:22 2017

@author: Student
"""
mStr=input()
mStr=mStr.split()

with open('source-1.txt') as finpt:
    a = finpt.read()
b = a.format(*mStr)

with open('htmlGen-1.html', 'w') as fout:
    fout.write(b)

