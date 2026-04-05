class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grid = defaultdict(set)
        column = defaultdict(set)
        row = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == ".":
                    continue
                    
                if(val in row[i] or val in column[j] or val in grid[(i//3, j//3)]):
                    return False
                row[i].add(val)
                column[j].add(val)
                grid[(i//3, j//3)].add(val)
        
        return True