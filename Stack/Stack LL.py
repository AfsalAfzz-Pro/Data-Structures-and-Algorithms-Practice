class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            temp = self.top
            self.top = new_node
            new_node.next = temp
        self.height += 1

    # def push(self, value):
    #     new_node = Node(value)
    #     if self.height == 0:
    #         self.top = new_node
    #     else:
    #         new_node.next = self.top
    #         self.top = new_node
    #     self.height += 1
    #     return True

    def pop(self):
        if self.top is None:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
        self.height -= 1
        return temp.value


my_stack = Stack(4)

my_stack.push(5)
my_stack.push(6)
print("popped value: ", my_stack.pop())
print("popped value: ", my_stack.pop())
print("popped value: ", my_stack.pop())
my_stack.push(6)
my_stack.push(5)


print()
my_stack.print_stack()
print('Top:', my_stack.top.value)
print('Height:', my_stack.height)

