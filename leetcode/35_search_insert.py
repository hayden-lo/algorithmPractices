# 2022/08/17
# 超过了89.39%
# 执行用时: 32 ms
# 内存消耗: 15.6 MB
class Solution1:
    @staticmethod
    # iterative method
    def searchInsert(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left


class Solution2:
    @staticmethod
    # recursive method
    def searchInsert(nums, target, left, right):
        if left >= right:
            return left

        mid = (left + right) // 2
        if nums[mid] < target:
            return Solution2.searchInsert(nums, target, mid + 1, right)
        elif nums[mid] > target:
            return Solution2.searchInsert(nums, target, left, mid - 1)
        else:
            return mid


if __name__ == '__main__':
    s = Solution1
    # case 1
    nums_ins = [1, 3, 5, 6]
    target_ins = 5
    exp_res = 2
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.searchInsert(nums_ins, target_ins)}")

    # case 2
    nums_ins = [1, 3, 5, 6]
    target_ins = 2
    exp_res = 1
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.searchInsert(nums_ins, target_ins)}")

    # case 3
    nums_ins = [1, 3, 5, 6]
    target_ins = 7
    exp_res = 4
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.searchInsert(nums_ins, target_ins)}")