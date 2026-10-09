class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        sortedArr = []
        for num, freq in count.items():
            sortedArr.append([freq, num])
        sortedArr.sort()

        res = []
        while len(res) < k:
            res.append(sortedArr.pop()[1])
        
        return res