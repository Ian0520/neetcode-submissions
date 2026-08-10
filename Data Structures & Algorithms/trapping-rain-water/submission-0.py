class Solution:
    def trap(self, height: List[int]) -> int:
        # water[i] = min(left_highest, right_highest)
        n = len(height)
        prefix = [0] * n
        high = 0
        for i in range(n):
            prefix[i] = high
            high = max(high, height[i])
        
        suffix = [0]*n
        high = 0
        for i in range(n-1,-1,-1):
            suffix[i] = high
            high = max(high, height[i])
        
        s = 0
        for i in range(n):
            s += max(0, min(prefix[i], suffix[i]) - height[i])

        return s