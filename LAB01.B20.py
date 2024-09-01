# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 13:26:08 2024

@author: NGUYEN THANH HUY
"""

a=int(input("hệ số a:"))
b=int(input("hệ số b:"))
c=int(input("hệ số c:"))
if a>b and a>c:
    hesolonnhat=a
elif b>a and b>c:
    hesolonnhat=b
else:
    hesolonnhat=c
print("số lớn nhất:", hesolonnhat)
        