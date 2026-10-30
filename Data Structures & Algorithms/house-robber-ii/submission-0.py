class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Because houses are in a circle, you cannot rob both the first 
        and last house.
        So we split the problem into two linear cases:
        Rob houses from index 1 to n-1 (exclude first house)
        Rob houses from index 0 to n-2 (exclude last house)
        '''
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]

        return max(self.houserobber(nums[1:]), self.houserobber(nums[:-1]))

    def houserobber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0] # take first house
        dp[1] = max(nums[0], nums[1]) # take the max between the two house

        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[-1]