class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        print("Created new Binary Tree")
        print(f"Root: {self.root}")

    def height(self):
        def _height(node):
            if not node:
                return 0
            return 1 + max(_height(node.left), _height(node.right))
        height = _height(self.root)
        print(f"Tree Height: {height}")
        return height

    def size(self):
        def _size(node):
            if not node:
                return 0
            return 1 + _size(node.left) + _size(node.right)
        size = _size(self.root)
        print(f"Total Nodes: {size}")
        return size

    def count_leaves(self):
        def _count_leaves(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            return _count_leaves(node.left) + _count_leaves(node.right)
        leaves = _count_leaves(self.root)
        print(f"Leaf Nodes Count: {leaves}")
        return leaves

    def is_full_binary_tree(self):
        def _is_full(node):
            if not node:
                return True
            if not node.left and not node.right:
                return True
            if node.left and node.right:
                return _is_full(node.left) and _is_full(node.right)
            return False
        result = _is_full(self.root)
        print(f"Is Full Binary Tree: {result}")
        return result

    def is_complete_binary_tree(self):
        def _count_nodes(node):
            if not node:
                return 0
            return 1 + _count_nodes(node.left) + _count_nodes(node.right)
        
        def _is_complete(node, index, node_count):
            if not node:
                return True
            if index >= node_count:
                return False
            return (_is_complete(node.left, 2 * index + 1, node_count) and 
                    _is_complete(node.right, 2 * index + 2, node_count))
        
        if not self.root:
            print("Is Complete Binary Tree: True")
            return True
        node_count = _count_nodes(self.root)
        result = _is_complete(self.root, 0, node_count)
        print(f"Is Complete Binary Tree: {result}")
        return result
if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    tree = BinaryTree(node1)
    tree.height()
    tree.size()
    tree.count_leaves()
    tree.is_full_binary_tree()
    tree.is_complete_binary_tree()
