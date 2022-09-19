from utils import build_binary_tree


# 2022/09/06
# 超过了11.98%
# 执行用时: 584 ms
# 内存消耗: 57.1 MB
class Solution1:
    @staticmethod
    # depth first search
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


# 2022/09/06
# 超过了32.33%
# 执行用时: 528 ms
# 内存消耗: 51.8 MB
class Solution2:
    @staticmethod
    # breadth first search
    def minDepth(root):
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
                if node.left is None and node.right is None:
                    return h + 1
            h += 1
        return h


if __name__ == '__main__':
    s = Solution2
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
