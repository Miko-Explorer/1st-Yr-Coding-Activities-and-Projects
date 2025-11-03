# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:24:49 2025

@author: Miko
"""
print("-"*34)
print(f"|{'Celcius to Farenheit':^32}|")
print("-"*34)
starting_celcius = int(input("Enter starting celcius:"))
print("-"*34)
counting_celcius = 0
print(f"|{'Celcius':^16}|{'Farenheit':^15}|")
print("-"*34)

while counting_celcius<=99:
    starting_celcius += 1
    counting_celcius = starting_celcius + 0
    farenheit = ((9/5) * counting_celcius) + 32
    formatted_farenheit = f"{farenheit:.2f}"
    print(f"|{counting_celcius:^15}C|{formatted_farenheit:^14}F|")
print("-"*34)
    
    
