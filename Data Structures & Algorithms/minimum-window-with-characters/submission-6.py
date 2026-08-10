class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window: slide right until valid, 
        # then slide until just before it is not
        if len(s) < len(t) :
            return ""

        count, window = {}, {}

        for c in t:
            count[c] = count.get(c,0) + 1
        
        have, need = 0, len(count)
        l = 0
        best = ""
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in count and count[c] == window[c]:
                have += 1
            while have == need:
                if best == "" or r - l + 1 < len(best):
                    best = s[l:r+1]
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        return best
                
