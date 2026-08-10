class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
            stack = []
            max_area = 0
            for index, h in enumerate(heights):
                start = index

                while stack and h < stack[-1][1]:
                    prev_start, height = stack.pop()
                    max_area = max(max_area, height*(index - prev_start))
                    start = prev_start
                stack.append((start, h))
            
            while stack:
                start, height = stack.pop()
                max_area = max(max_area, height * (len(heights) - start))

            return max_area
                