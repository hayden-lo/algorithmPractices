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


if __name__ == '__main__':
    s = Solution1
    # case 1
    nums_ins = [2, 7, 11, 15]
    target_ins = 9
    exp_res = [0, 1]
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.twoSum(nums_ins, target_ins)}")

    # case 2
    nums_ins = [3, 2, 4]
    target_ins = 6
    exp_res = [1, 2]
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.twoSum(nums_ins, target_ins)}")

    # case 3
    nums_ins = [3, 3]
    target_ins = 6
    exp_res = [0, 1]
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.twoSum(nums_ins, target_ins)}")
