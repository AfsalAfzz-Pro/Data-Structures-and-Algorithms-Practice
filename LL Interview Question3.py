# THIS IS A PROGRAM TO FIND IF A LINKEDLIST IS CIRCULAR
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

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def make_circular(self):
        self.tail.next = self.head     # This will make the Linked List circular

    def check_circular_ll(self):       # We will use this method too check if LinkedList is circular
        slow = self.head
        fast = self.head.next
        count = 0
        while fast != slow and count != self.length:
            slow = slow.next
            try:
                fast = fast.next.next
            except AttributeError:
                return "is not circular"
            count += 1
        return "is circular"


# Let's test it
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.make_circular()


print(my_linked_list.check_circular_ll())  # Output: 'is circular'
