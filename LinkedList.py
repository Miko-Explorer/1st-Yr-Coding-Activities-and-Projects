class linknodes():
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class linkedlist():
    def options(self):
        print("-" * 40)
        print(f"{'Menu':^40}")
        print("-" * 40)
        print("1. Add string")
        print("2. Display List of strings")
        print("3. Display List of 3-letter words")
        print("4. Display List of 4-letter words")
        print("5. Delete a 3-letter word")
        print("6. Delete a 4-letter word")
        print("7. Quit")
        print("-" * 40)

    def __init__(self, head_value=None):
        self.head_value = head_value
        self.list_words = []
        self.list_3words = []
        self.list_4words = []
        self.updated_linkedlist1 = []
        self.updated_linkedlist2 = []

    # Insertion of nodes in linked list:
    def add_string(self, value):
        new_value = linknodes(value)
        if self.head_value is None:
            self.head_value = new_value
            return
        current_node = self.head_value
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = new_value

    # Transversing through nodes in linkedlist:
    def display_list(self):
        current_node = self.head_value
        if current_node != None:
            while current_node is not None:
                self.list_words.append(current_node.value)
                current_node = current_node.next_node
            print(self.list_words)
        elif current_node == None:
            print("Linked list is empty")

    # Transversing through 3-letter nodes in linkedlist:
    def display_3words(self):
        current_node = self.head_value
        if current_node != None:
            while current_node is not None:
                if len(current_node.value) == 3:
                    self.list_3words.append(current_node.value)
                current_node = current_node.next_node
            print(self.list_3words)
        elif current_node == None:
            print("Linked list is empty")

    # Transversing through 4-letter nodes in linkedlist:
    def display_4words(self):
        current_node = self.head_value
        if current_node != None:
            while current_node is not None:
                if len(current_node.value) == 4:
                    self.list_4words.append(current_node.value)
                current_node = current_node.next_node
            print(self.list_4words)
        elif current_node == None:
            print("Linked list is empty")

    # Deletion of 3-letter words in linkedlist:
    def delete_3words(self, value):
        current_node = self.head_value
        if current_node == None:
            print("Linked list is empty")
            return
        elif current_node.value == value:
            self.head_value = current_node.next_node
            current_node = None
            return
        previous_value = None
        while current_node and current_node.value != value:
            previous_value = current_node
            current_node = current_node.next_node
        if current_node is None:
            return
        previous_value.next_node = current_node.next_node
        current_node = None
        current_node = self.head_value
        while current_node:
            self.updated_linkedlist1.append(current_node.value)
            current_node = current_node.next_node
        print(self.updated_linkedlist1)

    # Deletion of 4-letter words in linkedlist:
    def delete_4words(self, value):
        current_node = self.head_value
        if current_node == None:
            print("Linked list is empty")
            return
        elif current_node.value == value:
            self.head_value = current_node.next_node
            current_node = None
            return
        previous_value = None
        while current_node and current_node.value != value:
            previous_value = current_node
            current_node = current_node.next_node
        if current_node is None:
            return
        previous_value.next_node = current_node.next_node
        current_node = None
        current_node = self.head_value
        while current_node:
            self.updated_linkedlist2.append(current_node.value)
            current_node = current_node.next_node
        print(self.updated_linkedlist2)

    # Store text in a file then exit the program:
    def store_to_string(self, file):
        with open(file, "w") as file:
            file.write(str(self.list_words))
        print("list of string save to strings.txt")

    def store_to_3word(self, file):
        with open(file, "w") as file:
            file.write(str(self.list_3words))
        print("list of 3 letters to word3.txt")

    def store_to_4word(self, file):
        with open(file, "w") as file:
            file.write(str(self.list_4words))
        print("list of 4 letters to word4.txt")


LL = linkedlist()
LL.options()
while True:
    option = input("Enter choice from menu:")
    print("-" * 40)
    if option == "1":
        while True:
            input_strings = input("Enter any string or word (type 'fin' if your done):").lower()
            print("-" * 40)
            if input_strings == 'fin':
                break
            valid_string_input = True
            for character in input_strings:
                if not ('a' <= character <= 'z'):
                    valid_string_input = False
                    break
            if not valid_string_input:
                print("Invalid input")
                print("-" * 40)
            LL.add_string(input_strings)
    elif option == "2":
        LL.display_list()
        print("-" * 40)
    elif option == "3":
        LL.display_3words()
        print("-" * 40)
    elif option == "4":
        LL.display_4words()
        print("-" * 40)
    elif option == "5":
        input_3letter = input("Enter a 3 letter element to delete that is in the linkedlist:").lower()
        print("-" * 40)
        if len(input_3letter) == 3:
            LL.delete_3words(input_3letter)
            print("-" * 40)
        elif len(input_3letter) != 3:
            print("This word is not a 3 letter word")
            print("-" * 40)
    elif option == "6":
        input_4letter = input("Enter a 4 letter element to delete that is in the linkedlist:").lower()
        print("-" * 40)
        if len(input_4letter) == 4:
            LL.delete_4words(input_4letter)
            print("-" * 40)
        elif len(input_4letter) != 4:
            print("This word is not a 3 letter word")
            print("-" * 40)
    elif option == "7":
        input_file_strings = input("Enter file name to store the list of inputed strings:")
        input_file_3word = input("Enter file name to store 3 letters found in the linkedlist:")
        input_file_4word = input("Enter file name to store 4 letters found in the linkedlist:")
        LL.store_to_string(input_file_strings)
        LL.store_to_3word(input_file_3word)
        LL.store_to_4word(input_file_4word)
        print("-" * 40)
        print("That's all, thank you")
        print("-" * 40)
        break
    else:
        print("Invalid choice")
        print("-" * 40)