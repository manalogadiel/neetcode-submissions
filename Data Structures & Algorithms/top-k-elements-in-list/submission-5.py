from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        g = Counter(nums)
        x = list(sorted(g, key = lambda x: g[x], reverse = True))
        return x[:k]
       
