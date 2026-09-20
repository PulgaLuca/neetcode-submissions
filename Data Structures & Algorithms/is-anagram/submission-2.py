class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time complexity: O(n + mlogm)
        # Space complecity: O(1) or O(n+m) depending on sort algo
        if len(s) != len(t):
            return False
        
        countS, countT = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            countS[s[i]] += 1
            countT[t[i]] += 1
            
        return countS == countT