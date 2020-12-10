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
    def removeNode(self, data, node):
	
		if not node:
			return node
			
		if data < node.data:
			node.leftChild = self.removeNode(data, node.leftChild)
		elif data > node.data:
			node.rightChild = self.removeNode(data, node.rightChild)
		else:
			
			if not node.leftChild and not node.rightChild:
				print("Removing a leaf node...")
				del node
				return None
				
			if not node.leftChild:  # node !!!
				print("Removing a node with single right child...")
				tempNode = node.rightChild
				del node
				return tempNode
			elif not node.rightChild:   # node instead of self
				print("Removing a node with single left child...")
				tempNode = node.leftChild
				del node
				return tempNode
			
			print("Removing node with two children....")
			tempNode = self.getPredecessor(node.leftChild)   # self instead of elf  + get predecessor 
			node.data = tempNode.data
			node.leftChild = self.removeNode(tempNode.data, node.leftChild)
		
		return node  # 

	def getPredecessor(self, node):
	
		if node.rightChild:
			return self.getPredeccor(node.rightChild)
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


                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
