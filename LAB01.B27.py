# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:48:09 2024

@author: NGUYEN THANH HUY
"""

Hinh = input("Nhap vao hinh (hinh vuong), (hinh chu nhat), (hinh tron): ")
if Hinh == 'hinh vuong':
    canh = float(input("Nhap chieu dai canh: "))
    chu_vi = 4 * canh
    print("Ket qua chu vi hinh vuong la: ", chu_vi)
    dien_tich = canh ** 2
    print("Ket qua dien tich hinh vuong la: ", dien_tich)
elif Hinh == 'hinh chu nhat':
    rong = float(input("Nhap vao chieu rong: "))
    dai = float(input("Nhap vao chieu dai"))
    chu_vi = 2 * (rong + dai)
    print("Chu vi hinh chu nhat la: ", chu_vi)
    dien_tich = rong * dai
    print("Dien tich hinh chu nhat la: ", dien_tich)
elif Hinh == 'hinh tron':
    ban_kinh = float(input("Nhập bán kính: "))
    chu_vi = 2 * 3.14 * ban_kinh
    print("Ban kinh hinh tron la: ", ban_kinh)
    dien_tich = 3.14 * (ban_kinh ** 2)
    print("Dien tich hinh tron la: ", dien_tich)
else:
       print("Hinh khong hop le")