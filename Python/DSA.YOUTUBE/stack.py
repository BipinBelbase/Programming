

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
        if self.head:
            valuetoreturn = self.head.data 
            self.head = self.head.next
            self.size = self.size - 1
            return valuetoreturn
        else:
            print("noting to pop")
            return

    def peak(self):
        print(self.head.data)

    def show(self):
        result = ''
        curr = self.head
        while curr:
            
            
            result = result + str(curr.data)+","
            curr = curr.next
        return '['+result[:-1]+']' 





check = stack()

check.push(22)
check.push(33)
check.push(99)

print(check.show())

check.pop()

print(check.show())

print("poped item is ",check.pop())
