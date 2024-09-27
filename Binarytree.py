class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.root=None
        self.temp=None
        self.temp1=None
    def creation(self,data):
        newnode=Node(data)
        if self.root is None:
            self.root=newnode
        else:
            self.temp=self.root
            self.temp1=self.root
            flag=0
            while True:
                if self.temp.left is None:
                   self.temp.left=newnode
                   break
                elif self.temp.right is None:
                    self.temp.right=newnode
                    break
                elif flag==0:
                    self.temp=self.temp.left
                    flag=1
                else:
                    self.temp=self.temp1.right
                    flag=0
                    self.temp1=self.temp1.left
    def display(self, node):
        if node:
            # Traverse the left subtree
            self.display(node.left)
            # Visit the root (current node)
            print(node.data, end=" ")
            # Traverse the right subtree
            self.display(node.right)

n=int(input("Enter the number of node size:"))
a=BinaryTree()
for i in range (1,n+1):
    data=int(input(f"Enter the data for node {i}: "))
    a.creation(data)
print("In-order traversal of the binary tree:")
a.display(a.root)