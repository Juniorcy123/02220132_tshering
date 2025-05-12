class Node:
    def __init__(self, value, color='red'):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = color  # 'red' or 'black'

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, color='black')  # Sentinel leaf node
        self.root = self.NIL
    
    def insert(self, value):
        new_node = Node(value)
        new_node.left = self.NIL
        new_node.right = self.NIL
        
        parent = None
        current = self.root
        
        # Find the appropriate parent
        while current != self.NIL:
            parent = current
            if new_node.value < current.value:
                current = current.left
            else:
                current = current.right
        
        new_node.parent = parent
        
        if parent is None:
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node
        
        # If new node is root, color it black and return
        if new_node.parent is None:
            new_node.color = 'black'
            return
        
        # If grandparent is None, return
        if new_node.parent.parent is None:
            return
        
        self._fix_insert(new_node)
    
    def _fix_insert(self, node):
        while node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    # Case 1: Uncle is red
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    # Case 2: Uncle is black and node is right child
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    # Case 3: Uncle is black and node is left child
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    # Case 1: Uncle is red
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    # Case 2: Uncle is black and node is left child
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    # Case 3: Uncle is black and node is right child
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._left_rotate(node.parent.parent)
            
            if node == self.root:
                break
        
        self.root.color = 'black'
    
    def delete(self, value):
        node = self._search_node(value)
        if node == self.NIL:
            return
        
        original_color = node.color
        if node.left == self.NIL:
            x = node.right
            self._transplant(node, node.right)
        elif node.right == self.NIL:
            x = node.left
            self._transplant(node, node.left)
        else:
            min_node = self._minimum(node.right)
            original_color = min_node.color
            x = min_node.right
            if min_node.parent == node:
                x.parent = min_node
            else:
                self._transplant(min_node, min_node.right)
                min_node.right = node.right
                min_node.right.parent = min_node
            
            self._transplant(node, min_node)
            min_node.left = node.left
            min_node.left.parent = min_node
            min_node.color = node.color
        
        if original_color == 'black':
            self._fix_delete(x)
    
    def _fix_delete(self, node):
        while node != self.root and node.color == 'black':
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == 'red':
                    # Case 1: Sibling is red
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self._left_rotate(node.parent)
                    sibling = node.parent.right
                
                if sibling.left.color == 'black' and sibling.right.color == 'black':
                    # Case 2: Both sibling's children are black
                    sibling.color = 'red'
                    node = node.parent
                else:
                    if sibling.right.color == 'black':
                        # Case 3: Sibling's right child is black
                        sibling.left.color = 'black'
                        sibling.color = 'red'
                        self._right_rotate(sibling)
                        sibling = node.parent.right
                    
                    # Case 4: Sibling's right child is red
                    sibling.color = node.parent.color
                    node.parent.color = 'black'
                    sibling.right.color = 'black'
                    self._left_rotate(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == 'red':
                    # Case 1: Sibling is red
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self._right_rotate(node.parent)
                    sibling = node.parent.left
                
                if sibling.right.color == 'black' and sibling.left.color == 'black':
                    # Case 2: Both sibling's children are black
                    sibling.color = 'red'
                    node = node.parent
                else:
                    if sibling.left.color == 'black':
                        # Case 3: Sibling's left child is black
                        sibling.right.color = 'black'
                        sibling.color = 'red'
                        self._left_rotate(sibling)
                        sibling = node.parent.left
                    
                    # Case 4: Sibling's left child is red
                    sibling.color = node.parent.color
                    node.parent.color = 'black'
                    sibling.left.color = 'black'
                    self._right_rotate(node.parent)
                    node = self.root
        
        node.color = 'black'
    
    def search(self, value):
        return self._search_node(value) != self.NIL
    
    def _search_node(self, value):
        current = self.root
        while current != self.NIL and value != current.value:
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return current
    
    def get_black_height(self):
        if self.root == self.NIL:
            return 0
        
        height = 0
        node = self.root
        while node != self.NIL:
            if node.color == 'black':
                height += 1
            node = node.left  # All paths have same black height, so we can follow any path
        return height
    
    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.left = x
        x.parent = y
    
    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        
        x.right = y
        y.parent = x
    
    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    
    def _minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node
    
rb_tree = RedBlackTree()
rb_tree.insert(10)
rb_tree.insert(20)
rb_tree.insert(30)
print(rb_tree.get_black_height())  # Should return appropriate black height (likely 2)
print(rb_tree.search(20))  # True
rb_tree.delete(20)
print(rb_tree.search(20))  # False