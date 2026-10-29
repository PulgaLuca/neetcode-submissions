class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for coin in coins: # for each type of coin
            for current_change in range(coin, amount+1): # not trying values below the value of that coin
                dp[current_change] = min(dp[current_change], dp[current_change-coin]+1)

        return dp[-1] if dp[-1] != float('inf') else -1
