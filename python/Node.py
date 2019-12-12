class Node(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value) + ", " + str(self.next)