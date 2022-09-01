# 2022/09/01
# 超过了.61%
# 执行用时: 56 ms
# 内存消耗: 15 MB
class Solution:
    @staticmethod
    def combinationSum(candidates, target):
        def dfs(idx, path, residue):
            if residue == 0:
                result.append(path[:])
                return

            if residue < 0:
                return

            for i in range(idx, len(candidates)):
                # prune
                if candidates[i] > residue:
                    break

                path.append(candidates[i])
                dfs(i, path, residue - candidates[i])
                path.pop()

        candidates = sorted(candidates)
        result = []
        dfs(0, [], target)
        return result


if __name__ == '__main__':
    s = Solution
    candidates_ins = [2, 3, 6, 7]
    target_ins = 7
    exp_res = [[2, 2, 3], [7]]
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.combinationSum(candidates_ins, target_ins)}")
