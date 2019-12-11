# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, y):
        self.val = x
        self.next = y

class Solution:
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

node1 = ListNode(1, None)
node2 = ListNode(2, node1)
node3 = ListNode(3, node2)
node4 = ListNode(4, node3)
node5 = ListNode(5, node4)

solution = Solution()
solution.deleteNode(node3)
print(node3)

