class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def build(prev, i):
            if i >= len(nums):
                result.append(prev)
                return
            build(prev + [nums[i]], i + 1)
            build(prev, i + 1)
        build([], 0)
        return result