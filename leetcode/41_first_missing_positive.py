# 2022/08/16
# 超过了87.15%
# 执行用时: 132 ms
# 内存消耗: 44.6 MB
class Solution:
    @staticmethod
    def firstMissingPositive(nums):
        # initiate a list in size of nums_size + 1, indicating as a positive ingeter list
        nums_size = len(nums)
        mark_list = [0] * (nums_size + 1)

        # loop nums, if meet conditions and make mark list corresponding index to 1
        for value in nums:
            if nums_size + 1 > value > 0:
                mark_list[v - 1] = 1

        # loop mark list, find first 0 element, which index represents first missing positive
        for i in range(len(mark_list)):
            if mark_list[i] == 0:
                return i + 1
