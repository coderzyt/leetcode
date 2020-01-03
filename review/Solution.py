from typing import List

from python.TreeNode import TreeNode


class Solution(object):
    
    def binaryTreeInorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        WHITE, GREY = 0, 1
        stack = [(WHITE, root)]
        result = []
        while stack:
            color, node = stack.pop()
            if node is None:
                continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GREY, node))
                stack.append((WHITE, node.left))
            else:
                result.append(node.val)
        return result

    def binaryTreePreorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        WHITE, GREY = 0, 1
        stack = [(WHITE, root)]
        result = []
        while stack:
            color, node = stack.pop()
            if node is None:
                continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
                stack.append((GREY, node))
            else:
                result.append(node.val)
        return result

    def binaryTreePosorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        WHITE, GREY = 0, 1
        stack = [(WHITE, root)]
        result = []
        while stack:
            color, node = stack.pop()
            if node is None:
                continue
            if color == WHITE:
                stack.append((GREY, node))
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
            else:
                result.append(node.val)
        return result


if __name__ == "__main__":
    pass