# 2022/09/02
# 超过了98.48%
# 执行用时: 36 ms
# 内存消耗: 15.4 MB
class Solution:
    @staticmethod
    def permuteUnique(nums):
        def dfs(idx, path):
            if idx == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if check[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                    continue
                path.append(nums[i])
                check[i] = 1
                dfs(idx + 1, path)
                path.pop()
                check[i] = 0

        nums = sorted(nums)
        check = [0 for i in range(len(nums))]
        result = []
        dfs(0, [])

        return result


if __name__ == '__main__':
    s = Solution

    # case 1
    nums_ins = [1, 1, 2]
    exp_res = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.permuteUnique(nums_ins)}")

    # case 2
    nums_ins = [1, 2, 3]
    exp_res = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.permuteUnique(nums_ins)}")
