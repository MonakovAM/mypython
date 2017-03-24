# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 10:06:15 2017

@author: Student
"""
from string import Template
mStr=input()
mStr=mStr.split()

with open('source-2.txt') as finpt:
    a = finpt.read()
b = Template(a)
c=b.substitute(title=mStr[0], text1 = mStr[1], text2=mStr[2], text3 = mStr[3])


with open('htmlGen-2.html', 'w') as fout:
    fout.write(c)

