class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, value):
        self.stack_list.append(value)

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def pop(self):
        return self.stack_list.pop()


my_stack = Stack()
my_stack.print_stack()
print("Stack before popping")
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print("Stack after popping")
my_stack.print_stack()

print("\npopped value: ", my_stack.pop())

print("\nStack after popping")
my_stack.print_stack()
