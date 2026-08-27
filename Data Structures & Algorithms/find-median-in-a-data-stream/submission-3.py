class MedianFinder:

    def __init__(self):
        self.min_heap = [] # if odd length, min_heap size is greater by one
        self.max_heap = []
        self.length = 0

    def addNum(self, num: int) -> None:
        if not self.min_heap or num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        if len(self.min_heap) - len(self.max_heap) == 2:
            temp = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -temp)
        if len(self.max_heap) - len(self.min_heap) == 1:
            temp = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -temp)
        self.length += 1

    def findMedian(self) -> float:
        if self.length%2 == 1:
            return self.min_heap[0]
        return (self.min_heap[0] - self.max_heap[0]) / 2