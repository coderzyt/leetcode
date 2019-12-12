class ThreeNumSum(object):
    
    # 无法去重
    def three_num_sum(self, nums: list) -> list:

        if nums is None or nums.__len__() < 3:
            return []

        length = nums.__len__()
        index = 0
        result = []
        for index in range(0, length):
            i = 0
            while i < length:
                if i != index:
                    j = 0
                    while j < length:
                        if j != index and j != i:
                            if nums[i] + nums[j] == - (nums[index]):
                                cur = [nums[i], nums[j], nums[index]]
                                if not result.__contains__(cur):
                                    result.append(cur)
                        j = j + 1
                i = i + 1
        
        return result

    def three_num_sum2(self, nums: list) -> list:
        if not nums or len(nums) < 3:
            return []
        length = len(nums)
        nums.sort()
        result = []
        for index in range(0, length):
            if nums[index] > 0:
                return result
            # 去重
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            L = index + 1
            R = length - 1
            while R > L:
                sum = nums[L] + nums[R] + nums[index]
                if sum == 0:
                    result.append([nums[L], nums[R], nums[index]])
                    while L < R and nums[L] == nums[L + 1]:
                        L = L + 1
                    while L < R and nums[R] == nums[R - 1]:
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif sum < 0:
                    L = L + 1
                else:
                    R = R - 1
        return result

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    threeNumSum = ThreeNumSum()
    result = threeNumSum.three_num_sum2(nums)
    print(result)