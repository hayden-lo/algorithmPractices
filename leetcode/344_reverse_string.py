# 2022/09/05
# 超过了86.80%
# 执行用时: 40 ms
# 内存消耗: 19.5 MB
class Solution1:
    @staticmethod
    def reverseString(input_string):
        for i in range(len(input_string) // 2):
            input_string[i], input_string[-i - 1] = input_string[-i - 1], input_string[i]
        return input_string


# 2022/09/05
# 超过了47.49%
# 执行用时: 48 ms
# 内存消耗: 19.7 MB
class Solution2:
    @staticmethod
    def reverseString(input_string):
        i, j = 0, len(input_string) - 1
        while i < j:
            input_string[i], input_string[j] = input_string[j], input_string[i]
            i += 1
            j -= 1
        return input_string


if __name__ == '__main__':
    s = Solution2
    # case 1
    s_ins = ["h", "e", "l", "l", "o"]
    exp_res = ["o", "l", "l", "e", "h"]
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.reverseString(s_ins)}")

    # case 2
    s_ins = ["H", "a", "n", "n", "a", "h"]
    exp_res = ["h", "a", "n", "n", "a", "H"]
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.reverseString(s_ins)}")
