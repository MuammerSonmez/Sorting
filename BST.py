class Node:
    def __init__(self, data):
        self.data = data  
        self.left = None  
        self.right = None 

class BinarySearchTree:
    def __init__(self):
        self.root = None  


    def insert(self, data):
        if self.root is None:
            self.root = Node(data)  
        else:
            self._insert(self.root, data)


    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)  
            else:
                self._insert(node.left, data) 
        else:
            if node.right is None:
                node.right = Node(data)  
            else:
                self._insert(node.right, data) 

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None or node.data == data:
            return node  
        if data < node.data:
            return self._search(node.left, data)  
        return self._search(node.right, data)  
    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)  
            print(node.data, end=' ') 
            self.in_order_traversal(node.right)  


bst = BinarySearchTree()
bst.insert(7)
bst.insert(5)
bst.insert(1)
bst.insert(8)
bst.insert(3)
bst.insert(6)
bst.insert(0)
bst.insert(9)
bst.insert(4)
bst.insert(2)

print("\nArama:")
print("2 mevcut mu?", bst.search(2) is not None)  
print("10 mevcut mu?", bst.search(10) is not None)  
 

