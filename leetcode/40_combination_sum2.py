# 2022/08/30
# 超过了50.06%
# 执行用时: 68 ms
# 内存消耗: 15 MB
class Solution:
    @staticmethod
    def combinationSum2(candidates, target):
        def dfs(idx, path, residue):
            if residue == 0:
                result.append(path[:])
                return

            if residue < 0:
                return

            for i in range(idx, len(candidates)):
                # prune
                if candidates[i] > target:
                    break

                if i > idx and candidates[i - 1] == candidates[i]:
                    continue

                path.append(candidates[i])
                dfs(i + 1, path, residue - candidates[i])
                path.pop()

        candidates = sorted(candidates)
        result = []
        dfs(0, [], target)
        return result


if __name__ == '__main__':
    s = Solution
    candidates_ins = [10, 1, 2, 7, 6, 1, 5]
    target_ins = 8
    exp_res = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.combinationSum2(candidates_ins, target_ins)}")
