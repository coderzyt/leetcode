from python.ListNode import ListNode


class SwapPairs(object):

    def swap_pairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        cur = head
        first = None
        second = None
        while second is not None:
            first = cur
            second = cur.next
            next_first = second.next
            next_second = second.next.next
            second.next = first
            first.next = next_second
            cur = next_first

        return first


if __name__ == "__main__":
    node1 = ListNode(1, None)
    node2 = ListNode(2, node1)
    node3 = ListNode(3, node2)
    node4 = ListNode(4, node3)
    node5 = ListNode(5, node4)
    node6 = ListNode(6, node5)
    swapPairs = SwapPairs()
    print(swapPairs.swap_pairs(node6))
