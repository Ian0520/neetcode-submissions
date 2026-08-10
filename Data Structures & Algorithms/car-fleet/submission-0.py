class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # car in the back deleted, when collide with front
        pair = [[p,s] for p,s in zip(position,speed)]
        stack = []

        for p, s in sorted(pair)[::-1]: #Reversed Sorted order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # collide
                stack.pop()
        return len(stack)