# This LinkedList program has methods for inserting, and setting values

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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def set_value(self, target, value):
        new_node = Node(value)
        temp = self.head
        for _ in range(self.length):
            if temp.value == target:
                temp.value = value
                return True
            temp = temp.next

    def insert(self, target, value):
        new_node = Node(value)
        temp = self.head
        after = self.head
        if target == self.tail.value:
            self.append(value)
            return True
        for _ in range(self.length):
            try:
                if temp.value == target:
                    temp.next = new_node
                    new_node.next = after
                    self.length += 1
                    return True
                else:
                    temp = temp.next
                    after = temp.next
            except AttributeError:
                print("index out of range")
        return False

                            #  H         T         AT
                            #  1 -> 2 -> 3 -> 7 -> 4


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.print()

# my_linked_list.set_value(2, 3)
print()
my_linked_list.print()
print()

my_linked_list.insert(4, 5)
my_linked_list.print()

