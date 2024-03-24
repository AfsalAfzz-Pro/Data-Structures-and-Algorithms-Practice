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
        return True


# List to convert
my_list = [1, 2, 3, 4, 5]

# creating linked list
my_linked_list = LinkedList(my_list[0])

# iterating over list to append it to my_linked_list
for i in range(1, len(my_list)):
    my_linked_list.append(my_list[i])

# calling the print function on LinkedList
my_linked_list.print()
