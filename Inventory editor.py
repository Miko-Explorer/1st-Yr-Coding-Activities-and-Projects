# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:55:58 2024

@author: Miko
"""
#Main menu for inventory editing:
print("-" * 50)
print(f"{'(PRODUCT INVENTORY)':^50}")
print("-" * 50)
print(f"{'INVENTORY EDITING OPTIONS':^50}")
print("-" * 50)
print("[A] Add Products")
print("[B] Remove Products")
print("[C] Update Product Quantity")
print("[D] Display Inventory")
print("-" * 50)

#Block of code for each options that relies on user input:
user_input = input("*Enter letter of option: ")
inventory_record = []

def Add_product():
    while True:
        try:
            with open('EMPTY_INVENTORY.csv', 'r') as fhand:
                inventory_record[:] = fhand.read().splitlines() 
        except FileNotFoundError:
            inventory_record.clear()  
        prod_name = input("*Enter product name: ")
        prod_qty = int(input("*Enter product quantity: "))
        prod_prc = float(input("*Enter product price: "))
        prod_total = prod_qty * prod_prc
        print("*Total amount:", prod_total)
        add_record = {prod_name: [prod_qty, prod_prc, prod_total]}
        for item in add_record:
            inventory_record.append(item + ", " + str(add_record[item][0]) + ", " + 
                                    str(add_record[item][1]) + ", " + 
                                    str(add_record[item][2]))
        inventory_record.sort()
        with open('EMPTY_INVENTORY.csv', 'w') as fhand:  
            for line in inventory_record:
                fhand.write(line + '\n')
        print("-" * 50)
        add_another_record = input("*Would you like to add another record [Y/N]: ").capitalize()
        print("-" * 50)
        if add_another_record != "Y":
            break

def Remove_product():
    while True:
      try:
          with open('EMPTY_INVENTORY.csv', 'r') as fhand:
              inventory_record[:] = fhand.read().splitlines()  
      except FileNotFoundError:
          inventory_record.clear() 
      if not inventory_record:
          print("*No records found to remove.")
          break
      print("-" *50)
      print("*Current Inventory:")
      print("-" *50)
      for i, record in enumerate(inventory_record, 0):
          print(f"{i}. {record}")
      try:
          print("-" *50)
          product_to_remove = int(input("*Enter number of the product to remove (enter 0 if none): "))
          print("-" *50)
          if product_to_remove == 0:
              break
          if 1 <= product_to_remove <= len(inventory_record):
              removed_item = inventory_record.pop(product_to_remove - 0)
              print(f"*Removed product: {removed_item}")
              with open('EMPTY_INVENTORY.csv', 'w') as fhand:
                  for line in inventory_record:
                      fhand.write(line + '\n')              
              print("-" * 50)
          else:
              print("*Invalid choice, please try again.")
      except ValueError:
          print("*Invalid input. Please enter a number.")
      another_removal = input("*Would you like to remove another product [Y/N]: ").capitalize()
      print("-" * 50)
      if another_removal != "Y":
          break
   
def Update_quantity():
    while True:
       try:
           with open('EMPTY_INVENTORY.csv', 'r') as fhand:
               inventory_record[:] = fhand.read().splitlines()
       except FileNotFoundError:
           inventory_record.clear()
       if not inventory_record:
           print("*No records found to update.")
           break
       print("-" * 50)
       print("*Current Inventory:")
       print("-" * 50)
       for i, record in enumerate(inventory_record, 0):
           print(f"{i}. {record}")
       try:
           print("-" * 50)
           product_to_update = int(input("*Enter the number of the product to update quantity (enter 0 if none): "))
           print("-" * 50)
           if product_to_update == 0:
               break
           if 1 <= product_to_update <= len(inventory_record):
               selected_record = inventory_record[product_to_update - 0]
               details = selected_record.split(", ")
               prod_name = details[0]
               prod_qty = int(details[1])
               prod_prc = float(details[2])
               print(f"*Current quantity of {prod_name}: {prod_qty}")
               print("-" * 50)
               new_qty = int(input(f"*Enter new quantity for {prod_name}: "))
               print("-" * 50)
               new_total = new_qty * prod_prc
               updated_record = f"{prod_name}, {new_qty}, {prod_prc}, {new_total}"
               inventory_record[product_to_update - 1] = updated_record
               with open('EMPTY_INVENTORY.csv', 'w') as fhand:
                   for line in inventory_record:
                       fhand.write(line + '\n')               
               print(f"*Updated {prod_name}: {updated_record}")
               print("-" * 50)
           else:
               print("*Invalid choice, please try again.")
       except ValueError:
           print("*Invalid input. Please enter a number.")
       another_update = input("*Would you like to update another product [Y/N]: ").capitalize()
       print("-" * 50)
       if another_update != "Y":
           break

def Display_inventory():
    try:
        with open('EMPTY_INVENTORY.csv', 'r') as fhand:
            inventory_record[:] = fhand.read().splitlines()
    except FileNotFoundError:
        inventory_record.clear()
    if not inventory_record:
        print("*No records found in the inventory.")
        return
    print("-" * 50)
    print("*Current Inventory:")
    print("-" * 50)
    for record in inventory_record:
        print(record)
        print("-" * 50)
        
if user_input == "A":
    Add_product()

elif user_input == "B":
    Remove_product()

elif user_input == "C":
    Update_quantity()
    
elif user_input == "D":
    Display_inventory()
    
   
        
        
   


