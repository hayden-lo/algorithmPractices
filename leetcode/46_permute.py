# 2022/08/31
# 超过了30.87%
# 执行用时: 11 ms
# 内存消耗: 15.1 MB
class Solution:
    @staticmethod
    def permute(nums):
        def dfs(idx, path):
            if idx == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                num = nums[i]
                if num not in path:
                    path.append(num)
                    dfs(idx + 1, path)
                    path.pop()

        result = []
        dfs(0, [])

        return result


if __name__ == '__main__':
    s = Solution
    nums_ins = [1, 2, 3]
    exp_res = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.permute(nums_ins)}")
