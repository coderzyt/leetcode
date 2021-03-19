class Solution(object):

    def isRotation(self, str1: str, str2: str) -> bool:
        if not str1 or not str2:
            return False
        if len(str1) != len(str2):
            return False

        newStr = str2 + str2
        if newStr.__contains__(str1):
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isRotation('12345', '23451'))