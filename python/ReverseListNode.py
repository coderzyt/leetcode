from python.ListNode import ListNode

class ReverseListNode(object):
    
    def reverse_list_node(self, head: ListNode):
        if head is None or head.next is None:
            return  head
        pre = None
        cur = head
        next = None
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        
        return pre

if __name__ == "__main__":
    node1 = ListNode(1, None)
    node2 = ListNode(2, node1)
    node3 = ListNode(3, node2)
    node4 = ListNode(4, node3)
    node5 = ListNode(5, node4)
    reverseListNode = ReverseListNode()
    print(reverseListNode.reverse_list_node(node5))