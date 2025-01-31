


# queue


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class queue:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0
    def enqueue(self,data):
        # if stack is empty
        if self.head == None:
            newnode = Node(data)
            self.head = newnode 
            self.last = newnode
            self.size = self.size+1
            return

        # if stack have the valuees
        newnode = Node(data)
        self.last.next = newnode
        self.last = newnode
        self.size = self.size+1
    def dequeue(self):
        if self.head:
            valuetoreturn = self.head.data 
            self.head = self.head.next
            self.size = self.size - 1
            return valuetoreturn
        else:
            print("noting to dequeue")
            return
        
   

    def __len__(self):
        return self.size
    
    def peak(self):
        print(self.head.data)

    def show(self):
        result = ''
        curr = self.head
        while curr:
            
            
            result = result + str(curr.data)+","
            curr = curr.next
        return '['+result[:-1]+']' 
    






check = queue()

check.enqueue(22)
check.enqueue(33)
check.enqueue(99)

print(check.show())
print("this is the length of queue",len(check))
check.dequeue()

print(check.show())

print("dequeued  item is ",check.dequeue())




