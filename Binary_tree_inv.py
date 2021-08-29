class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):
    # Compare the new value with the parent node
      if self.data:
        if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
        elif (data > self.data):
           if self.right is None:
              self.right = Node(data)
           else:
              self.right.insert(data)
      else:
         self.data = data

# Inorder traversal
# Left -> Root -> Right
   def inorderTraversal(self, root):
      res = []
      if root:
         res = self.inorderTraversal(root.left)
         res.append(root.data)
         res = res + self.inorderTraversal(root.right)
      return res

# Use the insert method to add nodes
root = Node(4)
root.insert(7)
root.insert(2)
root.insert(1)
root.insert(3)
root.insert(6)
root.insert(9)
print(root.inorderTraversal(root)) 

def invertTree(node):
    if(node):
        temp = node.left
        node.left = node.right
        node.right = temp
        invertTree(node.left)
        invertTree(node.right)
        
invertTree(root)
print(root.inorderTraversal(root)) 
