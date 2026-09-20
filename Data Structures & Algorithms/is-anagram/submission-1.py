class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time complexity: O(nlogn + mlogm)
        # Space complecity: O(1) or O(n+m) depending on sort algo
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
