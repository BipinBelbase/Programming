#here we make nodes and all things needed to implement it 
# traverse pre,post,inorder post ......
#search 
#insert

# binary search tree 
# 1. each node should have 0 or 1 or two nodes in the tree(binar tree)
# 2. left node should be smaller than the right node so fotth


#Binary Tree 
# Binary Tree Node
# HEIGHT OF BINARTY TREE .............

class Node:
    def __init__(self, data):
        # data left right height
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # if empty just make node and add
          # otherwise call recursion with root.
          if self.root == None:
              newnode = Node(data)
              self.root = newnode
              return
          self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
   
        if node.data > data:
            if node.left == None:
                node.left = Node(data)
                
            else:
                self._insert_recursive(node.left, data)

        if node.data < data:
            if node.right== None:
                node.right= Node(data)
                
            else:
                self._insert_recursive(node.right, data)
       
        
        
        

    def BFS(self,data):
        pass
    
    
    def printr(self,head):
        if head == None:
            return 
        self.printr(head.left)
        print(head.data)
        self.printr(head.right)

    
    def print(self):
        return self.printr(self.root)
    
    def printBFS(self):
        root = self.root
        if not root:
            return

        queue = [root]  # Initialize a queue with the root node

        while queue:
            current = queue.pop(0)  # Dequeue the current node
            print(current.data)  # Process the current node

            if current.left:
                queue.append(current.left)  # Enqueue the left child
            if current.right:
                queue.append(current.right)


            



bst = BST()
bst.insert(22)
bst.insert(1)
bst.insert(2)
bst.insert(28)
bst.printBFS()