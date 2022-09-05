# 2022/08/16
# 超过了5.13%
# 执行用时: 132 ms
# 内存消耗: 16.8 MB
class Solution1:
    # dynamic programming
    @staticmethod
    def trappingRainWater(heights):
        # mark the highest number on the left for each element
        left_max = [heights[0]] + [0] * (len(heights) - 1)
        for i in range(1, len(heights)):
            left_max[i] = max(left_max[i - 1], heights[i])

        # mark the highest number on the right for each element
        right_max = [0] * (len(heights) - 1) + [heights[-1]]
        for i in range(len(heights) - 1)[::-1]:
            right_max[i] = max(right_max[i + 1], heights[i])

        # calculate gap between cannikin height and own height for each element
        cannikin_heights = []
        for i in range(len(heights)):
            cannikin_heights.append(min(left_max[i], right_max[i]) - heights[i])

        # sum up all gaps
        return sum(cannikin_heights)


# 2022/08/16
# 超过了5.13%
# 执行用时: 132 ms
# 内存消耗: 16.8 MB
class Solution2:
    # double pointer
    @staticmethod
    def trappingRainWater(heights):
        i, j = 0, len(heights) - 1
        left_max, right_max = 0, 0
        result = 0
        while i < j:
            left_max = max(left_max, heights[i])
            right_max = max(right_max, heights[j])
            if heights[i] < heights[j]:
                result += left_max - heights[i]
                i += 1
            else:
                result += right_max - heights[j]
                j -= 1
        return result


if __name__ == '__main__':
    s = Solution2
    # case 1
    height_ins = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    exp_res = 6
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.trappingRainWater(height_ins)}")

    # case 2
    height_ins = [4, 2, 0, 3, 2, 5]
    exp_res = 9
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.trappingRainWater(height_ins)}")
