# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return None
        WHITE, GREY = 0, 1
        stack = [(WHITE, root)]
        data = ""
        while stack:
            color, node = stack.pop()
            if not node:
                data += 'None,'
                continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
                stack.append((GREY, node))
            else:
                data += str(node.val) + ','
        return data


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(nodes):
            if nodes[0] == 'None':
                nodes.pop(0)
                return None
                
            root = TreeNode(nodes[0])
            nodes.pop(0)
            root.left = helper(nodes)
            root.right = helper(nodes)
            return root
        
        if not data:
            return None
        root = helper(data.split(','))
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))