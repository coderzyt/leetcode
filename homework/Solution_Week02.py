class Solution(object):
    
    def isAnagram(self, s: str, t: str) -> bool:
        if s is None or t is None:
            return False
        if s == "" and t == "":
            return True
        hashMap = {}
        for i in s:
            if hashMap.get(i) is None:
                hashMap.setdefault(i, 1)
            else:
                value = hashMap.get(i) + 1
                hashMap.__setitem__(i, value)
        for j in t:
            if hashMap.get(j) is None:
                return False
            value = hashMap.get(j) - 1
            hashMap.__setitem__(j, value)
        for i in s:
            if hashMap.get(i) != 0:
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    s = 'anagram'
    t = 'nagaram'
    print(solution.isAnagram(s, t))
    print(s.index('n'))
    print(s.find('a'))
    print(s.replace('a', ''))
    s.__contains__('a')