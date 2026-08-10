class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        result = len(temperatures) * [0]
        for i in range(len(temperatures)):
            while s and temperatures[i] > temperatures[s[-1]]:
                result[s[-1]] = i - s[-1]
                s.pop()
            s.append(i)
        return result