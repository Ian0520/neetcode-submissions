class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use frequency as index and store as group
        results = {}
        for word in strs:
            count = [0] * 26
            
            for char in word:
                index = ord(char) - ord('a')
                count[index] += 1

            if tuple(count) not in results:
                results[tuple(count)] = [word]
            else:
                results[tuple(count)].append(word)
        return list(results.values())