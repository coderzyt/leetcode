class MyStack(object):

    def __init__(self):
        self.stackMin = list()
        self.stackData = list()
    
    def pop(self) -> int:
        if not self.stackData and not self.stackMin:
            self.stackMin.pop()
            return self.stackData.pop()
        else:
            return None

    def push(self, num: int):


        




if __name__ == "__main__":
    pass