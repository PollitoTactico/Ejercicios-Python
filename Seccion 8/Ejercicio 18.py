class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
        new_node = Node(value)
        new_node.prev = self.top
        self.top.next = new_node
        self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            raise IndexError("Stack is empty")
        value = self.top.value
        self.top = self.top.prev
        if self.top:
            self.top.next = None
        self.height -= 1
        return value

    def is_empty(self):
        return self.height == 0


my_stack = Stack(4)

print('Top:', my_stack.top.value)
print('Height:', my_stack.height)



"""
    EXPECTED OUTPUT:
    ----------------
    Top: 4
    Height: 1

"""
