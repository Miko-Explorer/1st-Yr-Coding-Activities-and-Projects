#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Science():
    def __init__(self, name, age, uni):
        self.name = name
        self.age = age
        self.uni = uni
        
    def display_info(self):
        print("Name:", self.name)
        print("Current age:", self.age)
        print("Current uni:", self.uni)

class Program(Science):
    def __init__(self, name, age, uni, program):
        super().__init__(name, age, uni)
        self.program = program
    
    def display_info(self):
        super().display_info()
        print("Current program enrolled to:", self.program)

class Subintr(Program):
    def __init__(self, name, age, uni, program, subintr):
        super().__init__(name, age, uni, program)
        self.subintr = subintr

    def display_info(self):
        super().display_info()
        print("Favorite course in your program:", self.subintr)

cour = Science("Enrico Miguel Veloso", 19, "UST")
cour.display_info()
cour1 = Program("Erika Michelle Veloso", 20, "UST", "DSA")
cour1.display_info()
cour2 = Program("Ashley Michelle Vasco", 21, "FEU", "AM")
cour2.display_info()
cour3 = Subintr("Danica Whimsley", 22, "ADMU", "CE", "Calculus")
cour3.display_info()
cour4 = Subintr("Ben Caliba", 23, "USE", "IE", "Stats")
cour4.display_info()


# In[ ]:


class Vehicle():
    def __init__(self, name):
        self.name = name

class Wheeled_Vehicles(Vehicle):
    def car(self):
        print("Car:", self.name)
    def bike(self):
        print("Bike:", self.name)

class Car(self):
    def ev(self): 
        print("E vehicle:", self.name)
    def gv(self):
        print("G vehicle:", self.name)

class 

