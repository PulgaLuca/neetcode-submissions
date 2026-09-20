class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = defaultdict(int)
        for n in nums:
            seen[n] += 1
            if seen[n] > 1:
                return True

        return False
