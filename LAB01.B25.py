# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 14:13:32 2024

@author: NGUYEN THANH HUY
"""

a = input("Nhập một chữ cái ngẫu nhiên: ")

if a.islower():
    print("Chữ hoa:", a.upper())
elif a.isupper():
    print("Chữ thường:", a.lower())
else: 
    print("Không phải là chữu cái")
