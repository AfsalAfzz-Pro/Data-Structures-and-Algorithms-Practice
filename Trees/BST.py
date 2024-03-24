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
            if temp.value == new_node.value:
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

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def delete(self, value):
        temp = self.root
        prev = self.root
        while temp is not None:
            if value < temp.value:
                prev = temp
                temp = temp.left
            elif value > temp.value:
                prev = temp
                temp = temp.right
            else:
                if prev.right == temp:
                    prev.right = None
                    return temp
                elif prev.left == temp:
                    prev.left = None
                    return temp
        return False

    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results


my_BST = BinarySearchTree()
my_BST.insert(2)
my_BST.insert(1)
my_BST.insert(3)
my_BST.insert(4)


print("Root: ", my_BST.root.value)
print("Root.Left: ", my_BST.root.left.value)
print("Root.Right: ", my_BST.root.right.value)
print("Root.Right.Right: ", my_BST.root.right.right.value)

print()
print(my_BST.contains(4))
print(my_BST.contains(5))

print(my_BST.BFS())

print(my_BST.delete(4).value)
print()
print(my_BST.BFS())

print(my_BST.contains(4))
