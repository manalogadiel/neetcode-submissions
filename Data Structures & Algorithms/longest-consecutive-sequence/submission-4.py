class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = defaultdict(list)
        x = 0
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 1:
                ans[x].append(i)
            else:
                x += 1
        z = 0
        for i, j in ans.items():
            if len(j) > z:
                z = len(j)
        if nums:
            return z+1
        else:
            return 0



        