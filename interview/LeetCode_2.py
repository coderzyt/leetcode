# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        sumNode = result
        flag = 0
        while l1.val >= 0 or l2.val >= 0:
            sumNum = (l1.val if l1.val >= 0 else 0) + (l2.val if l2.val >= 0 else 0) + flag
            flag = sumNum // 10
            sumNode.val = sumNum % 10
            l1 = l1.next if l1.next else ListNode(-1)
            l2 = l2.next if l2.next else ListNode(-1)
            if l1.val >= 0 or l2.val >= 0 or flag:
                sumNode.next = ListNode(0)
                sumNode = sumNode.next
        if flag == 1:
            sumNode.val = 1
        return result


if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(5)
    l1.next = ListNode(6)
    l1.next.next = ListNode(4)

    l2 = ListNode(2)
    l2.next = ListNode(4)
    l2.next.next = ListNode(3)

    solution.addTwoNumbers(l1, l2)