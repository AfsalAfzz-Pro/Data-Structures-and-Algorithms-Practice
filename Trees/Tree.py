import matplotlib.pyplot as plt


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self, value):
        new_node = Node(value)
        self.root = new_node
        self.height = 1

    def insert_node(self, value):
        new_node = Node(value)
        current = self.root
        while True:
            if new_node.value < current.value:
                if current.left is None:
                    current.left = new_node
                    self.height += 1
                    return True
                else:
                    current = current.left
            if new_node.value > current.value:
                if current.right is None:
                    current.right = new_node
                    self.height += 1
                    return True
                else:
                    current = current.right

    def display_in_order(self, node):
        if node is not None:
            self.display_in_order(node.left)
            print(node.value, end=" ")
            self.display_in_order(node.right)

    def display_tree(self):
        self.display_in_order(self.root)

    def _plot_tree(self, node, x, y, dx, dy, ax):
        if node:
            ax.text(x, y, str(node.value), style='oblique', ha='center', va='center',
                    bbox=dict(facecolor='blue', alpha=0.5, edgecolor='blue'))
            if node.left:
                ax.plot([x, x - dx], [y - dy, y - 1], 'k-', linewidth=1.5)
                self._plot_tree(node.left, x - dx, y - 1, dx / 2, dy, ax)
            if node.right:
                ax.plot([x, x + dx], [y - dy, y - 1], 'k-', linewidth=1.5)
                self._plot_tree(node.right, x + dx, y - 1, dx / 2, dy, ax)

    def display_tree_visual(self):
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.set_aspect('equal')
        ax.axis('off')
        self._plot_tree(self.root, 0.5, 1, 0.5, 1, ax)
        plt.show()

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


my_BST = BST(8)
my_BST.insert_node(7)
my_BST.insert_node(9)
my_BST.insert_node(6)
my_BST.insert_node(5)
my_BST.insert_node(10)
my_BST.insert_node(11)
my_BST.insert_node(9.5)
print(my_BST.BFS())
my_BST.display_tree()
# my_BST.display_tree_visual()

