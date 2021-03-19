from python.ListNode import ListNode


class ListNodeHasCycle(object):

    def hasCycle2(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        cur = head
        first = cur.next
        second = cur.next.next
        while second is not None:
            if first == second:
                return True
            if first.next is not None and second.next is not None and second.next.next is not None:
                first = first.next
                second = second.next.next
            else:
                return False
        return False


if __name__ == "__main__":
    node1 = ListNode(1, None)
    node2 = ListNode(2, node1)
    node3 = ListNode(3, node2)
    node4 = ListNode(4, node3)
    node5 = ListNode(5, node4)

    # node1.__setNext__(node3)

    hasCycle = ListNodeHasCycle()
    print(hasCycle.hasCycle(node5))
