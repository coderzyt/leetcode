class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __setNext__(self, next):
        self.next = next
    
    def __str__(self):
        return str(self.val) + ", " + str(self.next)