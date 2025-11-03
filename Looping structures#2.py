# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 09:54:39 2025

@author: Miko
"""
day1 = int(input("Enter day-1 temp in degrees celcius:"))
day2 = int(input("Enter day-2 temp in degrees celcius:"))
day3 = int(input("Enter day-3 temp in degrees celcuis:"))
day4 = int(input("Enter day-4 temp in degrees celcius:"))
day5 = int(input("Enter day-5 temp in degrees celcius:"))
day6 = int(input("Enter day-6 temp in degrees celcius:"))
day7 = int(input("Enter day-7 temp in degrees celcius:"))
print("\t")

list1 = []
list1.append(day1)
list1.append(day2)
list1.append(day3)
list1.append(day4)
list1.append(day5)
list1.append(day6)
list1.append(day7)

colddays = sum(1 for d in list1 if 0<d<=60)
print("*Number of cold days:", colddays)

pleasantdays = sum(1 for d in list1 if 60<=d<=84)
print("*Numeber of pleasant days:", pleasantdays)

hotddays = sum(1 for d in list1 if 85<=d<=100)
print("*Number of hot days:", hotddays)
print("\t")

dict1 = {}
dict1["Day-1"] = day1
dict1["Day-2"] = day2
dict1["Day-3"] = day3
dict1["Day-4"] = day4
dict1["Day-5"] = day5
dict1["Day-6"] = day6
dict1["Day-7"] = day7

print("*Days that are cold (0 to 60 degrees celcius):")
for k,v in dict1.items():
    if 0<v<=60:
        print("-",k)

print("\t")
print("*Days that are pleasant (60 to 84 degrees celcius):")
for k,v in dict1.items():
    if 60<=v<=84:
        print("-",k)

print("\t")
print("*Days that are hot (85 to 100 degrees celcius):")
for k,v in dict1.items():
    if 85<=v<=100:
        print("-",k)