import collections


class Solution(object):

    def twoSum(self, nums: list, target: int) -> list:
        hashMap = collections.defaultdict(int)
        for i in range(len(nums)):
            if hashMap.__contains__(target - nums[i]):
                return [i, hashMap.get(target - nums[i])]
            hashMap[nums[i]] = i
        return []

    def groupAnagrams(self, strs: list) -> list:
        hashMap = collections.defaultdict(list)
        for str in strs:
            count = [0] * 26
            for char in str:
                count[ord(char) - ord('a')] += 1
            hashMap[tuple(count)].append(str)
        return hashMap.values()

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            s_mem = s[i]
            t_mem = t[i]
            count[ord(s_mem) - ord('a')] += 1
            count[ord(t_mem) - ord('a')] -= 1
        for i in range(len(count)):
            if count[i] != 0:
                return False
        return True


# if __name__ == "__main__":
#     solution = Solution()
#     s = 'anagram'
#     t = 'nagaram'
#     print(solution.isAnagram(s, t))
#     strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
#     print(solution.groupAnagrams(strs))
#     nums = [2, 7, 11, 15]
#     print(solution.twoSum(nums, 9))
