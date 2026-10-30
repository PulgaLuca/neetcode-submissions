class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Quando arrivo alla casa i, ho soltanto due possibilità:
        Non rubo la casa i: mantengo il risultato precedente dp[i-1].
        Rubo la casa i: 
        non posso aver rubato la casa precedente, quindi aggiungo nums[i] + dp[i-2].
        '''
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = [0] * (n)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[-1]
