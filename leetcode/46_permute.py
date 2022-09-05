# 2022/08/31
# 超过了60.64%
# 执行用时: 40 ms
# 内存消耗: 15.1 MB
class Solution1:
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


# 2022/09/05
# 超过了82.85%
# 执行用时: 36 ms
# 内存消耗: 15.2 MB
class Solution2:
    @staticmethod
    def permute(nums):
        def dfs(idx, path):
            if idx == len(nums):
                result.append(path[:])

            for i in range(len(nums)):
                if check[i] == 0:
                    path.append(nums[i])
                    check[i] = 1
                    dfs(idx + 1, path)
                    check[i] = 0
                    path.pop()

        result = []
        check = [0 for i in range(len(nums))]
        dfs(0, [])
        return result


if __name__ == '__main__':
    s = Solution2
    nums_ins = [1, 2, 3]
    exp_res = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.permute(nums_ins)}")
