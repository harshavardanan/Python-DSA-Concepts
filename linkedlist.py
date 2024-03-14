# Single Linked List so next keyword means the address pointing to "next node" 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    #print linked list
    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1

    def pop(self):
        if self.length == 0:
            return "Linked List is empty"
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length-=1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp 
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1

    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return temp.value
    
    def get(self, index):
        if index<0 or index>=self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert_value(self, index, value):
        if index<0 or index>self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index>self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length+=1
        return True

    def remove(self, index):
        if index<0 or index>=self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after



my_list = LinkedList(3)

my_list.append(5)
my_list.append(7)
my_list.append(8)
print("After append")
print(my_list.print_list())

my_list.pop()
print("After Pop")
print(my_list.print_list())

my_list.prepend(0)
print("After Prepend")
print(my_list.print_list())

my_list.pop_first()
print("After pop head value")
print(my_list.print_list())

#get value based on index
print("Getting a value")
print(my_list.get(2))

print("Setting different value to index")
print(my_list.set_value(2,9))
print(my_list.print_list())

print("Inserting value to list")
print(my_list.insert_value(2,7))
print(my_list.insert_value(1,0))
my_list.print_list()

print("Removing element from the list")
print(my_list.remove(3))

print("reversing a list")
print(my_list.reverse())
my_list.print_list()
