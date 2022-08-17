# 2022/08/16
# 超过了5.13%
# 执行用时: 132 ms
# 内存消耗: 16.8 MB
class Solution:
    @staticmethod
    def trapping_rain_water(heights):
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
