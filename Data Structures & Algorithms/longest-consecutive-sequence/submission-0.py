class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)

        best = 0
        for num in nums:
            if num-1 not in seen:
                cur = num
                length = 0
                while cur in seen:
                    length += 1
                    cur += 1
                best = max(length, best)
        return best