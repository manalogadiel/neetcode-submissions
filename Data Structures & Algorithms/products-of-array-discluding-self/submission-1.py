class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        x = 1
        for i, j in enumerate(nums):
            for a, b  in enumerate(nums):
                if i != a:
                    x *= nums[a]
            ans.append(x)
            x=1
        return ans

