class Node:
    def __init__(self, value):
        # Store node value
        self.value = value
        # Reference to next node
        self.next = None
        # Reference to previous node
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self, value):
        # Create new node with value
        new_node = Node(value)
        # Set head to new node
        self.head = new_node
        # Set tail to new node
        self.tail = new_node
        # Set initial length to 1
        self.length = 1
