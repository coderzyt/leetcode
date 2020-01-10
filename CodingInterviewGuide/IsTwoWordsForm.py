class Solution(object):

    def isTwoWordsForm(self, str1: str, str2: str) -> bool:
        if not str1 or not str2:
            return False
        if len(str1) != len(str2):
            return False

        hashMap = {}
        for i in range(len(str1)):
            if not hashMap.get(str1[i]):
                hashMap[str1[i]] = 1
            else:
                hashMap[str1[i]] = hashMap[str1[i]] + 1
            if not hashMap.get(str2[i]):
                hashMap[str2[i]] = -1
            else:
                hashMap[str2[i]] = hashMap[str2[i]] - 1

        for value in hashMap.values():
            if value != 0:
                return False
        return True



if __name__ == '__main__':
    str1 = '123'
    str2 = '321'
    solution = Solution()
    print(solution.isTwoWordsForm(str1, str2))