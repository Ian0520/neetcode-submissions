class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)
        
        last_mid = 10001
        while True:
            mid = (left + right) // 2

            if mid == last_mid:
                break

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
            last_mid = mid
        return -1