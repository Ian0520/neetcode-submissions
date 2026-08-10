class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            target = -nums[i]
            while left < right:
                total = nums[left] + nums[right]
                if total == target:
                    if [-target, nums[left], nums[right]] not in results:
                        results.append([-target, nums[left], nums[right]])
                if total < target:
                    left += 1
                else:
                    right -= 1
        return results
                