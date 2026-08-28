class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(prev, count, i):
            if count > target:
                return
            if i >= len(nums):
                if count == target: 
                    result.append(prev)
                return
            dfs(prev, count, i+1)
            dfs(prev + [nums[i]], count + nums[i], i)
        dfs([], 0, 0)
        return result