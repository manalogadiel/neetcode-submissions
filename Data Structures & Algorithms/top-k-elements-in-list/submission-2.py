class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = {}
        for i in set(nums):
            x[i] = nums.count(i)
        x = dict(sorted(x.items(), key = lambda x: x[1], reverse = True))
        return list(x.keys())[:k]
        

