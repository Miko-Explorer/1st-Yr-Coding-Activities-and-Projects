#Assigning of variable names for the months of 2024:
month_1 = "(JANUARY 2024)"
month_2 = "(FEBUARY 2024)"
month_3 = "(MARCH 2024)"
month_4 = "(APRIL 2024)"
month_5 = "(MAY 2024)"
month_6 = "(JUNE 2024)"
month_7 = "(JULY 2024)"
month_8 = "(AUGUST 2024)"
month_9 = "(SEPTEMBER 2024)"
month_10 = "(OCTOBER 2024)"
month_11 = "(NOVEMBER 2024)"
month_12 = "(DECEMBER 2024)"

#Defining of of newly created functions that holds the number days per month:
def Jan():
    print(f"{month_1:^50}")
    print("-" * 51)
    print("Sun\t\tMon\t\tTue\t\tWed\t\tThurs\tFri\t\tSat")
    print("\t\t" * 1, end='')
    for i in range (1,32):
        print(i,end='\t\t')
        if (i + 1) % 7 == 0:
            print()
            
def Feb():
    print(f"{month_2:^50}")
    print("-" * 51)
    print("Sun\t\tMon\t\tTue\t\tWed\t\tThurs\tFri\t\tSat")
    print("\t\t" * 4, end='')
    for i in range (1,30):
        print(i,end='\t\t')
        if (i + 4) % 7 == 0:
            print()
            
def Mar():
    print(f"{month_3:^50}")
    print("-" * 51)
    print("Sun\t\tMon\t\tTue\t\tWed\t\tThurs\tFri\t\tSat")
    print("\t\t" * 5, end='')
    for i in range (1,32):
        print(i,end='\t\t')
        if (i + 5) % 7 == 0:
            print()   
            
def Apr():
    print(f"{month_4:^50}")
    print("-" * 51)
    print("Sun\t\tMon\t\tTue\t\tWed\t\tThurs\tFri\t\tSat")
    print("\t\t" * 1, end='')
    for i in range (1,31):
        print(i,end='\t\t')
        if (i + 1) % 7 == 0:
            print()

def May():
    print(f"{month_5:^50}")
    print("-" * 51)
    print("Sun\t\tMon\t\tTue\t\tWed\t\tThurs\tFri\t\tSat")
    print("\t\t" * 3, end='')
    for i in range (1,32):
        print(i,end='\t\t')
        if (i + 3) % 7 == 0:
            print()
            
def Jun():
    print(f"{month_6:^50}")
    print("-" * 51)
    print("Sun\t\tMon\t\tTue\t\tWed\t\tThurs\tFri\t\tSat")
    print("\t\t"* 6, end='')
    for i in range (1,31):
        print(i,end='\t\t')
        if (i + 6) % 7 == 0:
            print()

def Jul():
    print(f"{month_7:^50}")
    print("-" * 51)
    print("Sun\t\tMon\t\tTue\t\tWed\t\tThurs\tFri\t\tSat")
    print("\t\t"* 1, end='')
    for i in range (1,32):
        print(i,end='\t\t')
        if (i + 1) % 7 == 0:
            print()

def Aug():
    print(f"{month_8:^50}")
    print("-" * 51)
    print("Sun\t\tMon\t\tTue\t\tWed\t\tThurs\tFri\t\tSat")
    print("\t\t"* 4, end='')
    for i in range (1,32):
        print(i,end='\t\t')
        if (i + 4) % 7 == 0:
            print()
    
def Sept():
    print(f"{month_9:^50}")
    print("-" * 51)
    print("Sun\t\tMon\t\tTue\t\tWed\t\tThurs\tFri\t\tSat")
    print("\t\t"* 0, end='')
    for i in range (1,31):
        print(i,end='\t\t')
        if (i + 0) % 7 == 0:
            print()
            
def Oct():
    print(f"{month_10:^50}")
    print("-" * 51)
    print("Sun\t\tMon\t\tTue\t\tWed\t\tThurs\tFri\t\tSat")
    print("\t\t"* 2, end='')
    for i in range (1,32):
        print(i,end='\t\t')
        if (i + 2) % 7 == 0:
            print()

def Nov():
    print(f"{month_11:^50}")
    print("-" * 51)
    print("Sun\t\tMon\t\tTue\t\tWed\t\tThurs\tFri\t\tSat")
    print("\t\t"* 5, end='')
    for i in range (1,31):
        print(i,end='\t\t')
        if (i + 5) % 7 == 0:
            print()

def Dec():
    print(f"{month_12:^50}")
    print("-" * 51)
    print("Sun\t\tMon\t\tTue\t\tWed\t\tThurs\tFri\t\tSat")
    print("\t\t"* 0, end='')
    for i in range (1,32):
        print(i,end='\t\t')
        if (i + 0) % 7 == 0:
            print()

#User input of month and displays corresenponding month based on the input by the user:
try:
    print("\n")
    month_number = int(input("*Enter a number corresponding to a month in a year:"))
    print("\n")
    if month_number == 1:
        (Jan())
    elif month_number == 2:
        (Feb())
    elif month_number == 3:
        (Mar())
    elif month_number == 4:
        (Apr())
    elif month_number == 5:
        (May())
    elif month_number == 6:
        (Jun())
    elif month_number == 7:
        (Jul())
    elif month_number == 8:
        (Aug())
    elif month_number == 9:
        (Sept())
    elif month_number == 10:
        (Oct())
    elif month_number == 11:
        (Nov())
    elif month_number == 12:
        (Dec())
    elif month_number >= 12:
        print("*The number you have enter is invalid, please try again.")
except:
    print("\n")
    print("*Invalid input, please try again.")


   





































