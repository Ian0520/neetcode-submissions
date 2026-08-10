class Solution:

    def encode(self, strs: List[str]) -> str:  
        results = str()
        for s in strs:
            results += str(len(s))
            results += '#'
            results += s
        #print(results)
        return results

    def decode(self, s: str) -> List[str]:
        results = []
        i = 0
        while i < len(s):
            n_str = ""
            while s[i] != '#':
                n_str += s[i]
                i += 1
            i += 1
            length = int(n_str)
            word = s[i : i + length]
            results.append(word)
            i += length
        return results
