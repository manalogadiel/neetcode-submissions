class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = [1] * len(nums)
        a = 1
        
        for i in range(len(nums)):
            x[i] = a
            a *= nums[i]
        
        b = 1
        
        for i in range(len(nums)-1, -1, -1):
            x[i] *= b
            b *= nums[i]
        
        return x

    
