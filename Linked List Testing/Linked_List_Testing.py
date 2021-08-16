# This project is to test linked lists in python
class Node:
    value = None
    next = None
    def __init__(self, value):
        self.value = value
        self.next = None # set next to null

class head: # dummy head class
    next = None
    def __init__(self): 
        self.next = None # set next to null

first = head
current = first
repeat = True
while repeat:
    print("1: add\n"+ # menu stolen from my previous projects
          "2: remove\n"+
          "3: print\n"+
          "4: quit\n")
    choice = input("enter choice: ")
    if choice == "4":
        repeat = False
    elif choice == "3":
        current = first.next
        while current != None:
            print(current.value)
            current = current.next

    elif choice == "2":
        removeVal = (input("Enter value to be removed: "))
        current = first.next
        prev = first
        while current.next != None:

            if current.value == removeVal: # remove value if true
                prev.next = current.next # causes the linked list to skip this value, thereby removing it
                print("First occurence of value removed")
                break
            prev = current
            current = current.next
        
    elif choice == "1":
        newVal = (input("Enter new value: "))
        if first.next == None:
            first.next = Node(newVal) # create first node
            current = first.next
        else:
            current = first.next
            while current.next != None:
                current = current.next
            current.next=Node(newVal) # create new node