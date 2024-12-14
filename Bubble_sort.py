# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 12:19:10 2024

@author: Asus
"""

with open("province.txt" , "r" , encoding="utf-8") as file:
    lines = file.readlines()


def BubbleSort(a_list):
    n = len(a_list)  # หาความยาวของลิสต์
    # ใช้ลูปสำหรับการไล่ตรวจสอบและเรียงลำดับ
    for k in range(1, n):  # ทำซ้ำ n-1 รอบ
        flag = 0
        for i in range(0, n - k):  # ไล่จาก 0 จนถึงตำแหน่งสุดท้ายที่ยังไม่เรียง
            if a_list[i] < a_list[i + 1]:  # ถ้าตัวปัจจุบันมากกว่าตัวถัดไป
                # สลับตำแหน่ง (swap)
                tmp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = tmp
                flag = 1
    # คืนค่าลิสต์ที่เรียงลำดับแล้ว (แต่ไม่จำเป็นหากแก้ไขลิสต์โดยตรง)
        if flag == 0:
            break
    return a_list  


if __name__ == '__main__':

    # สร้างลิสต์ต้นฉบับ

    print(f'"ลิสต์ก่อนเรียงลำดับ:"\n, {lines}\n\n\n')

    # เรียกใช้ฟังก์ชัน Bubble Sort
    BubbleSort(lines)
    print(f'"ลิสต์หลังเรียงลำดับ:"\n, {lines}')