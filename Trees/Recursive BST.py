class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    # def closest_value(self, target):
    #     closest = self.root.value
    #     node = self.root
    #     while node:
    #         if node.value == target:
    #             return target
    #         if target < node.value:
    #             closest = min(closest, node.value)
    #             node = node.left
    #         else:
    #             closest = max(closest, node.value)
    #             node = node.right
    #
    #     return closest

    def __r_contains(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)


my_bst = BinarySearchTree()
my_bst.insert(47)
my_bst.insert(27)
my_bst.insert(54)
my_bst.insert(17)
my_bst.insert(4)
my_bst.insert(21)

print("\t\t\t", my_bst.root.value)
print("        ", my_bst.root.left.value, "\t ", my_bst.root.right.value)
print("\t", my_bst.root.left.left.value)
print(" ", my_bst.root.left.left.left.value, "  ", my_bst.root.left.left.right.value)

print()
print(my_bst.r_contains(91))
print()
print("closest value to 17.5 is ", my_bst.closest_value(17.5))


