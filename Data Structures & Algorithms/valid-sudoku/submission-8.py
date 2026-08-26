class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = [0] * 9

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                index = ord(board[i][j][0]) - ord('1')
                if nums[index] == 1:
                    return False
                nums[index] = 1
            nums = [0] * 9

        for i in range(9):
            for j in range(9):
                if board[j][i] == ".":
                    continue
                index = ord(board[j][i][0]) - ord('1')
                if nums[index] == 1:
                    return False
                nums[index] = 1
            nums = [0] * 9

        for bi in range(0, 9, 3):
            for bj in range(0, 9, 3):
                for i in range(bi, bi + 3):
                    for j in range(bj, bj + 3):
                        if board[i][j] == ".":
                            continue
                        index = ord(board[i][j][0]) - ord('1')
                        if nums[index] == 1:
                            return False
                        nums[index] = 1
                nums = [0] * 9

        return True
        