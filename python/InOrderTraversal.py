from typing import List
from python.TreeNode import TreeNode


class InOrderTraversal(object):

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GREY = 0, 1
        result = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None:
                continue
            if color == WHITE:
                stack.append(WHITE, node.right)
                stack.append(GREY, node)
                stack.append(WHITE, node.left)
            else:
                result.append(node.val)
        return result
