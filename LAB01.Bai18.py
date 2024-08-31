# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:40:40 2024

@author: NGUYEN THANH HUY
"""

h1=int(input("Giờ 1:"))
h2=int(input("Giờ 2:"))
p1=int(input("Phút 1:"))
p2=int(input("Phút 2:"))
s1=int(input("Giây 1:"))
s2=int(input("Giây 2:"))
hCongh= h1 + h2
htruh= h1-h2
PcongP=p1+p2
PtruP=p1-p2
ScongS=s1+s2
StruS=s1-s2
print(f"Kết quả cộng: Giờ {hCongh}, Phút {PcongP}, Giây {ScongS}")
print(f"Kết quả trừ : Giờ {hCongh}, Phút {PcongP}, Giây {ScongS}")