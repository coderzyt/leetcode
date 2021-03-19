from python.ListNode import ListNode
from python.Node import Node


class ReverseKGroup(object):

    def reverseKGroup(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:  # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                jump.next, jump, l = pre, l, r  # connect two k-groups
            else:
                return dummy.next

    def reverse_node(self, head: Node) -> Node:
        if head is None or head.next is None:
            return head

        pre = None
        next = None
        cur = head
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    def reverse_k_group(self, head: Node, k: int) -> Node:
        if head is None or head.next is None:
            return head
        cur = head
        pre = None
        for i in range(0, k):
            if cur is not None:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
        head.next = cur
        return pre


if __name__ == "__main__":
    node6 = Node(6, None)
    node5 = Node(5, node6)
    node4 = Node(4, node5)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)
    reverseKGroup = ReverseKGroup()
    result = reverseKGroup.reverseKGroup(node1, 2)
    print(result)
    # result = reverseKGroup.reverse_node(node1)
    # print(result)
