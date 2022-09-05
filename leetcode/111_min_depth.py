# 2022/08/30
# 超过了50.06%
# 执行用时: 68 ms
# 内存消耗: 15 MB
from utils import build_binary_tree


class Solution1:
    @staticmethod
    def minDepth(root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        min_depth = 10e5
        if root.left is not None:
            min_depth = min(min_depth, Solution1.minDepth(root.left))
        if root.right is not None:
            min_depth = min(min_depth, Solution1.minDepth(root.right))

        return min_depth + 1


if __name__ == '__main__':
    s = Solution1
    # case 1
    root_ins = [3, 9, 20, None, None, 15, 7]
    root_ins = build_binary_tree(root_ins)
    exp_res = 2
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.minDepth(root_ins)}")

    # case 2
    root_ins = [2, None, 3, None, 4, None, 5, None, 6]
    root_ins = build_binary_tree(root_ins)
    exp_res = 5
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.minDepth(root_ins)}")
