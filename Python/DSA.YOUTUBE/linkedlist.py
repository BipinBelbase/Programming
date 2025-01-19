
# its a collection of nodes
# nodes haved two component one is DATA and another is next node address
# why use linked list instead of array
# array size is unutilized 
# we can create more data structure .. stack ques .. doubly linked list, circular LL .
# we use heavy read with array and (search)write heavy with linked list

class Node:

    def __init__(self,data):

        self.data = data
        self.next = None

class linkedList:
    def __init__(self,data = None):
        if data:
            self.insert_head(data)
            return

        
        self.head = Node("HEAD")
        self.tail = Node("TAIL")
        self.head.next = self.tail
        self.totalitems = 0


    def __len__(self):
        return self.totalitems
       
    def insert_head(self,data):
        self.totalitems = self.totalitems + 1
        new_node = Node(data)
        if self.head.next == self.tail:
            new_node.next = self.tail
            self.head.next = new_node
            return

        new_node.next = self.head.next
        self.head.next = new_node

   

    def append(self,value):
        new_node = Node(value)

        if self.head.next == self.tail:
                self.insert_head(value)
                self.totalitems = self.totalitems + 1
                return

        current = self.head.next
        while current.next != self.tail:
            current = current.next

        new_node.next = self.tail
        current.next = new_node
        self.totalitems = self.totalitems + 1

    def __str__(self):
        curr = self.head.next

        result = ''

        while curr != self.tail:
            result =  result  +str(curr.data) +','
            curr = curr.next

        return '['+result[:-1]+']'
    
    def clear(self):
         current = self.head.next
         while current != self.tail:
             next_node = current.next  # Store the next node
             current.next = None  # Disconnect the current node
             current = next_node  # Move to the next node

         self.head.next = self.tail  # Reset the head to point to the tail node
         self.totalitems = 0
         print("linked list cleared")

# insert after .. eg. (3,12)....... insert in 3rd index what ever there shift right
    def insert(self, index, value):
             if self.head.next == self.tail:
                 print("List is empty")
                 return
 
             if index < 0 or index > self.totalitems:
                 print("Index out of range")
                 return

             curr = self.head.next
             for i in range(index - 1):  # Traverse to the node before the insertion index
                    curr = curr.next

        # Create the new node and insert it
             new_node = Node(value)
             new_node.next = curr.next  # New node points to the next node
             curr.next = new_node  # Previous node points to the new node
 
             self.totalitems += 1
    def insertaftervalue(self,value,newvalue):
            

            if self.head.next == self.tail:
                 print("List is empty")
                 return
            curr = self.head.next
            while curr.next.data != value:
                curr = curr.next
                if curr.next == None:
                     print("value not in the linked list")
                     return 

        # Create the new node and insert it
            new_node = Node(newvalue)
            new_node.next = curr.next  # New node points to the next node
            curr.next = new_node  # Previous node points to the new node
 
            self.totalitems += 1

#check
l = linkedList()
l.insert_head(1)
l.insert_head(2)
l.insert_head(3)
l.insert_head(4)

l.append(5)
print(l)
print("now doing insert after value")
l.insertaftervalue(133,100)
print("after the inserting 133,100")
print(l)