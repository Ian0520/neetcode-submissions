class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        indices = {}
        for i in range(0, len(nums), 1):
            if target - nums[i] in indices:
                return [indices[target-nums[i]], i]
            indices[nums[i]] = i
            