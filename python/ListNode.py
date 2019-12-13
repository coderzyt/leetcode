class ListNode(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val) + ", " + str(self.next)
    
    def setNext(self, next):
        self.next = next