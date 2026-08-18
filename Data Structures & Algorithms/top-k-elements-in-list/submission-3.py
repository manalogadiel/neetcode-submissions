class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = {}
        y = [[] for i in range(len(nums)+ 1)]

        for i in nums:
            x[i] = 1 + x.get(i, 0)
        for i, j in x.items():
            y[j].append(i)
        
        ans = []
        for i in range(len(y)-1, -1, -1):
            for j in y[i]:
                ans.append(j)
                if len(ans)==k:
                    return ans
        return []

        

        

