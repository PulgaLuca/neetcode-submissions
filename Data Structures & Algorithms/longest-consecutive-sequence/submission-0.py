class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n^2) O(n)
        numSet = set(nums)
        longest = 0
        for n in nums:
            # start of a sequence?
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest