class MaxArea(object):
    def getMaxArea(self, height: list) -> int:
        length = height.__len__()
        max = 0
        for i in range(0, length):
            for j in range(i + 1, length):
                cur = (height[i] if height[i] < height[j] else height[j]) * (j - i)
                max = cur if cur >= max else max
        return max

    def getMaxArea2(self, height: list) -> int:
        length = height.__len__()
        i, j = 0, length - 1
        max = 0
        while i != j:
            if (height[i] <= height[j]):
                cur = height[i] * (j - i)
                max = cur if cur > max else max
                i = i + 1
            else:
                cur = height[j] * (j - i)
                max = cur if cur > max else max
                j = j - 1
        return max


if __name__ == "__main__":
    param = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    maxArea = MaxArea()
    print(maxArea.getMaxArea2(param))
