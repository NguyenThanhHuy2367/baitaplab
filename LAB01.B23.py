# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:00:38 2024

@author: NGUYEN THANH HUY
"""

import math

print("Giải phương trình bậc hai")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
delta = b**2 - 4 * a * c
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có nghiệm kép x1 = x2 = ", -(b / (2 * a)) )
else:
    print("Phương trình có hai nghiệm phân biệt:")
    print("x1 = ", (-(b) + math.sqrt(delta))/(2*a) )
    print("x2 = ", (-(b) - math.sqrt(delta))/(2*a) )