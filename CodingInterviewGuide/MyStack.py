class MyStack(object):

    def __init__(self):
        self.stackMin = list()
        self.stackData = list()
    
    def pop(self) -> int:
        if not self.stackData and not self.stackMin:
            self.stackMin.pop(-1)
            return self.stackData.pop(-1)
        else:
            return None

    def push(self, num: int):
        if self.stackData.__len__() == 0:
            self.stackData.append(num)
            self.stackMin.append(num)
        else:
            self.stackData.append(num)
            last = self.stackMin.pop(-1)
            self.stackMin.append(last)
            if num >= last:
                self.stackMin.append(last)
            else:
                self.stackMin.append(num)

    def getMin(self) -> int:
        min = self.stackMin.pop(-1)
        self.stackMin.append(min)
        return min


if __name__ == "__main__":
    pass