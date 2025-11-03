# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:56:56 2025

@author: Miko
"""
num1 = int(input("Enter a number:"))
y = 0
print(f"{'x':^15}|{'y':^14}")

while True:
    num1 += 0.2
    y = (3*num1**5) - (2*num1**3) + num1
    formatted_y = f"{y:.2f}"
    formatted_num1 = f"{num1:.2f}"
    print(f"{formatted_num1:^15}|{formatted_y:^14}")
    trya = (input("Do you want to continue [Y/N]:")).upper()
    if trya == "Y":
        print(f"{formatted_num1:^15}|{formatted_y:^14}")
        continue
    elif trya == "N":
        break
    