class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while(True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
# Recursive binary search tree
    def _r_contains(self, current_node, value):
        if current_node == None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self._r_contains(current_node.left, value)
        if value > current_node.value:
            return self._r_contains(current_node.right, value)
    
    def r_contains(self, value):
        return self._r_contains(self.root, value)
    
    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value< current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value>current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def _r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

my_bst = BinarySearchTree()
#my_bst.insert(2)
#my_bst.insert(1)
#my_bst.insert(4)

#print(my_bst.root.value)
#print(my_bst.root.right.value)
#print(my_bst.root.left.value)

#print(my_bst.contains(4))
#print(my_bst.r_contains(4))

my_bst._r_insert(5)
my_bst._r_insert(3)
my_bst._r_insert(7)
print("Root", my_bst.root.value)
print("Left", my_bst.root.left.value)
print("Right", my_bst.root.right.value)