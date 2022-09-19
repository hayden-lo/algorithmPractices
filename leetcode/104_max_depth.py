from utils import build_binary_tree


# 2022/09/06
# 超过了77.37%
# 执行用时: 44 ms
# 内存消耗: 17.4 MB
class Solution1:
    @staticmethod
    # depth first search
    def maxDepth(root):
        if root is None:
            return 0

        max_depth = 0
        if root.left is not None:
            max_depth = max(max_depth, Solution1.maxDepth(root.left))
        if root.right is not None:
            max_depth = max(max_depth, Solution1.maxDepth(root.right))

        return max_depth + 1


# 2022/09/06
# 超过了98.12%
# 执行用时: 36 ms
# 内存消耗: 17.3 MB
class Solution2:
    @staticmethod
    # depth first search
    def maxDepth(root):
        if root is None:
            return 0

        left_max_depth = Solution2.maxDepth(root.left)
        right_max_depth = Solution2.maxDepth(root.right)

        return max(left_max_depth, right_max_depth) + 1


# 2022/09/06
# 超过了92.26%
# 执行用时: 40 ms
# 内存消耗: 16.2 MB
class Solution3:
    @staticmethod
    # breadth first search
    def maxDepth(root):
        if root is None:
            return 0

        queue = [root]
        h = 0
        while len(queue) > 0:
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            h += 1
        return h


if __name__ == '__main__':
    s = Solution3
    root_ins = [3, 9, 20, None, None, 15, 7]
    root_ins = build_binary_tree(root_ins)
    exp_res = 3
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.maxDepth(root_ins)}")
