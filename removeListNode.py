# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, y):
        self.val = x
        self.next = y

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        pre = head
        cur = head.next
        while cur:
            if cur.val == val:
                cur = cur.next
                pre.next = cur
            else:
                pre = cur
                cur = cur.next
        return head

node1 = ListNode(1, None)
node2 = ListNode(2, node1)
node3 = ListNode(3, node2)
node4 = ListNode(4, node3)
node5 = ListNode(5, node4)

solution = Solution()
result = solution.removeElements(node5, 3)
print(result)