def invert_binary_tree(root):
    """Swap left and right children
    """
    if not root:
        return
    root.left, root.right = invert_binary_tree(root.right), invert_binary_tree(
        root.left)
    return root


def max_depth_binary_tree(root):
    """Take the max value between
    the depth of the left child and right child
    """
    if not root:
        return 0
    return 1 + max(max_depth_binary_tree(root.left),
                   max_depth_binary_tree(root.right))


def diameter_binary_tree(root):
    """Take the max diameter between
    the left and right child and add 1 to it.
    """
    res = [0]

    def dfs(node):
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)
        res[0] = max(res[0], left, right)
        return 1 + max(left, right)

    dfs(root)

    return res


def balance_binary_tree(root):
    """A binary tree is balanced if the diff of depth
    between the left and right child is not > 1
    """
    if not root:
        return True

    def dfs(node):
        if not node:
            return [True, 0]

        left = dfs(node.left)
        right = dfs(node.right)

        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return balanced, 1 + max(left, right)

    return dfs(root)[0]
