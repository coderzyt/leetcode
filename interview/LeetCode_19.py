# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # node_no = 0
        # node = head
        # while node is not None:
        #     node = node.next
        #     node_no += 1
        # node_no -= n + 1

        # node = head
        # if node_no == -1:
        #     head = head.next
        # else:
        #     while(node_no):
        #         node = node.next
        #         node_no -= 1
        #     node.next = node.next.next
        # return head
        node = head
        length = 0
        while node:
            node = node.next
            length += 1
        index = length - n - 1
        node = head
        if index == -1:
            return head.next
        while index:
            node = node.next
            index -= 1
        node.next = node.next.next
        return head

    
if __name__ == "__main__":
    node = ListNode(2)
    node.next = ListNode(3)
    node.next.next = ListNode(4)
    node.next.next.next = ListNode(5)
    solution = Solution()
    solution.removeNthFromEnd(node, 2)
