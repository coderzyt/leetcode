from homework.Week_02.TreeNode import TreeNode


class TreeNodeTraveral(object):

    def inorder(self, root: TreeNode) -> list:
        WHITE, BLACK = 0, 1
        result = []
        storeStack = [(WHITE, root)]
        while storeStack:
            color, node = storeStack.pop()
            if node is None:
                continue
            if color == WHITE:
                storeStack.append(BLACK, node.right)
                storeStack.append(WHITE, node)
                storeStack.append(BLACK, node.left)
            else:
                result.append(node.val)
        return result

    def inorder_recursion(self, root: TreeNode) -> list:
        result = []
        self.inorder_helper(root, result)
        return result

    def inorder_helper(self, root: TreeNode, result: list) -> list:
        if root is not None:
            if root.left is not None:
                self.inorder_recursion(root.left, result)
            result.append(root.val)
            if root.right is not None:
                self.inorder_recursion(root.right, result)

    def preorder(self, root: TreeNode) -> list:
        WHITE, BLACK = 0, 1
        result = []
        storeStack = [(WHITE, root)]
        while storeStack:
            color, node = storeStack.pop()
            if node is None:
                continue
            if color == WHITE:
                storeStack.append(BLACK, node.right)
                storeStack.append(BLACK, node.left)
                storeStack.append(WHITE, node)
            else:
                result.append(node.val)
        return result

    def preorder_recursion(self, root: TreeNode) -> list:
        result = []
        self.preorder_helper(root, result)
        return result

    def preorder_helper(self, root: TreeNode, result: list) -> list:
        if root is not None:
            result.append(root.val, result)
            if root.left is not None:
                self.preorder_recursion(root.left, result)
            if root.right is not None:
                self.preorder_recursion(root.right, result)

    def posorder(self, root: TreeNode) -> list:
        WHITE, BLACK = 0, 1
        result = []
        storeStack = [(WHITE, root)]
        while storeStack:
            color, node = storeStack.pop()
            if node is None:
                continue
            if color == WHITE:
                storeStack.append(WHITE, node)
                storeStack.append(BLACK, node.right)
                storeStack.append(BLACK, node.left)
            else:
                result.append(node.val)
        return result

    def posorder_recursion(self, root: TreeNode) -> list:
        result = []
        self.posorder_helper(root, result)
        return result

    def posorder_helper(self, root: TreeNode, result: list) -> list:
        if root is not None:
            if root.left is not None:
                self.posorder_helper(root.left, result)
            if root.right is not None:
                self.posorder_helper(root.right, result)
            result.append(root.val)
