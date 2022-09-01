# 2022/08/16
# 超过了21.04%
# 执行用时: 604 ms
# 内存消耗: 14.9 MB
class Solution:
    @staticmethod
    def fibonacci(n):
        # initialize
        if n <= 1:
            return n

        return Solution.fibonacci(n - 1) + Solution.fibonacci(n - 2)


if __name__ == '__main__':
    s = Solution
    # case 1
    n_ins = 2
    exp_res = 1
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.fibonacci(n_ins)}")

    # case 2
    n_ins = 3
    exp_res = 2
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.fibonacci(n_ins)}")

    # case 3
    n_ins = 4
    exp_res = 3
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.fibonacci(n_ins)}")
