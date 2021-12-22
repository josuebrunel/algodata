#### [ bst.py ]( bst.py )

```python

class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.value} [{self.left}, {self.right}]"

    def insert(self, val):
        if not val:
            return False
        if not self.value:
            self.value = val
            return True
        if val <= self.value:
            if self.left:
                return self.left.insert(val)
            self.left = Node(val)
        else:
            if self.right:
                return self.right.insert(val)
            self.right = Node(val)
        return True

    def inorder(self):
        values = []
        stack = []
        current = self
        while current or stack:
            if current:
                stack.append(current)
                current = current.right
            else:
                current = stack.pop()
                values.append(current.value)
                current = current.left
        return values



if __name__ == "__main__":
    root = Node(5)
    root.insert(3)
    root.insert(7)
    print(root)
    root.insert(2)
    print(root)
    root.insert(6)
    root.insert(4)
    print(root)
    print(root.inorder())


```



