from collections import deque
from python.ListNode import ListNode


class Solution(object):

    # def trap(self, height: list) -> int:

    def maxSlidingWindow2(self, nums: list, k: int) -> list:
        # base cases
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        def clean_deque(i):
            # remove indexes of elements not from sliding window
            if deq and deq[0] == i - k:
                deq.popleft()

            # remove from deq indexes of all elements
            # which are smaller than current element nums[i]
            # print(deq[-1])
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        # init deque and output
        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        # build output
        for i in range(k, n):
            clean_deque(i)
            deq.append(i)
            output.append(nums[deq[0]])
        return output

    def maxSlidingWindow(self, nums: list, k: int) -> list:
        if nums is None:
            return None
        length = len(nums)
        if k < 2:
            return nums
        result = []
        for i in range(0, length - k + 1):
            result.append(max(nums[i:i + k]))
        return result


    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        nums1[m:m + n] = nums2
        nums1.sort()

    def plusOne(self, digits: list) -> list:
        if digits is None:
            return None
        length = len(digits)
        i = length - 1
        while i >= 0:
            digits[i] = digits[i] + 1
            digits[i] = digits[i] % 10
            if digits[i] > 0:
                return digits
            i = i - 1
        result = [1]
        result[1:1+length] = digits
        return result

    def twoSum(self, nums: list, target: int) -> list:
        if nums is None:
            return None
        length = len(nums)
        if length == 1:
            return []
        hashMap = {}
        for i, num in enumerate(nums):
            key = hashMap.get(target - num)
            if key is not None:
                return [i, key]
            hashMap[num] = i
        return []

    def moveZeros(self, nums: list) -> list:
        if nums is None:
            return None
        length = len(nums)
        if length == 1:
            return nums
        index = 0
        for i in range(length):
            if nums[i] != 0:
                nums[index] = nums[i]
                if index != i:
                    nums[i] = 0
                index = index + 1
        return nums

    def removeDuplicates(self, nums: list) -> int:
        if nums is None or len(nums) < 2:
            return len(nums)
        length = len(nums)
        index = 0
        for i in range(1, length):
            if nums[index] != nums[i]:
                index = index + 1
                nums[index] = nums[i]
            else:
                pass
        return index + 1

    # def rotate(self, nums: list, k: int) -> None:
    #     if nums is None:
    #         return None
    #     length = len(nums)
    #     if length > 1:
    #         remainder = k % length
    #         for i in range(length):

    class MyCircularDeque:

        def __init__(self, k: int):
            """
            Initialize your data structure here. Set the size of the deque to be k.
            """

        def insertFront(self, value: int) -> bool:
            """
            Adds an item at the front of Deque. Return true if the operation is successful.
            """

        def insertLast(self, value: int) -> bool:
            """
            Adds an item at the rear of Deque. Return true if the operation is successful.
            """

        def deleteFront(self) -> bool:
            """
            Deletes an item from the front of Deque. Return true if the operation is successful.
            """

        def deleteLast(self) -> bool:
            """
            Deletes an item from the rear of Deque. Return true if the operation is successful.
            """

        def getFront(self) -> int:
            """
            Get the front item from the deque.
            """

        def getRear(self) -> int:
            """
            Get the last item from the deque.
            """

        def isEmpty(self) -> bool:
            """
            Checks whether the circular deque is empty or not.
            """

        def isFull(self) -> bool:
            """
            Checks whether the circular deque is full or not.
            """



if __name__ == '__main__':
    solution = Solution()

    # nums = [0,0,1,1,1,2,2,3,3,4]
    # print(solution.removeDuplicates(nums))
    # print(solution.moveZeros([3,2,4]))
    # print(solution.twoSum([3,2,4]))

    # print(12 % 10)
    # print(solution.plusOne([9]))
    #
    # solution.merge([1,2,3,0,0,0], 6, [2,5,6], 3)
    #
    # l1 = ListNode(1, None)
    # l2 = ListNode(2, None)
    # print(solution.mergeTwoLists(l1, l2))

    print(solution.maxSlidingWindow2([1,3,-1,-3,5,3,6,7], k=3))