class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x =  set(nums)
        z = 0
        for i in x:
            if i-1 not in x:
                y = 1
                while i+y in x:
                    y+=1
                z = max(y, z)
        return z





        