# avl tree implementation by self in python 
# we will first  nodes 
# then make binary tree 
# then check is it balanced 
# and final step rebalance it using rotation rr,ll,rl,ls 4 functions


class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0

class AVL:
    def __init__(self):
        self.head = None

    def insertion(self,val):
        if self.head == None:
            node = Node(val)
            return
        

        node = Node(val)

        if head.val > node.val:
            insertion(self.head.left)
           
            self.head.left =
            
        if head.val < val:
            insertion(self.head.right)

      
    def deletion(self,val):
        pass

    def rotation(self,root):
        pass

    def get_height(self,node):
        pass

    def balance_factor(self,node):
        #calculating bf by leftheight - right height
        pass

    def print_tree():
        pass


#driver code
def main():
    tree = AVL()
    tree.insertion(1)
    tree.insertion(2)
    tree.insertion(3)

    tree.print_tree()
    