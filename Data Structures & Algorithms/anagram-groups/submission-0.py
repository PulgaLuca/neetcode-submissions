class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for w in strs:
            sortedWord = ''.join(sorted(w))
            res[sortedWord].append(w)
        return list(res.values())
        