from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create hashset of rows, columns and squares
        # iterate through rows and columns
            # if ".", continue
            # if value in rows/ columns or squares return false
            # else add value into rows, columns and squares
        # return true
        columns = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) # key = (r//3, c//3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in columns[c] 
                or board[r][c] in rows[r] 
                or board[r][c] in squares[r//3, c//3]):
                    return False
                
                columns[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r//3, c//3].add(board[r][c])

        return True

                