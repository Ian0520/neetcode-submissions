class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        results = [1] * n

        prefix = 1
        for i in range(n):
            results[i] *= prefix
            prefix *= nums[i]
        prefix = 1
        for i in range(n-1,-1,-1):
            results[i] *= prefix
            prefix *= nums[i]
        return results