# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:16:43 2024

@author: NGUYEN THANH HUY
"""

ngay=int(input("Ngày sinh:"))
thang=int(input("Tháng sinh:"))
nam=int(input("Năm sinh:"))
#NgàyThangNam
print("ngày tháng năm:", f"{ngay}/{thang}/{nam}")
#NgàyThangNam ( chỉ lấy 2 số cuối của năm)
namsau= nam % 100
print("ngày tháng (năm lấy 2 số cuối ):", f"({ngay}/{thang}/{namsau})")
# đổi vị trí năm ngày
print(" Đổi vị trí Ngày, năm :", f"{nam}/{thang}/{ngay}")
#ngược lại
nhapngay = int(input("Nhập ngày:"))
nhapthang = int(input("Nhập tháng:"))
nhapnam = int(input("Nhập năm:"))
print(f"Ngày sinh là: {nhapngay}/{nhapthang}/{nhapnam}")
