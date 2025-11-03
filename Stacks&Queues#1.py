import re

class stack():
    def __init__(self):
        self.text = []
        self.list1 = []
        self.list2 = []
        self.list3 = []
        self.list4 = []
        self.list5 = 0
        self.list6 = []
        self.list7 = []
        self.long = 0
        self.short = 0

    def read_display_text(self):
        with open("SAMPLE#1.txt", "r") as file:
            for line in file:
                print(line.strip())

    def convert_line_to_list(self):
        with open("SAMPLE#1.txt", "r") as file:
            for line in file:
                self.text.append(line.strip())

    def check_every_palindrom(self):
        with open("SAMPLE#1.txt", "r") as file:
            self.list1 = re.findall(r'\b\w+\b', file.read()) #Returns a list of all words in the paragraph.
            for word in self.list1:
                self.list2.append(word.lower())
            for word in self.list2:
                if word == word[::-1]:
                    self.list3.append(word)
                else:
                    self.list4.append(word)
            print("Palindrome:", self.list3)

    def filter_palindrome_list(self):
        self.list5 = [word for word in self.list3 if word[1:]] #Filters elements who have 1 character.
        for word in self.list5:
            if any(letter.isdigit() for letter in word): #Filters elements that have numbers in it.
                self.list6.append(word)
            else:
                self.list7.append(word)
        print("Filtered palindrome list:", self.list7)

    def check_palindrome_in_paragraph(self):
        for word in self.list7:
            if len(word) > len(self.list7[0]):
                self.long = word
        for word in self.list7:
            if len(word) < len(self.list7[0]):
                self.short = word
        for i, line in enumerate(open("SAMPLE#1.txt"), 1): #Finds the line where the longest palindrome word is.
            if self.long in line:
                print("Longest palindrome:", self.long, "Line:", i)
        for i, line in enumerate(open("SAMPLE#1.txt"), 1): #Finds the line where the longest palindrome word is.
            if self.short in line:
                print("Shortest palindrome:", self.short, "Line:", i)

s = stack()
s.read_display_text()
s.convert_line_to_list()
print(" ")
s.check_every_palindrom()
print(" ")
s.filter_palindrome_list()
print(" ")
s.check_palindrome_in_paragraph()