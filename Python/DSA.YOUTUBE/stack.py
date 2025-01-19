

# stack


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None
        self.size = 0
    def push(self,data):
        
        
        # if stack is empty
        if self.head == None:
            newnode = Node(data)
            self.head = newnode 
            self.size = self.size+1
            return

        # if stack have the valuees
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode 
        self.size = self.size+1
    def pop(self):
        self.head = self.head.next
        self.size = self.size - 1

    def peak(self):
        print(self.head.data)

    def show(self):
        result = ''
        curr = self.head
        while curr:
            
            
            result = result + str(curr.data)+","
            curr = curr.next
        return '['+result[:-1]+']' 
        

stack = stack()
stack.push(33)
stack.push(13)
stack.push(1)
stack.push(5)

print(stack.show())
print("size of stack ",stack.size)
stack.pop()
print(stack.show())
stack.peak()

print("size of stack ",stack.size)