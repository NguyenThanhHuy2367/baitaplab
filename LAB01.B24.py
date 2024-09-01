# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 13:09:32 2024

@author: NGUYEN THANH HUY
"""

h = int(input("Nhập số giờ: "))
m = int(input("Nhập số phút: "))
s = int(input("Nhập số giây: "))
if h < 0 or h >23:
    print("Giờ không hợp lệ!")
elif m < 0 or m > 59 :
    print("Phút không hợp lệ!")
elif s < 0 or s > 59:
    print("Giây không hợp lệ!")
else:
    print("Giờ,phút và giây đều hợp lệ!")