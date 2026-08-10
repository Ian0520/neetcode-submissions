class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0
        right = len(s1)-1

        goal = [0] * 26
        seen = [0] * 26
        for c in s1:
            index = ord(c) - ord("a")
            goal[index] += 1

        l = 0
        for c in s2[:len(s1)]:
            seen[ord(c) - ord("a")] += 1
            if seen == goal:
                return True

        while right < len(s2)-1:
            right += 1
            seen[ord(s2[right]) - ord("a")] += 1 
            seen[ord(s2[left]) - ord("a")] -= 1
            left += 1
            if seen == goal:
                return True
        return False
            