
class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self,data = None):

        self.first = None


    def add(self,data):
        newnode = Node(data)

        if self.first == None:
             
           
             
             
    
            # we can add here
             self.first = newnode

             return

        # if first data is not empty we have to do 
        # before adding new node we have to store the address of that node so we can link it to new node
        # new node address = oldnode.next..
        # so it means self.first.data = xxx and self.next=None
        # so just do self.first.next = newnode and then self.
        temp = self.first
        while temp.next != None:
            temp = temp.next
        temp.next = newnode
       

    # print function .. printing all nodes dataOnly
    def print(self):
        temp = self.first
        
        while temp != None:
            print(temp.data)
           
            temp = temp.next
     

l = LinkedList(2)
l.add(4)
l.add(22)
l.add(1)
l.add(8)
l.print()
