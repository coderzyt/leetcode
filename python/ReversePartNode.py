from python.Node import Node


class ReversePartNode(object):
    def reverse_part_node(self, head: Node, begin: int, end: int) -> Node:
        if head is None or head.next is None:
            return head
        cur = head
        bPre = None
        eNext = None
        len = 0
        while cur is not None:
            len = len + 1
            bPre = cur if len == begin - 1 else bPre
            eNext = cur if len == end + 1 else eNext
            cur = cur.next
        if begin > end or begin < 1 or end > len:
            return head
        node1 = head if bPre is None else bPre.next
        node2 = node1.next
        node1.next = eNext
        next = None
        while node2 != eNext:
            next = node2.next
            node2.next = node1
            node1 = node2
            node2 = next
        if bPre is not None:
            bPre.next = node1
            return head

        return node1


if __name__ == "__main__":
    node6 = Node(6, None)
    node5 = Node(5, node6)
    node4 = Node(4, node5)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)
    reversePartNode = ReversePartNode()
    print(reversePartNode.reverse_part_node(node1, 2, 5))
