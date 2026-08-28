class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i, total, path):
            if total == target:
                result.append(path.copy())
                return

            if total > target or i == len(nums):
                return

            # 選 nums[i]，同一個數字可以繼續選
            path.append(nums[i])
            dfs(i, total + nums[i], path)
            path.pop()

            # 不選 nums[i]，移到下一個數字
            dfs(i + 1, total, path)
        dfs(0, 0, [])
        return result