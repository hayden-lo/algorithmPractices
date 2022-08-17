# 2020/10/29
# 超过了96%
# 执行用时: 32 ms
# 内存消耗: 14.4 MB
class Solution1:
    @staticmethod
    def twoSum(nums, target):
        hash_table = {}
        for i in range(len(nums)):
            reverse = target - nums[i]
            if reverse not in hash_table:
                hash_table[nums[i]] = i
            else:
                return [hash_table[reverse], i]


# 2021/02/23
# 超过了41%
# 执行用时: 44 ms
# 内存消耗: 14.8 MB
class Solution2:

    @staticmethod
    def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
