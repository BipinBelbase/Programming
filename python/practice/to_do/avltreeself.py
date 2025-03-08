class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.head = None

    def insertion(self,val):
        if self.head == None:
            self.head = Node(val)
            return 
        
        self.head = self._insertion(self.head , val)

    def _insertion(self,head,value):

       
            if value < head.val:
                if head.left == None:
                    head.left = Node(value)

                else: 
                    head.left = self._insertion(head.left, value)
                    


            if value > head.val:
                if head.right == None:
                    head.right = Node(value)                
                else:
                    head.right= self._insertion(head.right, value)
                  
                    
            head.height = self.cal_height(head)
        #we have to change the head like if we have done rotation and our old head is "a" and now out new head"b " so we have to assign out head to the head of actuall code
            head = self.rebalance(head)
            return head


    
    def get_height(self,node):
        if node == None:
            return 0
        return node.height

    def cal_height(self,node):
        
        return 1+max(self.get_height(node.left),self.get_height(node.right))
        
        
 


    def rebalance(self,head):
        balance_factor = self.balance_factor(head)
        if balance_factor >= -1 and balance_factor <= 1:
            return head
        elif balance_factor <-1:
            #do left rotate
            if self.balance_factor(head.right) >0:
                #children right rotate then parent  left rotate
                head.right = self.right_rotate(head.right)

            #now do left rotate
            return self.left_rotate(head)

        elif balance_factor > 1 :
            #do left rotate
            if self.balance_factor(head.left) < 0:
                #children left rotate then parent right rotate
                head.left = self.left_rotate(head.left)

            return self.right_rotate(head)
             
        
    def balance_factor(self,node):
        if node == None:
            return 0
       
        return self.get_height(node.left) -  self.get_height(node.right)


    def left_rotate(self,head):
        #it just totate right and return 
        pointer = head.right
        head.right = pointer.left
        pointer.left =head

        head.height = self.cal_height(head)
        pointer.height = self.cal_height(pointer)
    
        return pointer
        
    def right_rotate(self,head):

        pointer = head.left
        head.left = pointer.right
        pointer.right = head

        head.height = self.cal_height(head)
        pointer.height = self.cal_height(pointer)
    

        return pointer


    def print(self):
        print("preorder traverse:")
        self.preorder(self.head)
        print("postorder traverse:(coming soon be in touch )")

    def preorder(self, head):
        if head == None:
            
            return
        print("[",head.val,"]","Height",head.height)

        self.preorder(head.left)
        self.preorder(head.right)

        
        


#driver code
def main():
    tree = AVL()
    tree.insertion(3)
    tree.insertion(4)
    tree.insertion(5)
    tree.insertion(2)
    tree.insertion(1)
    tree.print()
    

if __name__ == "__main__":
    main()





