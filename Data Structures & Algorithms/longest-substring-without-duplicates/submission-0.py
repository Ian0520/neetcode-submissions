class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        seen = set()
        best = 0
        length = 0
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                length -= 1           
            length += 1
            seen.add(s[right])
            best = max(best, length)
            right += 1
        return best
                