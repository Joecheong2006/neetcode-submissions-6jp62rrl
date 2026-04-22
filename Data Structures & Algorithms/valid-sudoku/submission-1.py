class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            count = set()
            for e in row:
                if e == '.':
                    continue
                if e in count:
                    return False
                count.add(e)
        for j in range(9):
            count = set()
            for i in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in count:
                    return False
                count.add(board[i][j])

        for i in range(3):
            for j in range(3):
                count = set()
                for y in range(3):
                    for x in range(3):
                        e = board[i * 3 + y][j * 3 + x]
                        if e == '.':
                            continue
                        if e in count:
                            return False
                        count.add(e)
        return True