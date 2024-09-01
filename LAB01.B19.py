# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 13:22:35 2024

@author: NGUYEN THANH HUY
"""

a = int(input("Nhap vao so a: "))
b = int(input("Nhap vao so b: "))
c = int(input("Nhap vao so c: "))
d = int(input("Nhap vao so d: "))
if a< b and a< c and a<d:
    sobenhat=a
elif b<a and b<c and b<d:
    sobenhat=b
elif c<a and c<b and c<d:
    sobenhat=c
elif d<a and d<b and d<c:
    sobenhat=d
    print("Số bé nhất:", sobenhat)