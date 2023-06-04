class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def partition_list(self, x):
        if self.length == 0:
            return

        less_head = None
        less_tail = None
        greater_head = None
        greater_tail = None

        current = self.head

        while current is not None:
            if current.value < x:
                if less_head is None:
                    less_head = current
                    less_tail = current
                else:
                    less_tail.next = current
                    less_tail = current
            else:
                if greater_head is None:
                    greater_head = current
                    greater_tail = current
                else:
                    greater_tail.next = current
                    greater_tail = current

            current = current.next

        if less_head is None:
            self.head = greater_head
        else:
            self.head = less_head
            less_tail.next = greater_head

        if greater_tail is not None:
            greater_tail.next = None

ll = LinkedList(3)
ll.append(5)
ll.append(8)
ll.append(10)
ll.append(2)
ll.append(1)

print("LL before partition_list:")
ll.print_list()  # Output: 3 5 8 10 2 1

ll.partition_list(5)

print("LL after partition_list:")
ll.print_list()  # Output: 3 2 
