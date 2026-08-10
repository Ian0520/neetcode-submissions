class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        best = (right - left) * min(heights[left], heights[right])
        while left < right:
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            best = max(best, (right - left) * min(heights[left], heights[right]))
        return best