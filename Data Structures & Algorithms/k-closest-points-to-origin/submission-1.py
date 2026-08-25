class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x, y in points:
            heapq.heappush(max_heap, (-(x**2 + y**2), (x,y)))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        print(max_heap)
        result = [point for d, point in max_heap]
        return result
                
        