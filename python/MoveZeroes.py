class MoveZeroes(object):

    def move_zeroes(self, nums: list) -> None:
        if nums is None or nums.__len__() < 2:
            return None
        length = nums.__len__()
        index = 0
        for i in range(0, length):
            if nums[i] != 0:
                nums[index] = nums[i]
                index = index + 1
        while index < length:
            nums[index] = 0
            index = index + 1
        print(nums)


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    moveZeros = MoveZeroes()
    moveZeros.move_zeroes(nums)
