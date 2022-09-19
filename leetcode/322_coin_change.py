# 2022/09/07
# 超过了89.39%
# 执行用时: 32 ms
# 内存消耗: 15.6 MB
class Solution1:
    @staticmethod
    # depth first search
    def coinChange(coins, target):
        # initialize
        states = [[0] * (target + 1)] * len(coins)
        states[0][0] = 0

        # dynamic programming transformation
        for i in range(1, len(coins)):
            # not pick
            for j in range(target + 1):
                if states[i - 1][j]:
                    states[i][j] = states[i - 1][j]

            # pick
            for j in range(target - coins[i] + 1):
                if states[i - 1][j]:
                    states[i][j + coins[i]] = states[i - 1][j] + 1

        # optimize
        min_coins = 1e9
        for i in range(target + 1):
            if states[len(coins) - 1][i] < min_coins:
                min_coins = states[len(coins) - 1][i]

        return min_coins


if __name__ == '__main__':
    s = Solution1
    coins_ins = [1, 2, 5]
    target_ins = 11
    exp_res = 3
    print(f"Expected result: {str(exp_res)}")
    print(f"Outcome result: {s.coinChange(coins_ins, target_ins)}")
