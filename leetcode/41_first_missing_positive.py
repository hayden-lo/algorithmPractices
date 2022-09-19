# 2022/08/16
# 超过了87.15%
# 执行用时: 132 ms
# 内存消耗: 44.6 MB
class Solution:
    @staticmethod
    def firstMissingPositive(nums):
        # initiate a list in size of nums_size + 1, indicating as a positive integer list
        nums_size = len(nums)
        mark_list = [0] * (nums_size + 1)

        # loop nums, if meet conditions and make mark list corresponding index to 1
        for value in nums:
            if nums_size + 1 > value > 0:
                mark_list[value - 1] = 1

        # loop mark list, find first 0 element, which index represents first missing positive
        for i in range(len(mark_list)):
            if mark_list[i] == 0:
                return i + 1


if __name__ == '__main__':
    s = Solution
    # case 1
    nums_ins = [1, 2, 0]
    exp_res = 3
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.firstMissingPositive(nums_ins)}")

    # case 2
    nums_ins = [3, 4, -1, 1]
    exp_res = 2
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.firstMissingPositive(nums_ins)}")

    # case 3
    nums_ins = [7, 8, 9, 11, 12]
    exp_res = 1
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.firstMissingPositive(nums_ins)}")
