#Initialization of variables to be used and defining a class:
class queues():
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    option1 = 0
    option2 = 0
    option3 = 0
    ent_word1 = 0
    ent_word2 = 0

#User input words and stores it ina a list and create another list that reverses the words from the user input:
    def generate_queues(self):
        self.ent_word1 = input("Enter any word:").lower()
        self.list1.append(self.ent_word1)
        while True:
            self.option1 = input("Do you want to add another word (Y/N):").upper()
            if self.option1 == "Y":
                self.ent_word1 = input("Enter any word:").lower()
                self.list1.append(self.ent_word1)
                continue
            elif self.option1 == "N":
                break
        for wrd in self.list1:
            self.list2.append(''.join(list(wrd)))
        for wrd in self.list2:
            self.list3.append(''.join(list(wrd[::-1])))
        print("Normal queues:", self.list2)
        print("Check is word is reverse still the same:", self.list3)

#Checks word by word and by its letter if they have the same letters even if swapped and appended all letters that pass the checking into a list:
    def palindrome_enqueues(self):
        for wrd2, wrd3 in zip(self.list2, self.list3):
            if sum((ord(a) - ord(b))**2 for a, b in zip(wrd2, wrd3)) == 0 and len(wrd2) == len(wrd3):
                self.list4.append(wrd2)
            else:
                self.list5.append(wrd2)
        print("Palindrome words:", self.list4)
        print("Non-palidrome words:", self.list5)

#Removes a word in the list of all Palindrome words:
    def palindrome_diqueues(self):
        self.option3 = input("Do you want remove a word (Y/N):").upper()
        if self.option3 == "Y":
            self.list4.pop(0)
            print("Updated palindrome words:", self.list4)
        elif self.option3 == "N":
            print("Palindrome words:", self.list4)

#Checks if queue is empty:
    def isEmpty(self):
        if len(self.list4) == 0:
            print("Empty")
        else:
            print("There are contents inside")

#Peeks the front element in a queue:
    def peek_queues(self):
        if len(self.list4) == 0:
            print("Empty")
        else:
            print("First word:", self.list4[0])

Q = queues()
Q.generate_queues()
print(" ")
Q.palindrome_enqueues()
print(" ")
Q.palindrome_diqueues()
print(" ")
Q.isEmpty()
print(" ")
Q.peek_queues()
