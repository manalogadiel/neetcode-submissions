from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        g = Counter(nums)
        x = list(sorted(g, key = g.get, reverse = True))
        return x[:k]
       
