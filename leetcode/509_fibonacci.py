# 2022/08/16
# 超过了21.04%
# 执行用时: 604 ms
# 内存消耗: 14.9 MB
class Solution:
    def fibonacci(self, n):
        # initialize
        if n <= 1:
            return n

        return self.fibonacci(n - 1) + self.fibonacci(n - 2)
