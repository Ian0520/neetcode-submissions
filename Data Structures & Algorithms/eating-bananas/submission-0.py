class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = 1
        max_k = max(piles)+1

        while min_k < max_k:
            mid = (min_k + max_k) // 2
            
            hours_left = h
            for p in piles:
                hours_left -= p // mid 
                if p%mid > 0:
                    hours_left -= 1

            if hours_left < 0:
                min_k = mid + 1
            else:
                max_k = mid
        return max_k