from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board

        self.solve()

        for i in range(0, 9):
            for j in range(0, 9):
                board[i][j] = self.board[i][j]

    def possibilities(self, row, col):
        possible = {str(i) for i in range(1, 10)}

        big_row = (row // 3) * 3;
        big_col = (col // 3) * 3;

        for i in range(9):
            # Row
            if self.board[row][i] in possible:
                possible.remove(self.board[row][i])
            # Column
            if self.board[i][col] in possible:
                possible.remove(self.board[i][col])
            if self.board[big_row + i // 3][big_col + i % 3] in possible:
                possible.remove(self.board[big_row + i // 3][big_col + i % 3])

        return possible

    def solve(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == ".":
                    for value in self.possibilities(i, j):
                        self.board[i][j] = value
                        if self.solve():
                            return True
                        self.board[i][j] = "."
                    return False  # Point A
        return True
