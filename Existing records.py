# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 19:15:33 2024

@author: Miko
"""
#Initialization of variables:
count = 0
line_1 = []
line_2 = []
student_records = {'Caliba':['Benedict','1DSA2',98,99,90],
         'Veloso':['Enrico','1DSA2',96,92,89],
         'Sy':['Eibert','1DSA2',89,94,93],
         'Vergara':['Dennis','1DSA2',99,92,90],
         'Yutuc':['Thom','1DSA2',99,99,99],
         'Dela Cruz':['Juan','1DSA2',89,88,87],
         'Manoloto':['Pepito','1DSA2',99,100,100],
         'Martin':['Coco','1DSA2',88,85,86,86.3],
         'Duterte':['Sarah','1DSA2',88,80,75],
         'Vasco':['Erika','1DSA2',98,99,90]}

#Blocks of code creating 10 existing sorted student records:
line_1.append((f"{'No.':>10},{'LN:':>10},{'FN:':>10},{'Sec:':>10},{'Q1:':>10},\
{'Q2:':>10},{'Q3:':>10},{'AVE:':>10}"))
for record in student_records:
    count=count+1
    line_1.append(str(count)+", "+record+", "+student_records[record][0]+", "+\
student_records[record][1]+", "+str(student_records[record][2])+", "+\
str(student_records[record][3])+", "+str(student_records[record][4])+", "+\
str((student_records[record][2]+student_records[record][3]+student_records[record][4])/3))
sort_lastname = sorted(line_1[1:], key=lambda x: x.split(', ')[1])
line_1[1:] = [f"{idx + 1}, {', '.join(record.split(', ')[1:])}" for idx, record in enumerate(sort_lastname)]

#Creation of csv file where the records are stored in:
with open('STUDENTS_RECORDS.csv','a') as fhand:
    for line_a in line_1:
        fhand.write(line_a+',''\n')
    for line_b in line_2:
        fhand.write(line_b+'\n')
        