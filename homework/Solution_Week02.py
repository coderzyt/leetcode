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

    def groupAnagrams2(self, strs: list) -> list:
        result = {}
        for str in strs:
            key = tuple(sorted(str))
            result[key] = result.get(key, []) + [str]
        return result.values()

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        for i in range(len(count)):
            if count[i] != 0:
                return False
        return True

    def isAnagram2(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


if __name__ == "__main__":
    solution = Solution()
#     s = 'anagram'
#     t = 'nagaram'
#     print(solution.isAnagram(s, t))
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams2(strs))
#     nums = [2, 7, 11, 15]
#     print(solution.twoSum(nums, 9))
