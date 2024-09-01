# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 13:54:03 2024

@author: NGUYEN THANH HUY
"""

print("Giả và biện luận phương trình")
a=float(input("Hệ số a= "))
b=float(input("Hệ số b= "))
if a!=0:
    x= -b/a
    print("x=%.3f"%x)
elif b!=0:
    print("Phương trình vô nghiệm ")
else:
    print("Phương trình vô số nghiệm ")