# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 14:18:11 2024

@author: NGUYEN THANH HUY
"""

a=int(input("nhập hệ số a: "))
b=int(input("nhập hệ số b: "))
c=int(input("nhập hệ số c: "))
if a>b:
    a,b= b,a
if a>c:
    a,c=c,a
if b>c:
    b,c=c,b
    print(f"Các số theo thứ tự tăng dần:{a},{b},{c}")