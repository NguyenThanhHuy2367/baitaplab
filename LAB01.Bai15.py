# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:46:53 2024

@author: NGUYEN THANH HUY
"""

a=int(input("Nhập a:"))
b=int(input("Nhập b:"))
A=(((a+b) / ((a)**(1/3)+((b)**(1/3)))) - (a*b)**(1/3)) / ((((a**(1/3)) - (b**(1/3))))**2)
print("Kết quả:",A)