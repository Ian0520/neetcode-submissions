class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(len(board)):
            seen = set()
            for col in range(len(board[row])):
                num = board[row][col]
                if num == '.':
                    continue
                if num in seen:
                    return False
                seen.add(num)
        
        
        for col in range(len(board[0])):
            seen = set()
            for row in range(len(board)):
                num = board[row][col]
                if num == '.':
                    continue
                if num in seen:
                    return False
                seen.add(num)
        
        d = [(-1, -1), (0 ,-1), (1,-1),
             (-1,0), (0,0), (1,0),
             (-1,1), (0,1),   (1,1)]
        for x in range(1, 8, 3):
            for y in range(1, 8, 3):
                seen = set()
                for dx, dy in d:
                    num = board[x+dx][y+dy]
                    if num == '.':
                        continue
                    if num in seen:
                        return False
                    seen.add(num)
        return True
