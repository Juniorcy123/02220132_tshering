# AVL Tree Implementation
# Implemented by: [Your Name]
# Partner: [Partner's Name]

class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    def _height(self, node):
        return node.height if node else 0
    
    def _balance(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0
    
    def _update_height(self, node):
        if node:
            node.height = max(self._height(node.left), self._height(node.right)) + 1
    
    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        self._update_height(y)
        self._update_height(x)
        return x
    
    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        self._update_height(x)
        self._update_height(y)
        return y
    
    def insert(self, value):
        def _insert(node, value):
            if not node:
                return AVLNode(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            elif value > node.value:
                node.right = _insert(node.right, value)
            else:
                return node
            self._update_height(node)
            balance = self._balance(node)
            if balance > 1:
                if value < node.left.value:
                    return self._right_rotate(node)
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)
            if balance < -1:
                if value > node.right.value:
                    return self._left_rotate(node)
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)
            return node
        self.root = _insert(self.root, value)
    
    def delete(self, value):
        def _delete(node, value):
            if not node:
                return node
            if value < node.value:
                node.left = _delete(node.left, value)
            elif value > node.value:
                node.right = _delete(node.right, value)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                temp = self._min_node(node.right)
                node.value = temp.value
                node.right = _delete(node.right, temp.value)
            self._update_height(node)
            balance = self._balance(node)
            if balance > 1:
                if self._balance(node.left) >= 0:
                    return self._right_rotate(node)
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)
            if balance < -1:
                if self._balance(node.right) <= 0:
                    return self._left_rotate(node)
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)
            return node
        self.root = _delete(self.root, value)
    
    def _min_node(self, node):
        while node.left:
            node = node.left
        return node
    
    def search(self, value):
        node = self.root
        while node and node.value != value:
            node = node.left if value < node.value else node.right
        return node
    
    def get_height(self):
        return self._height(self.root)
    
    def is_balanced(self):
        def _check(node):
            if not node:
                return True, 0
            left_ok, left_h = _check(node.left)
            right_ok, right_h = _check(node.right)
            balanced = left_ok and right_ok and abs(left_h - right_h) <= 1
            return balanced, max(left_h, right_h) + 1
        return _check(self.root)[0]
    
    def print_tree(self):
        def _print(node):
            if not node:
                return
            _print(node.left)
            print(node.value, end=" ")
            _print(node.right)
        _print(self.root)
        print()

if __name__ == "__main__":
    avl_tree = AVLTree()
    avl_tree.insert(10)
    avl_tree.insert(20)
    avl_tree.insert(30)
    print(avl_tree.is_balanced())
    print(avl_tree.get_height())
    print("Tree (in-order):", end=" ")
    avl_tree.print_tree()