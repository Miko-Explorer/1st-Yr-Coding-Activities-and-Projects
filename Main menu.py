# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 21:32:46 2024

@author: Miko
"""
#Layout of the main menu and its following options and user input:
print("-"*55)
print(f"{'MAIN MENU':^54}")
print("-"*55)
print("[1] Add Record")
print("[2] Search")
print("[3] Modify")
print("[4] Delete")
print("[5] Exit")
print("-"*55)
user_choice = int(input("*Enter number:"))
print("-"*55)

#Block of code if user enters a number based from the given options:
count = 10
line_1 = []
fhand = open('STUDENTS_RECORDS.csv', 'r')
for line in fhand:
    count = count + 1

#If the user chose option 1:
    if user_choice == 1:
        line_1.clear()
        first_n = input("*Enter first name:")
        last_n = input("*Enter last name:")
        sec = input("*Enter yout section:")
        quat_1 = int(input("*Enter quarter#1 grade:"))
        quat_2 = int(input("*Enter quarter#2 grade:"))
        quat_3 = int(input("*Enter quarter#3 grade:"))
        Average = (quat_1 + quat_2 + quat_3)/3
        print("*Average:", Average)
        new_record = {last_n:[first_n,sec,quat_1,quat_2,quat_3,Average]}
        for record in new_record:
            line_1.append(str(count)+", "+record+", "+new_record[record][0]+", "+new_record[record][1]+\
","+str(new_record[record][2])+", "+str(new_record[record][3])+", "+str(new_record[record][4])+\
", "+str(new_record[record][5]))
        with open('STUDENTS_RECORDS.csv','a') as fhand:
            for line in line_1:
                fhand.write(line+'\n')
        print("-"*55)
        add_new_record_again = input("*Would you like to add a record again[Y/N]:")
        print("-"*55)
        if add_new_record_again == "Y":
            continue
        elif add_new_record_again == "N":
            break

#If the user chose option 2:
    elif user_choice == 2:
        search = input("*Search:")
        with open('STUDENTS_RECORDS.csv', 'r') as fhand:
            found = False 
            for line in fhand:
                fields = line.strip().split(',')  
                for element in fields:  
                    if search in element.lower(): 
                        print(line.strip()) 
                        found = True
                        break  
                        if not found:
                            print(f"No records found for '{search}'.")
        print("-"*55)
        again = input("*Would you like to search for another user? [Y/N]: ").strip().lower()
        if again != 'y':
            print("-"*55)
            break

#If the user chose option
    elif user_choice == 3:
        search = input("*Enter the last name of the record to modify: ").strip()
        print("-"*55)
    records = [] 
    modified = False  
    with open('STUDENTS_RECORDS.csv', 'r') as fhand:
        for line in fhand:
            records.append(line.strip())
    for i, record in enumerate(records):
        fields = record.split(', ')
        if fields[1].lower() == search.lower():
            print(f"*Record found: {record}")
            print("-"*55)
            print("*Enter the new details for this record:")
            print("-"*55)
            first_n = input("*Enter new first name: ")
            last_n = input("*Enter new last name: ")
            sec = input("*Enter new section: ")
            quat_1 = int(input("*Enter new quarter#1 grade: "))
            quat_2 = int(input("*Enter new quarter#2 grade: "))
            quat_3 = int(input("*Enter new quarter#3 grade: "))
            Average = (quat_1 + quat_2 + quat_3) / 3
            print("*New Average:", Average)
            updated_record = f"{fields[0]}, {last_n}, {first_n}, {sec}, {quat_1}, {quat_2}, {quat_3}, {Average:.2f}"
            records[i] = updated_record
            modified = True
            print("*Record updated successfully!")
            print("-"*55)
            break
    if not modified:
        print(f"*No record found with the last name '{search}'.")
    with open('STUDENTS_RECORDS.csv', 'w') as fhand:
        for record in records:
            fhand.write(record + '\n')
    edit_again = input("*Would you like to edit another record? [Y/N]: ").strip().lower()
    print("-"*55)
    if edit_again != 'y': 
        break


        
    
    
    

    
    