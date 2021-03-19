from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        first = ListNode(0)
        first.next = head
        pre = first
        end = first

        while end.next:
            count = k
            while count and end:
                end = end.next
                count -= 1
            if not end:
                break
            start = pre.next
            next = end.next
            end.next = None
            pre.next = self.reverse(start)
            start.next = next
            pre = start
            end = pre
        return first.next
    
    def reverse(self, head):
        pre, cur = None, head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

