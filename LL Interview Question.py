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
        if self.head and self.tail is None:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def find_middle_node(self):
        if self.head and self.tail is None:
            return None
        slow = self.head
        fast = self.head.next

        while fast is not None:
            print("this is slow", slow.value)
            print("this is fast", fast.value)
            slow = slow.next
            try:
                fast = fast.next.next
            except AttributeError:
                return slow
        return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)


my_linked_list.print()
print()
print(my_linked_list.find_middle_node().value)


# print(my_linked_list.length)

