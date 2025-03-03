# stack

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        # if stack is empty
        if self.head == None:
            newnode = Node(data)
            self.head = newnode
            self.size = self.size + 1
            return

        # if stack has values
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
        self.size = self.size + 1

    def pop(self):
        self.head = self.head.next
        self.size = self.size - 1

    def peak(self):
        print(self.head.data)

    def show(self):
        result = ''
        curr = self.head
        while curr:
            result = result + str(curr.data) + ","
            curr = curr.next
        return '[' + result[:-1] + ']'

    def string(self, string):
        for i in string:
            newnode = Node(i)
            newnode.next = self.head
            self.head = newnode
            self.size = self.size + 1


string1 = stack()
string2 = stack()

def undoredo():
    s = input("What string do you want to play with? ")
    string1.string(s)
        
    while True:
        x = input("Please write 'r' for redo and 'u' for undo: q for quit ")
        if x == "q":
            return
        if x == "r":
            redo()
        elif x == "u":
            undo()
        else:
            print("Please write 'r' for redo or 'u' for undo...")

def redo():
    if string2.head:
        string1.push(string2.head.data)
        string2.pop()
        print(f"this is string1 {string1.show()} and this is string2: {string2.show()}")
    else:
        print("Nothing to redo")
        return
    

def undo():
    if string1.head:

        string2.push(string1.head.data)
        string1.pop()
        print(f"this is string1 {string1.show()} and this is string2: {string2.show()}")
    else:
        print("Noting to undo")
        return
undoredo()
