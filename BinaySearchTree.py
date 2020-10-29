class Node(object):
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
class BinarySearchTree(object):
    def __init__(self):
        self.root = None
    def insert(self,data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data,self.root)
    def insertNode(self,data,node):
        if data < node.data:
            if node.leftchild:
               self.insertNode(data,node.leftchild)
            else:
                node.leftchild = Node(data)
        else:
            if node.rightchild:
                self.insertNode(data,node.rightchild)
            else:
                node.rightchild = Node(data)
    def remove(self,data):
        if self.root:
            self.root = self.removeNode(data,self.root)
    def removeNode(self,data,node):
        if not node:
            return node
        if data < node.data:
            node.leftchild = self.removeNode(data,node.leftchild)
        elif data > node.data:
            node.rightchild = self.removeNode(data,node.rightchild)
        else:
            if not node.leftchild and not node.rightchild:
               print("Removing a leaf node...")
               del node
               return node
            if not node.leftchild:
                print("Removing a node with single right-child..")
                tempnode = node.rightchild
                del node 
                return tempnode
            elif not node.rightchild:
                 print("Removing a node with single left-child...")
                 tempnode = node.leftchild
                 del node 
                 return tempnode
            else:
                print("Removing a node with two children...")
                tempnode = self.getPredecessor(node.leftchild)
                node.data = tempnode.data
                node.leftchild = self.removeNode(tempnode.data,node.leftchild)
        return node
    
    def getPredecessor(self,node):
        if node.rightchild:
            return self.Predecessor(node.rightchild)
        return node
    def traverse(self):
        if self.root:
            self.traverse_Inorder(self.root)
    def traverse_Inorder(self,node):
        if node.leftchild:
           self.traverse_Inorder(node.leftchild)
        print("%s"% node.data)
        
        if node.rightchild:
            self.traverse_Inorder(node.rightchild)
                
                
                
b1 = BinarySearchTree()
b1.insert(10)
b1.insert(13)
b1.insert(5)
b1.insert(15)
b1.insert(4)
b1.insert(6)
b1.remove(13)
b1.traverse()


                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
