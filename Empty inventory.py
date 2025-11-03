# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:20:13 2024

@author: Miko
"""
#Initialization of Variables:
header = []

#Creating an empty inventory:
header.append(f"{'Prod:':>10},{'Qty:':>10},{'Prc:':>10},{'Total:':>10}")
with open('EMPTY_INVENTORY.csv', 'a') as fhand:
    for line in header:
        fhand.write(line+',''\n')
        