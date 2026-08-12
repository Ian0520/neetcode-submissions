class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # mid on 1st part:
        #  [nums[0],nums[mid]) <-  nums[mid]  -> (nums[mid], max] and [min, nums[-1])
        # mid on 2nd part:
        # [min,nums[mid]) and [nums[0], max] <- nums[mid] -> (nums[mid] ,nums[-1]]
        left = 0 
        right = len(nums)
        while(left < right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[0]: # 1st part
                if nums[0] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid+1
            else: # 2nd part
                if nums[mid] < target <= nums[-1]:
                    left = mid+1
                else:
                    right = mid
        return -1